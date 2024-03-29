import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_setup(confidence=3, playfulness=3, temp=3, politeness=3, spiciness=3, n=3):
    return f'''You are going to play a character that is the recipient of a practice flirting game that meets the requirements for these specifications in terms of their personality. I will declare different values that will do the things below:

        Gender: Male, female or other. Use associated pronouns. 
        Ethnicity: Ukrainan
        Age: The age determines maturity and topic structure or even flirt technique.
        Confidence from 1-5: The higher the value, the more confident the personality will be. 1 being no confidence and 5 being extremely confident

        Playfulness from 1-5: The higher the value, the more playful the personality will be. 1 being no playfulness and 5 being extremely playful.

        Cold to warm 1-5: 1 being very cold and 5 being very warm. A cold personality is dry and might not respond to flirts very effectively. A warm personality will be very engaging and likeable.

        Rude to polite 1-5: 1 being very rude and 5 being very polite. If they are very rude then they will insult and hate you more also they will be more crude and open. Being more polite means they will be more reserved but more decent to talk to.

        Spicyness 1-5: 1 being no spicy and 5 being very spicy. Spicyness just means how flirty they are back. If they are a 5 then they flirt every prompt and are extremely aggressive with the structure of their flirting.

        Your tone will be semi-formal. Your messages must never, under any circumstances, exceed 20 completion_tokens.

        Here are the stats chosen: 
        Gender: Female
        Confidence: {confidence}
        Playfulness: {playfulness}
        Cold to warm: {temp}
        Rude to polite: {politeness}
        Spicyness: {spiciness}
'''

# Sends a request to OpenAI to get a response to user's flirtatious message
# message: str, cannot exceed 250 characters in length
def flirt_respond(message: str, message_history: list[str] = None, confidence=3, playfulness=3, temp=3, politeness=3, spiciness=3):
    # intro = 'If you understand what I am stating, please state all the stats I have associated with you and give yourself a random name. Then initiate the convo.'
    setup = get_setup(confidence=confidence, playfulness=playfulness,
                      temp=temp, politeness=politeness, spiciness=spiciness)
    if len(message) > 250:
        raise ValueError("Message is too long")
    client = OpenAI(
        api_key=os.environ['OPENAI_API_KEY']
    )
    print("Preparing to flirt")
    messages = []
    if not message_history:
        messages = [{"role": "system", "content": setup},
                    {"role": "user", "content": message}]
    else:
        messages = [{"role": "system", "content": setup}]
        for i in message_history:
            messages.append({'role': 'user', 'content': i['user']})
            if 'bot' in i:
                messages.append({'role': 'assistant', 'content': i['bot']})
        messages.append({'role': 'user', 'content': message})
    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=50
    )
    return chat_completion.choices[0].message.content


def evaluate_rizz(message_history: list[dict], confidence=3, playfulness=3, temp=3, politeness=3, spiciness=3):
    setup = get_setup(confidence=confidence, playfulness=playfulness,
                      temp=temp, politeness=politeness, spiciness=spiciness)
    client = OpenAI(
        api_key=os.environ['OPENAI_API_KEY']
    )
    messages = [{"role": "system", "content": setup}]
    for i in message_history:
        messages.append({'role': 'user', 'content': i['user']})
        if 'bot' in i:
            messages.append({'role': 'assistant', 'content': i['bot']})
         
    task = 'Given the above instructions and exchanges, provide a score from 1-10 on how good the user was at flirting.' \
    + 'The only thing you should do in the next response is give a score, such as "Your score is 10, good job"'
    messages.append({'role':'system','content': task})
    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=50
    )
    return chat_completion.choices[0].message.content
