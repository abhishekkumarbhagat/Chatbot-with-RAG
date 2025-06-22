#!/usr/bin/env python3
"""
Insurance Support Chatbot Runner
This script helps you set up and run the RAG chatbot with your insurance documents.
"""

import os
import subprocess
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def check_openai_api_key():
    """Check if OPENAI_API_KEY is set"""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY not found!")
        print("\nTo set your OpenAI API key, you have two options:")
        print("\nOption 1: Set it in the .env file (Recommended):")
        print("echo 'OPENAI_API_KEY=your-api-key-here' > .env")
        print("python run_chatbot.py")
        
        print("\nOption 2: Set it temporarily for this session:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        print("python run_chatbot.py")
        
        print("\nTo get an OpenAI API key:")
        print("1. Go to https://platform.openai.com/")
        print("2. Sign up or log in")
        print("3. Go to API Keys section")
        print("4. Create a new API key")
        print("5. Copy the key and set it as shown above")
        
        return False
    else:
        print("✅ OPENAI_API_KEY is set")
        return True

def check_knowledgebase():
    """Check if knowledgebase folder exists and has files"""
    knowledgebase_path = "./knowledgebase"
    if not os.path.exists(knowledgebase_path):
        print("❌ Knowledgebase folder not found!")
        print("Please create a 'knowledgebase' folder and add your PDF/DOCX files.")
        return False
    
    files = [f for f in os.listdir(knowledgebase_path) 
             if f.lower().endswith(('.pdf', '.docx'))]
    
    if not files:
        print("❌ No PDF or DOCX files found in knowledgebase folder!")
        print("Please add your insurance documents to the knowledgebase folder.")
        return False
    
    print(f"✅ Found {len(files)} document(s) in knowledgebase:")
    for file in files:
        print(f"   • {file}")
    return True

def main():
    print("🏥 Insurance Support Chatbot Setup")
    print("=" * 40)
    
    # Check prerequisites
    if not check_openai_api_key():
        return
    
    if not check_knowledgebase():
        return
    
    print("\n🚀 Starting the chatbot...")
    print("The chatbot will open in your web browser.")
    print("Press Ctrl+C to stop the chatbot.")
    print("-" * 40)
    
    try:
        # Run the Streamlit app
        subprocess.run([
            sys.executable, "-m", "pipenv", "run", "streamlit", "run", "phase_3.py"
        ])
    except KeyboardInterrupt:
        print("\n👋 Chatbot stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error running chatbot: {e}")

if __name__ == "__main__":
    main() 