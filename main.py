import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from call_functions import available_functions
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
#user prompt argument
parser.add_argument("user_prompt", type=str, help="User prompt")
# --verbose flag
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


resp = client.models.generate_content(
    model="gemini-2.5-flash",
    contents= args.user_prompt, 
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature= 0),
    )

if args.verbose:
    if resp.usage_metadata is not None:
        print("User prompt: ", args.user_prompt)
        print("Prompt tokens:", resp.usage_metadata.prompt_token_count)
        print("Response tokens: ", resp.usage_metadata.candidates_token_count)
    else:
        raise RuntimeError("Api call failed")
if resp.function_calls is not None:
    for function_call in resp.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
        print("\n")

print(resp.text)