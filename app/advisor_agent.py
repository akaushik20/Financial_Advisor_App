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
    profile = state.get("profile")
    market_data = state.get("market_data")

    amount=profile.get("Investment Amount", 0)
    risk_appetite = profile.get("Risk Appetite", "Medium")
    additional_comments = profile.get("Additional Comments", "")

    stocks = market_data.get("stocks", [])
    crypto= market_data.get("crypto", [])
    market_data.get("stock_prices", [])


    prompt = f'''You are a financial advisor. 
    A user wants to invest {amount} with a risk level: {risk_appetite}. 
    Here are available investment option and other inputs
    1. Stocks - {stocks}
    2. Cryptocurrencies - {crypto}
    3. Additional User Comments - {additional_comments}
    4. Market Data - {market_data}

    Based on the above information, recommend a simple diversified portfolio using both stocks and crypto (if appropriate).
Explain the reasoning in clear, simple terms.
'''
    print(f"Prompt for Advisor Agent: {prompt}")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", 
             "content": prompt}
        ],
        temperature=0.7
    )

    state['advice'] = {
        'advice': response.choices[0].message.content}

    return state

