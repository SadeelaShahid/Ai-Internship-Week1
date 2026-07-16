import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

SYSTEM_PROMPT = """You are a data extraction tool. Extract the name, city, and intent from the user's message.
Reply with ONLY a valid JSON object in this exact format, nothing else:
{"name": "...", "city": "...", "intent": "..."}
Do not add any explanation, greeting, or extra text. Only output the JSON."""

messages_to_test = [
    "Hi, I'm Ahmed from Lahore, I want to book a flight to Karachi.",
    "My name is Sara and I live in Islamabad. I need help resetting my password.",
    "This is Bilal from Multan, I want to cancel my subscription.",
]

for msg in messages_to_test:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": msg}
        ]
    )
    print(f"Input: {msg}")
    print(f"Output: {response.choices[0].message.content}")
    print("---")
