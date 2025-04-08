import google.generativeai as genai
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Configure Gemini with environment variable
    GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
    if not GOOGLE_API_KEY:
        print("Error: GEMINI_API_KEY not found in environment variables")
        return
        
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    print("AI Chatbot CLI (Type 'exit' to quit)")
    print("-----------------------------------")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break
            
        try:
            response = model.generate_content(user_input)
            print(f"\nAI: {response.text}")
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main() 