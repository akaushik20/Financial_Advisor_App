## This script will act as the profile agent for the financial advisor app.
import sys
import os
from dotenv import load_dotenv
import requests
from shared_state import AdvisorState

import config 



# Add the directory of this file to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from .env file
load_dotenv()
# Fetch the environment variables
POLYGON_API_KEY=os.getenv("POLYGON_API_KEY", None)


# Asset selection by risk profile
def get_assets_by_risk(risk: str):
    risk = risk.lower()
    categories = config.RISK_CATEGORY_MAP.get(risk,["index_etfs"])
    stocks, crypto = [], []

    for i in categories:
        assets = config.STOCK_POOL.get(i, [])
        if i == "crypto":
            crypto.extend(assets)
        else: 
            stocks.extend(assets)
    
    return stocks, crypto

    
# Fetch stock prices from Polygon
def fetch_polygon_stocks(symbols):
    # Define the dictionary to hold stock prices
    prices = {}
    if not POLYGON_API_KEY:
        raise ValueError("Polygon API key is not set. Please set the POLYGON_API_KEY environment variable.")    
    for i in symbols:
        url= f"https://api.polygon.io/v1/open-close/{i}/2025-06-20?adjusted=true&apiKey={POLYGON_API_KEY}"
        response=requests.get(url)
        if response.status_code ==200:
            data=response.json()
            print(data)
            prices[i] = data['close']
        else:
            print(f"Failed to fetch data for {i}. Status code: {response.status_code}")
    return prices

def market_agent(state: AdvisorState) -> AdvisorState:
    profile=state.get("profile", {})
    risk_profile = profile.get("Risk Appetite", "Low").lower()
    print(f"Risk Profile: {risk_profile}")

    stocks, crypto=get_assets_by_risk(risk_profile)
    print(f"Selected Stocks: {stocks}, Selected Crypto: {crypto}")
    stock_price=fetch_polygon_stocks(stocks)
    # For simplicity, we will not fetch crypto prices in this example
    #print(f"Stock Prices: {stock_price['close']}")

    state["market_data"] = {
        "stocks": stocks,
        "crypto": crypto,
        "stock_prices": stock_price}
    return state
