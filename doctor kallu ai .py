from dotenv import load_dotenv #dotenv is a librery and load_dotenv is that tool that open and read .env file 
from google import genai
import os # this is for python so he can access my files 
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
    except :
        print("Oops! Something went wrong. Please try again later.")