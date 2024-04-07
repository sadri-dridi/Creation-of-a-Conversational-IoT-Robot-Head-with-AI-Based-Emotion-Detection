import openai
import os
from dotenv import load_dotenv

load_dotenv()

def analyze_sentiment(msg):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Craft a system message that instructs the model to perform sentiment analysis.
    sentiment_system_message = {
        "role": "system",
        "content": "Classify the sentiment of the following message as positive, neutral, or negative: {}.".format(msg)
    }

    try:
        # Get the sentiment analysis from the model
        sentiment_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[sentiment_system_message, {"role": "user", "content": msg}]
        )
        sentiment_analysis_result = sentiment_completion.choices[0].message['content']

        # Assuming the model returns a single word or a phrase with the sentiment, extract it.
        # You might need to adjust the parsing here depending on the actual output format.
        sentiment = sentiment_analysis_result.split('.')[0].strip()

        return sentiment

    except Exception as error:
        print(str(error))
        return "Error"

def get_response(history, msg):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    messages = [{"role": "user", "content": input_text} for input_text, _ in history]
    messages += [{"role": "assistant", "content": completion_text} for _, completion_text in history]
    messages.append({"role": "user", "content": msg})

    try:
        # Get the response from the model
        response_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        response_text = response_completion.choices[0].message['content']
        return response_text

    except Exception as error:
        print(str(error))
        return "Error"

def chatbot(msg):
    global history
    sentiment = analyze_sentiment(msg)
    response = get_response(history, msg)
    history.append((msg, response))
    return response, sentiment

if __name__ == "__main__":
    history = []
    query = "how do i find teh dimension of a matrix ?"
    response, sentiment_score = chatbot(query)
    print(f"Response: {response}")
    print(f"Sentiment: {sentiment_score}")
