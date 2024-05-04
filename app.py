import chainlit as cl
import requests
import json

# Function to send user input to the API endpoint and get a response
def chat(text):
    response = requests.post(
        'http://74.68.156.74:8000/predict',
        headers={"Content-Type": "application/json"},
        data=json.dumps({"text": text})
    )
    if response.status_code == 200:
        bot_response = response.json().get("prediction", "")
        bot_response = bot_response.replace("</s>", "")
        return bot_response
    else:
        return "Error: Unable to fetch output from the API endpoint URL"



@cl.on_message
async def main(message: cl.Message):
    # Get user input
    user_input = message.content

    # Get bot response
    bot_response = chat(user_input)

    # Send a response back to the user
    await cl.Message(
        content=f"{bot_response}",
    ).send()