# Insurance Support Chatbot with RAG

A Python-based Retrieval-Augmented Generation (RAG) chatbot specifically designed for insurance customer support. This chatbot is trained on insurance plan documents and can answer questions about benefits, coverage, and plan details.

## 🎯 Objective

Develop a RAG chatbot trained on customer support documentation to assist users by answering queries and providing relevant support information.

## ✅ Key Features

- **Knowledge-Based Responses**: Only answers questions based on information present in the provided insurance documents
- **Strict Boundary**: Responds with "I don't know" for questions outside the knowledge base
- **User-Friendly Interface**: Modern Streamlit web interface with chat functionality
- **Multi-Format Support**: Loads both PDF and DOCX files from the knowledge base
- **Real-Time Processing**: Uses Groq's fast LLM for quick responses

## 📋 Requirements Met

1. ✅ **Source-Based Answers**: Bot answers questions only from the provided insurance documents
2. ✅ **Boundary Enforcement**: Responds "I don't know" for questions outside the knowledge base
3. ✅ **User-Friendly Interface**: Clean, intuitive chat interface with sidebar information

## 🏗️ Project Structure

```
Chatbot-with-RAG-main/
├── README.md                    # Project documentation
├── .gitignore                   # Python-specific exclusions
├── Pipfile                      # Dependencies (Pipenv)
├── Pipfile.lock                 # Locked dependencies
├── phase_1.py                   # Basic Streamlit UI
├── phase_2.py                   # LLM integration
├── phase_3.py                   # Full RAG implementation
├── run_chatbot.py              # Helper script to run the chatbot
└── knowledgebase/              # Insurance documents folder
    ├── *.pdf                   # PDF insurance documents
    └── *.docx                  # DOCX insurance documents
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Pipenv (for dependency management)
- GROQ API key (free at https://console.groq.com/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Chatbot-with-RAG-main
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   ```

3. **Set up your GROQ API key:**
   ```bash
   export GROQ_API_KEY='your-api-key-here'
   ```

4. **Add your insurance documents:**
   - Place your PDF and DOCX insurance documents in the `knowledgebase/` folder
   - The chatbot will automatically load all supported files

5. **Run the chatbot:**
   ```bash
   python run_chatbot.py
   ```

## 🎮 Usage

### Running the Chatbot

**Option 1: Using the helper script (Recommended)**
```bash
python run_chatbot.py
```

**Option 2: Direct Streamlit command**
```bash
pipenv run streamlit run phase_3.py
```

### Using the Chatbot

1. **Open your browser** to the URL shown in the terminal (usually http://localhost:8501)
2. **Ask questions** about your insurance plans, such as:
   - "What is my deductible for the Gold plan?"
   - "What services are covered under my plan?"
   - "What is the copay for specialist visits?"
3. **Get answers** based only on your insurance documents
4. **Clear chat history** using the button at the bottom

## 🔧 Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)

### Knowledge Base

- **Location**: `./knowledgebase/` folder
- **Supported Formats**: PDF and DOCX files
- **Auto-loading**: All supported files are automatically loaded on startup

## 🧠 How RAG Works

This chatbot uses Retrieval-Augmented Generation (RAG) to provide accurate, source-based answers:

1. **Document Loading**: Insurance documents are loaded and processed
2. **Text Chunking**: Documents are split into manageable chunks
3. **Vector Embedding**: Chunks are converted to vector representations
4. **Query Processing**: User questions are embedded and matched to relevant chunks
5. **Answer Generation**: The LLM generates answers based on retrieved information
6. **Boundary Enforcement**: Only information from the knowledge base is used

## 🎨 Interface Features

- **Modern Chat Interface**: Clean, responsive design
- **Sidebar Information**: Shows loaded documents and chatbot capabilities
- **Real-time Responses**: Fast answers using Groq's LLM
- **Chat History**: Maintains conversation context
- **Clear Chat**: Option to reset conversation
- **Loading Indicators**: Visual feedback during processing

## 🔒 Privacy & Security

- **Local Processing**: Documents are processed locally
- **No External Storage**: No data is sent to external servers (except Groq API)
- **API Key Security**: Store your GROQ_API_KEY securely

## 🐛 Troubleshooting

### Common Issues

1. **"GROQ_API_KEY not found"**
   - Set your API key: `export GROQ_API_KEY='your-key'`
   - Get a free key at https://console.groq.com/

2. **"No documents found"**
   - Ensure PDF/DOCX files are in the `knowledgebase/` folder
   - Check file permissions

3. **"Failed to load documents"**
   - Verify file formats are supported (PDF/DOCX)
   - Check file integrity

### Getting Help

- Check the console output for error messages
- Ensure all dependencies are installed: `pipenv install`
- Verify your GROQ API key is valid

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to submit issues and enhancement requests!
