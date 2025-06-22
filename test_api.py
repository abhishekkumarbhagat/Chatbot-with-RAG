#!/usr/bin/env python3
"""
Simple test script to verify OpenAI API key
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

def test_openai_api():
    """Test if the OpenAI API key is working"""
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ OPENAI_API_KEY not found in .env file")
        return False
    
    print(f"✅ Found API key: {api_key[:10]}...")
    
    try:
        client = OpenAI(api_key=api_key)
        
        # Test with a simple completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'Hello, API is working!'"}
            ],
            max_tokens=10
        )
        
        print("✅ API test successful!")
        print(f"Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ API test failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧪 Testing OpenAI API Key...")
    print("=" * 40)
    test_openai_api() 