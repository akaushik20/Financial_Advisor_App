import sys
import os
from dotenv import load_dotenv

import openai
from openai import OpenAI
from shared_state import AdvisorState


load_dotenv()

openai_apikey=os.getenv("OPENAI_API_KEY")
client=OpenAI(api_key = openai_apikey)

def advisor_agent(state: AdvisorState) -> AdvisorState:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", 
             "content": "how is the market today? What are the best stocks to invest in?"}
        ],
        temperature=0.7
    )

    print(response)
    state['advice'] = {
        'advice': response}

    return state

