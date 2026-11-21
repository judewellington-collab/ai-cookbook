import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Write a limerick about the Python programming language.",
    config=types.GenerateContentConfig(
        system_instruction="You're a helpful assistant.",
    ),
)

print(response.text)
