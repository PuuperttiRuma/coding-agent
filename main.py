import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"

def main():
    # Command line arguments
    verbose = False
    user_prompt = ""

    if len(sys.argv) == 1:
        print("No prompt given, exiting.")
        sys.exit(1)
        
    for arg in sys.argv:
        if arg == "--verbose":
            verbose = True
        else:
            user_prompt = sys.argv[1]
         
    # Chat
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model=model,
        contents=messages
    )

    print(response.text)
    if verbose: 
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
