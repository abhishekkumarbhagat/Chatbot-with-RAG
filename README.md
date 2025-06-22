# Insurance Support Chatbot with RAG

A Python-based Retrieval-Augmented Generation (RAG) chatbot designed for insurance customer support. This chatbot is trained on your insurance plan documents to answer questions about benefits, coverage, and plan details. It uses OpenAI for both language understanding and for creating document embeddings.

## 🎯 Objective

To develop a RAG chatbot trained on customer support documentation that can assist users by answering queries strictly based on the provided information.

## ✅ Key Features

- **Knowledge-Based Responses**: Only answers questions using information from the provided insurance documents.
- **Strict Boundary Enforcement**: Responds with "I don't know" for any question outside the knowledge base.
- **User-Friendly Interface**: Modern and simple web interface built with Streamlit.
- **Multi-Format Support**: Loads both PDF and DOCX files from the `knowledgebase` folder.
- **Web Scraping Integration**: Automatically scrapes support articles from AngelOne support portal (https://www.angelone.in/support).
- **Cloud-Native Embeddings**: Uses OpenAI's embedding service, avoiding local GPU/CPU dependency issues.
- **Secure Deployment**: API keys are protected using environment variables and are not stored in the code.

## 🏗️ Project Structure

```
.
├── .github/workflows/         # GitHub Actions for CI/CD (optional)
├── .streamlit/config.toml     # Streamlit deployment configuration
├── knowledgebase/             # Folder for your PDF and DOCX files
├── .gitignore                 # Files and folders ignored by Git
├── app.py                     # Entry point for some deployment platforms
├── phase_3.py                 # The main Streamlit application logic
├── requirements.txt           # List of dependencies for deployment
├── test_dependencies.py       # Script to test all dependencies
├── README.md                  # This file
└── ...
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

### Testing Dependencies

Before running the app, you can test if all dependencies are properly installed:

```bash
python test_dependencies.py
```

This will verify that all required packages are available and working correctly.

### Part 2: Deploying to Streamlit Community Cloud

This is the recommended and easiest way to host your chatbot for free.

1.  **Push to GitHub:**
    Make sure your `knowledgebase` folder and all your latest code are pushed to your GitHub repository. The `fix/deployment` branch is confirmed to be working.

2.  **Create an App on Streamlit Cloud:**
    - Go to [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.
    - Click **"New app"**.

3.  **Configure and Deploy:**
    - **Repository**: Select `your-github-name/Chatbot-with-RAG`.
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

## 🧠 How RAG Works

This chatbot uses Retrieval-Augmented Generation (RAG) to provide accurate, source-based answers:

1.  **Document Loading**: Your PDF and DOCX files from the `knowledgebase` are loaded.
2.  **Text Chunking**: Documents are split into smaller, manageable chunks.
3.  **Vector Embedding (via OpenAI)**: Each chunk is converted into a numerical representation (embedding) using OpenAI's powerful models.
4.  **Query Processing**: When you ask a question, it's also converted into an embedding.
5.  **Answer Generation**: The most relevant document chunks are sent to the OpenAI LLM along with your original question, and it generates an answer based *only* on that provided information.

## 📚 Knowledge Base

The chatbot combines multiple sources of information:

- **Local Documents**: PDF and DOCX files from the `knowledgebase/` folder
- **Web Integration**: Automatically scrapes support articles from AngelOne support portal
- **Dynamic Content**: Combines local documents with live web content for comprehensive knowledge base
- **Fallback Mechanism**: If web scraping fails, the chatbot continues to work with local documents only

## 🔒 Security

- **API Key Protection**: Your OpenAI key is loaded from a `.env` file locally and from Streamlit's secret manager in the cloud. It is **never** exposed in the code or on GitHub.
- **`.gitignore`**: The `.gitignore` file is configured to prevent sensitive files like `.env` from ever being tracked by git.
---

*This project is ready for use and further development.*
