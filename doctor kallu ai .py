from dotenv import load_dotenv
from google import genai
import os 
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="you are a doctor, only answer medical related questions"
    )
)

while True:
    user_input = input("you: ")

    if user_input.lower() == "quit":
        break

    try:
        response = chat.send_message(user_input)
        print(f"gemini: {response.text}")
    except Exception as e:
     print(f"error: {e}") 