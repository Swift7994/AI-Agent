import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt, max_iterations
from functions.call_function import call_function, available_functions



    


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("GEMINI_API_KEY environment variable is not set.")
        exit(1)

    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]
    verbose = "--verbose" in args
    contents = next((arg for arg in args if not arg.startswith("--")), None)

    if not contents:
        print("No input provided.")
        exit(1)

    if verbose:
        print(f"User prompt: {contents}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=contents)]),
    ]

    iters = 0
    while True:
        iters += 1
        if iters > max_iterations:
            print(f"Maximum iterations ({max_iterations}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            
    if not response.function_calls:
        return response.text
    
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    
    messages.append(types.Content(role="user", parts=function_responses))

if __name__ == "__main__":
    main()