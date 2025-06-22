# Insurance Support Chatbot with RAG

A Python-based Retrieval-Augmented Generation (RAG) chatbot specifically designed for insurance customer support. This chatbot is trained on insurance plan documents and can answer questions about benefits, coverage, and plan details.

## 🎯 Objective

Develop a RAG chatbot trained on customer support documentation to assist users by answering queries and providing relevant support information.

## ✅ Key Features

- **Knowledge-Based Responses**: Only answers questions based on information present in the provided insurance documents
- **Strict Boundary**: Responds with "I don't know" for questions outside the knowledge base
- **User-Friendly Interface**: Modern Streamlit web interface with chat functionality
- **Multi-Format Support**: Loads both PDF and DOCX files from the knowledge base
- **Real-Time Processing**: Uses OpenAI's GPT models for quick responses
- **Secure Deployment**: API keys protected through environment variables

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
├── requirements.txt             # Dependencies for deployment
├── phase_1.py                   # Basic Streamlit UI
├── phase_2.py                   # LLM integration
├── phase_3.py                   # Full RAG implementation
├── app.py                       # Main application entry point
├── run_chatbot.py              # Helper script to run the chatbot
├── test_api.py                 # API key test script
├── Procfile                    # Deployment configuration
├── runtime.txt                 # Python version specification
├── .streamlit/config.toml      # Streamlit configuration
└── knowledgebase/              # Insurance documents folder
    ├── *.pdf                   # PDF insurance documents
    └── *.docx                  # DOCX insurance documents
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Pipenv (for dependency management)
- OpenAI API key (get one at https://platform.openai.com/)

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Chatbot-with-RAG-main
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   ```

3. **Set up your OpenAI API key:**
   ```bash
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```

4. **Add your insurance documents:**
   - Place your PDF and DOCX insurance documents in the `knowledgebase/` folder
   - The chatbot will automatically load all supported files

5. **Run the chatbot:**
   ```bash
   python run_chatbot.py
   ```

## 🌐 GitHub Deployment

### Option 1: Deploy to Streamlit Cloud (Recommended)

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set the main file path to: `phase_3.py`
   - Add your secrets:
     - Go to "Advanced settings"
     - Add secret: `OPENAI_API_KEY` with your API key value

3. **Your app will be live at:** `https://your-app-name.streamlit.app`

### Option 2: Deploy to Railway

1. **Connect to Railway:**
   - Go to [railway.app](https://railway.app)
   - Sign in with GitHub
   - Click "New Project"
   - Select "Deploy from GitHub repo"

2. **Configure environment variables:**
   - Add `OPENAI_API_KEY` with your API key
   - Add `PORT` (Railway will set this automatically)

3. **Deploy:**
   - Railway will automatically detect the Procfile and deploy

### Option 3: Deploy to Heroku

1. **Install Heroku CLI and login:**
   ```bash
   heroku login
   ```

2. **Create Heroku app:**
   ```bash
   heroku create your-app-name
   ```

3. **Set environment variables:**
   ```bash
   heroku config:set OPENAI_API_KEY=your-api-key-here
   ```

4. **Deploy:**
   ```bash
   git push heroku main
   ```

## 🔒 Security Best Practices

### API Key Protection

1. **Never commit API keys to Git:**
   - The `.env` file is in `.gitignore`
   - Use environment variables in production

2. **Use deployment platform secrets:**
   - Streamlit Cloud: Advanced settings → Secrets
   - Railway: Environment variables
   - Heroku: `heroku config:set`

3. **Rotate keys regularly:**
   - Generate new API keys periodically
   - Update environment variables accordingly

### Environment Variables

```bash
# Required
OPENAI_API_KEY=your-openai-api-key

# Optional (for deployment)
PORT=8501
```

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

## 🐛 Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY not found"**
   - Set your API key in `.env` file locally
   - Use deployment platform secrets for production

2. **"No documents found"**
   - Ensure PDF/DOCX files are in the `knowledgebase/` folder
   - Check file permissions

3. **"Failed to load documents"**
   - Verify file formats are supported (PDF/DOCX)
   - Check file integrity

4. **Deployment issues**
   - Check that `requirements.txt` is up to date
   - Verify environment variables are set correctly
   - Check deployment platform logs

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
