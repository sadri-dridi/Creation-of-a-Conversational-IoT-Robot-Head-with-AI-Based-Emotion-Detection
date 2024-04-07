import openai
import os
from dotenv import load_dotenv

load_dotenv()

def preguntar(history, msg):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    messages = []
    for input_text, completion_text in history:
        messages.append({"role": "user", "content": input_text})
        messages.append({"role": "assistant", "content": completion_text})

    messages.append({"role": "user", "content": msg})

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        completion_text = completion.choices[0].message['content']

        history.append((msg, completion_text))

        return history

    except Exception as error:
        print(str(error))

    return None


    
def chatbot(msg):
    global history
    history = preguntar(history, msg)
    return history[-1][1]

if __name__ == "__main__":
    history = []
    query = "can you make a hello_word in python?"
    sentiment_score = classify_sentiment(query)
    print(f"Sentiment Score: {sentiment_score}")
    response = chatbot(query)
    print(response)