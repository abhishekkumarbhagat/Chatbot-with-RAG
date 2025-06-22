#!/usr/bin/env python3
"""
Insurance Support Chatbot - Main Application
This is the main entry point for the deployed application.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import and run the main application
if __name__ == "__main__":
    import streamlit.web.cli as stcli
    
    # Set up the command line arguments for Streamlit
    sys.argv = [
        "streamlit", "run", "phase_3.py",
        "--server.port", "8501",
        "--server.address", "0.0.0.0"
    ]
    
    # Run Streamlit
    sys.exit(stcli.main()) 