"""Check available Gemini models with your API key"""
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ No GOOGLE_API_KEY found. Please add it to your .env file")
else:
    genai.configure(api_key=api_key)
    print("🔍 Available models for generateContent:\n")
    
    try:
        models = genai.list_models()
        available = []
        
        for m in models:
            if 'generateContent' in m.supported_generation_methods:
                model_name = m.name.split('/')[-1]
                available.append(model_name)
                print(f"  ✅ {model_name}")
        
        if available:
            print(f"\n✨ Recommended model: {available[0]}")
        else:
            print("⚠️  No models available")
            
    except Exception as e:
        print(f"❌ Error listing models: {e}")
