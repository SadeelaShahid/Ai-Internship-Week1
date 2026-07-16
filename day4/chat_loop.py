import os
from dotenv import load_dotenv
from openai import OpenAI
from config import SYSTEM_PROMPT

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("Error: OPENROUTER_API_KEY not found. Check your .env file.")
    exit(1)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

print("Chat started! Type 'quit' or 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ("quit", "exit"):
        print("Chat ended. Bye!")
        break

    try:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            timeout=15,
        )
        print("Bot:", response.choices[0].message.content)

    except Exception as e:
        print("Something went wrong while talking to the model.")
        print(f"Details: {e}")

    print()