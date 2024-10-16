import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL")
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def create_completion(prompt, model="gpt-4o"):
    response = client.chat.completions.create(
        model=model, temperature=0.5, messages=[{"role": "user", "content": prompt}]
    )
    return response
