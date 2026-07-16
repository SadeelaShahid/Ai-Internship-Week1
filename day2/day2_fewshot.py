import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

messages = [
    {"role": "system",
     "content": "You clean up messy sentences into grammatically correct, clear sentences. Only output the cleaned sentence, nothing else."},

    {"role": "user", "content": "me and him goes to market yesterday for buy some stuff"},
    {"role": "assistant", "content": "He and I went to the market yesterday to buy some things."},

    {"role": "user", "content": "she dont know nothing about this project i think"},
    {"role": "assistant", "content": "I don't think she knows anything about this project."},

    {"role": "user", "content": "there was many peoples at the event was so loud"},
    {"role": "assistant", "content": "There were many people at the event, and it was very loud."},

    {"role": "user", "content": "he not coming today because he sick and also his car broke"},
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages
)

print("Messy input: he not coming today because he sick and also his car broke")
print("Cleaned output:", response.choices[0].message.content)
