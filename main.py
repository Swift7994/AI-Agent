import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if not api_key:
        print("GEMINI_API_KEY environment variable is not set.")
        exit(1)

    if len(sys.argv) > 1:
        contents = sys.argv[1]
    else:
        print("No input provided.")
        exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=contents)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )

    if len(sys.argv) > 2:
        if "--verbose" in sys.argv[2:]:
            print(f"User prompt: {contents}")
            prompt_tokens = response.usage_metadata.prompt_token_count
            response_tokens = response.usage_metadata.candidates_token_count
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")
            
            
    print(response.text)

if __name__ == "__main__":
    main()