## This script will act as the profile agent for the financial advisor app.
import sys
import os
from dotenv import load_dotenv
import requests
from shared_state import AdvisorState

import config 
import streamlit as st



# Add the directory of this file to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from .env file
load_dotenv()
# Fetch the environment variables
POLYGON_API_KEY=os.getenv("POLYGON_API_KEY", None)
FINNHUB_API_KEY=os.getenv("FINNHUB_API_KEY", None)

LOW_RISK_SYMBOLS = [
    "SPY",  # S&P 500 ETF
    "VOO",  # Vanguard S&P 500 ETF
    "VTI",  # Total Market ETF
    "BND",  # Bond ETF
    "JNJ",  # Johnson & Johnson
    "PG",   # Procter & Gamble
    "KO",   # Coca-Cola
    "PEP",  # PepsiCo
    "WMT",  # Walmart
    "HD",   # Home Depot
    "MCD",  # McDonald's
    "XLP",  # Consumer Staples ETF
]

MEDIUM_RISK_SYMBOLS = [
    "AAPL",  # Apple
    "MSFT",  # Microsoft
    "GOOGL", # Alphabet
    "AMZN",  # Amazon
    "NVDA",  # Nvidia
    "META",  # Meta Platforms
    "VUG",   # Vanguard Growth ETF
    "QQQ",   # Nasdaq 100 ETF
    "XLF",   # Financials ETF
    "UNH",   # UnitedHealth
    "JPM",   # JPMorgan Chase
]

HIGH_RISK_SYMBOLS = [
    "ARKK",  # ARK Innovation ETF
    "TSLA",  # Tesla
    "COIN",  # Coinbase
    "PLTR",  # Palantir
    "SQ",    # Block (formerly Square)
    "SOFI",  # SoFi Technologies
    "RBLX",  # Roblox
    "AFRM",  # Affirm
    "RIOT",  # Riot Blockchain
    "MARA",  # Marathon Digital
    "XBI",   # Biotech ETF
]

POPULAR_SYMBOLS = LOW_RISK_SYMBOLS + MEDIUM_RISK_SYMBOLS + HIGH_RISK_SYMBOLS

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

def fetch_analyst_recommendations(symbols, risk):
    selected_stocks = []
    if not FINNHUB_API_KEY:
        raise ValueError("Finnhub API key is not set.")
    else:
        for symbol in symbols:
            url= f"https://finnhub.io/api/v1/stock/recommendation?symbol={symbol}&token={FINNHUB_API_KEY}"
            response = requests.get(url)
            if response.status_code==200:
                data = response.json()
                #print(f"Analyst recommendations for {symbol}: {data}")
                if not data:
                    continue
                latest=data[0]
                if latest['buy']>=10 and risk=="low":
                    selected_stocks.append(symbol)
                elif (latest['buy']+latest['strongBuy'])>=15 and risk=="medium":
                    selected_stocks.append(symbol)
                elif latest['strongBuy']>=10 and risk=="high":
                    selected_stocks.append(symbol)
                else:
                    print(f"Skipping {symbol} due to insufficient recommendations for risk profile {risk}.")
            else:
                raise ValueError(f"Failed to fetch data for {symbol}. Status code: {response.status_code}")
            
    return selected_stocks



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

    #calling the recommendation function
    recommended_stocks=fetch_analyst_recommendations(POPULAR_SYMBOLS, risk_profile)

    #stocks, crypto=get_assets_by_risk(recommended_stocks)
    print(f"Selected Stocks: {recommended_stocks}")
    ##, Selected Crypto: {crypto}")
    crypto = []
    stock_price=fetch_polygon_stocks(recommended_stocks)


    state["market_data"] = {
        "stocks": recommended_stocks,
        "crypto": crypto,
        "stock_prices": stock_price}
    return state
