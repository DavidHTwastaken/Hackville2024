import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Sends a request to OpenAI to get a response to user's flirtatious message
# message: str, cannot exceed 250 characters in length
def flirt_respond(message: str):
    if len(message) > 250:
        raise ValueError("Message is too long")
    client = OpenAI(
        api_key=os.environ['OPENAI_API_KEY']
    )

    prompt = 'Respond as though the user is trying to flirt with you. Respond with personalized tone.'
    print("Preparing to flirt")
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt},
                  {"role": "user", "content": message}],
        max_tokens=50
    )
    return chat_completion.choices[0].message.content
