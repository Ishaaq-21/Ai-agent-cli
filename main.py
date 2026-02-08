import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
# --verbose flag
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


resp = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages)


if resp.usage_metadata is not None: 
    print("Prompt tokens:", resp.usage_metadata.prompt_token_count)
    print("Response tokens: ", resp.usage_metadata.candidates_token_count)
else: 
    raise RuntimeError("Api call failed")


print("Response: \n", resp.text)