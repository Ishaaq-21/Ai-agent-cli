import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)


resp = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")


if resp.usage_metadata is not None: 
    print("Prompt tokens usage:", resp.usage_metadata.prompt_token_count)
    print("Resp Tokens : ", resp.usage_metadata.candidates_token_count)
else: 
    raise RuntimeError("Api call failed")


print("Reponse: \n", resp.text)