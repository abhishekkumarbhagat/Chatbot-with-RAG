# Insurance Support Chatbot with RAG

A Python-based Retrieval-Augmented Generation (RAG) chatbot designed for insurance customer support. This chatbot is trained on your insurance plan documents to answer questions about benefits, coverage, and plan details. It uses OpenAI for both language understanding and for creating document embeddings.

## 🎯 Objective

Develop a RAG chatbot trained on customer support documentation to assist users by answering queries and providing relevant support information.

## ✅ Key Features

- **Knowledge-Based Responses**: Only answers questions using information from the provided insurance documents.
- **Strict Boundary Enforcement**: Responds with "I don't know" for any question outside the knowledge base.
- **User-Friendly Interface**: Modern and simple web interface built with Streamlit.
- **Multi-Format Support**: Loads both PDF and DOCX files from the `knowledgebase` folder.
- **Cloud-Native Embeddings**: Uses OpenAI's embedding service, avoiding local dependency issues.
- **Secure Deployment**: API keys are protected using environment variables.

## 📋 Requirements Met

1. ✅ **Source-Based Answers**: Bot answers questions only from the provided insurance documents
2. ✅ **Boundary Enforcement**: Responds "I don't know" for questions outside the knowledge base
3. ✅ **User-Friendly Interface**: Clean, intuitive chat interface with sidebar information

## 🏗️ Project Structure

The project has been cleaned up to contain only the essential files.

```
.
├── .github/                # (Optional) GitHub Actions workflows
├── .streamlit/             # Streamlit deployment configuration
├── knowledgebase/          # Folder for your PDF and DOCX files
├── .gitignore              # Files and folders ignored by Git
├── phase_3.py              # The main Streamlit application logic
├── requirements.txt        # List of dependencies for deployment
└── README.md               # This file
```

## 🚀 Quick Start & Deployment Guide

This guide covers both running the app locally and deploying it to Streamlit Community Cloud.

### Prerequisites

- Python 3.11+
- Git
- An OpenAI API key (get one at [platform.openai.com](https://platform.openai.com/))

### Part 1: Running Locally

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/abhishekkumarbhagat/Chatbot-with-RAG.git
    cd Chatbot-with-RAG
    ```

2.  **Install Dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Set Up Your API Key:**
    Create a file named `.env` in the root of the project and add your API key to it:
    ```
    OPENAI_API_KEY='your-sk-xxxx-api-key-here'
    ```
    This file is already in `.gitignore` to prevent it from being committed.

4.  **Add Your Documents:**
    Place your PDF and DOCX insurance documents inside the `knowledgebase/` folder.

5.  **Run the App:**
    ```bash
    streamlit run phase_3.py
    ```
    The app should open in your web browser.

### Part 2: Deploying to Streamlit Community Cloud

This is the recommended and easiest way to host your chatbot for free.

1.  **Push to GitHub:**
    Ensure your `knowledgebase` folder and all your latest code are pushed to your GitHub repository. The `fix/deployment` branch is confirmed to be working.

2.  **Create an App on Streamlit Cloud:**
    - Go to [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.
    - Click **"New app"**.

3.  **Configure and Deploy:**
    - **Repository**: Select `abhishekkumarbhagat/Chatbot-with-RAG`.
    - **Branch**: Select `fix/deployment`.
    - **Main file path**: Set to `phase_3.py`.
    - Click **"Advanced settings..."**.

4.  **Add Your Secret Key:**
    - In the "Secrets" text box, paste your OpenAI API key in TOML format:
      ```toml
      OPENAI_API_KEY = "your-sk-xxxx-api-key-here"
      ```
    - Click **"Save"**.

5.  **Deploy!**
    - Click the **"Deploy!"** button. Your app will be live in a few minutes.

## 🔒 Security

- **API Key Protection**: Your OpenAI key is loaded from a `.env` file locally and from Streamlit's secret manager in the cloud. It is **never** exposed in the code or on GitHub.
- **`.gitignore`**: The `.gitignore` file is configured to prevent sensitive files like `.env` from ever being tracked by git.

---

*This project is ready for use and further development.*

## 🎮 Usage

### Running Locally

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

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `PORT`: Port for deployment (optional, defaults to 8501)

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
- **Real-time Responses**: Fast answers using OpenAI's models
- **Chat History**: Maintains conversation context
- **Clear Chat**: Option to reset conversation
- **Loading Indicators**: Visual feedback during processing

## 🔒 Privacy & Security

- **Local Processing**: Documents are processed locally
- **No External Storage**: No data is sent to external servers (except OpenAI API)
- **API Key Security**: Store your OPENAI_API_KEY securely
- **Environment Variables**: Sensitive data kept out of code

### Getting Help

- Check the console output for error messages
- Ensure all dependencies are installed: `pipenv install`
- Verify your OpenAI API key is valid
- Check deployment platform documentation

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 🚀 Deployment Status

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://insurance-support-chatbot.streamlit.app)

*Replace the badge URL with your actual deployed app URL*
