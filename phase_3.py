# Phase 1 libraries
import os
import warnings
import logging

import streamlit as st

# Phase 2 libraries
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Phase 3 libraries
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA

# Disable warnings and info logs
warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)

# Page configuration
st.set_page_config(
    page_title="Insurance Support Chatbot",
    page_icon="🏥",
    layout="wide"
)

st.title('🏥 Insurance Support Chatbot')
st.markdown("**Your AI assistant for insurance plan questions and support**")
st.markdown("---")

# Sidebar for information
with st.sidebar:
    st.header("ℹ️ About this Chatbot")
    st.markdown("""
    This chatbot is trained on your insurance plan documents and can help you with:
    - Plan benefits and coverage details
    - Deductibles and copays
    - Network information
    - Claims and billing questions
    
    **Note:** The chatbot will only answer questions based on the information available in your insurance documents.
    """)
    
    st.header("📚 Knowledge Base")
    st.markdown("Loaded documents:")
    knowledgebase_path = "./knowledgebase"
    if os.path.exists(knowledgebase_path):
        for filename in os.listdir(knowledgebase_path):
            if filename.lower().endswith(('.pdf', '.docx')):
                st.markdown(f"• {filename}")

# Setup a session state variable to hold all the old messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display all the historical messages
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Phase 3 (Pre-requisite)
@st.cache_resource
def get_vectorstore():
    knowledgebase_path = "./knowledgebase"
    loaders = []
    
    # Check if knowledgebase folder exists
    if not os.path.exists(knowledgebase_path):
        st.error(f"Knowledgebase folder not found at {knowledgebase_path}")
        return None
    
    # Load all PDF and DOCX files from knowledgebase folder
    loaded_files = []
    for filename in os.listdir(knowledgebase_path):
        file_path = os.path.join(knowledgebase_path, filename)
        if filename.lower().endswith('.pdf'):
            try:
                loaders.append(PyPDFLoader(file_path))
                loaded_files.append(filename)
            except Exception as e:
                st.warning(f"Failed to load PDF {filename}: {str(e)}")
        elif filename.lower().endswith('.docx'):
            try:
                loaders.append(Docx2txtLoader(file_path))
                loaded_files.append(filename)
            except Exception as e:
                st.warning(f"Failed to load DOCX {filename}: {str(e)}")
    
    if not loaders:
        st.error("No valid PDF or DOCX files found in knowledgebase folder")
        return None
    
    try:
        # Create chunks, aka vector database–Chromadb
        index = VectorstoreIndexCreator(
            embedding=HuggingFaceEmbeddings(model_name='all-MiniLM-L12-v2'),
            text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        ).from_loaders(loaders)
        
        with st.sidebar:
            st.success(f"✅ Successfully loaded {len(loaded_files)} documents!")
            for file in loaded_files:
                st.markdown(f"• {file}")
        
        return index.vectorstore
    except Exception as e:
        st.error(f"Error creating vector store: {str(e)}")
        return None

# Initialize vector store
with st.spinner("Loading knowledge base..."):
    vectorstore = get_vectorstore()

if vectorstore is None:
    st.error("❌ Failed to load knowledge base. Please check your GROQ_API_KEY and knowledgebase folder.")
    st.stop()

prompt = st.chat_input('Ask about your insurance benefits...')

if prompt:
    # Display user message
    with st.chat_message('user'):
        st.markdown(prompt)
    
    # Store the user prompt in state
    st.session_state.messages.append({'role':'user', 'content': prompt})
    
    # Check if GROQ_API_KEY is set
    if not os.environ.get("GROQ_API_KEY"):
        with st.chat_message('assistant'):
            st.error("❌ GROQ_API_KEY not found. Please set your Groq API key as an environment variable.")
        st.session_state.messages.append(
            {'role':'assistant', 'content': "I'm sorry, I cannot access the knowledge base. Please set your GROQ_API_KEY."})
    else:
        # Phase 2 - Setup LLM
        groq_sys_prompt = ChatPromptTemplate.from_template("""You are an expert insurance support assistant. You can ONLY answer questions based on the information provided in the insurance documents in your knowledge base.

IMPORTANT RULES:
1. ONLY answer questions using information from the provided insurance documents
2. If the question cannot be answered using the information in the documents, respond with exactly: "I don't know"
3. Do not make up information or use external knowledge
4. Be specific and reference plan details when possible
5. If you're unsure about something, say "I don't know"

Question: {user_prompt}

Answer based ONLY on the insurance documents:""")

        model = "llama3-8b-8192"

        groq_chat = ChatGroq(
                groq_api_key=os.environ.get("GROQ_API_KEY"), 
                model_name=model
        )

        # Phase 3 - RAG Implementation
        try:
            with st.spinner("Searching knowledge base..."):
                chain = RetrievalQA.from_chain_type(
                    llm=groq_chat,
                    chain_type='stuff',
                    retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
                    return_source_documents=True)
               
                result = chain({"query": prompt})
                response = result["result"]
                
                # Check if the response indicates no relevant information found
                if not response or response.strip() == "" or "don't know" in response.lower():
                    response = "I don't know"
                
            with st.chat_message('assistant'):
                st.markdown(response)
            
            st.session_state.messages.append(
                {'role':'assistant', 'content': response})
                
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            if "GROQ_API_KEY" in str(e):
                error_msg = "❌ GROQ_API_KEY not found. Please set your Groq API key as an environment variable."
            
            with st.chat_message('assistant'):
                st.error(error_msg)
            
            st.session_state.messages.append(
                {'role':'assistant', 'content': "I'm sorry, I encountered an error. Please check your API key and try again."})

# Add a clear chat button
if st.button("🗑️ Clear Chat History"):
    st.session_state.messages = []
    st.rerun()


