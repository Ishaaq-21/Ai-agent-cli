import os
from dotenv import load_dotenv
from google import genai
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()


resp = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=args.user_prompt)


if resp.usage_metadata is not None: 
    print("Prompt tokens:", resp.usage_metadata.prompt_token_count)
    print("Response tokens: ", resp.usage_metadata.candidates_token_count)
else: 
    raise RuntimeError("Api call failed")


print("Response: \n", resp.text)