from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def flirt_respond(message: str):
    if len(message) > 250:
        raise ValueError("Message is too long")
    client = OpenAI()

    prompt = 'Respond as though the user is trying to flirt with you'

    chat_completion = client.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt},
                  {"role": "user", "content": message}],
        max_tokens=250
    )
    return chat_completion['choices'][0]['message']['content']
