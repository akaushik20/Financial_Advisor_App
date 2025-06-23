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
    prompt = f'''You are a financial advisor. The user has input amount: enter amount, 
    risk appetite: enter risk appetite, and additional comments: enter additional comments.
    Here are the invetment options for risk appetite listed below:

    1. High Risk: Stocks, Cryptocurrencies, Commodities
    2. Medium Risk: Mutual Funds, ETFs, Bonds
    3. Low Risk: Fixed Deposits, Savings Accounts, Government Bonds

    Depending on the above information can you summarize the market conditions and provide investment advice?
      
    Based on the user inputs, provide investment advice.'''

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

