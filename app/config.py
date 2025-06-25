RISK_CATEGORY_MAP = {
    "low": ["bond_etfs", "dividend_etfs", "defensive_stocks"],
    "medium": ["index_etfs", "blue_chip", "sector_etfs"],
    "high": ["growth_stocks", "crypto", "innovation_etfs"]
}

STOCK_POOL = {
    "bond_etfs": [
        "BND",  # Vanguard Total Bond
        "AGG",  # iShares Core U.S. Aggregate Bond
        "TLT",  # iShares 20+ Year Treasury
        "LQD",  # iShares Investment Grade Corp Bond
        "SHY"   # iShares 1-3 Year Treasury Bond ETF
    ],
    "dividend_etfs": [
        "VIG",  # Vanguard Dividend Appreciation
        "SCHD", # Schwab U.S. Dividend Equity
        "NOBL", # S&P 500 Dividend Aristocrats
        "DVY",  # iShares Select Dividend ETF
        "HDV"   # iShares Core High Dividend
    ],
    "defensive_stocks": [
        "KO", "PEP", "JNJ", "PG", "WMT", "COST"
    ],
    "index_etfs": [
        "SPY", "VOO", "VTI", "IVV", "QQQ", "DIA"
    ],
    "blue_chip": [
        "AAPL", "MSFT", "JPM", "V", "MA", "UNH", "META"
    ],
    "sector_etfs": [
        "XLK",  # Tech
        "XLV",  # Health
        "XLF",  # Finance
        "XLY",  # Consumer Discretionary
        "XLE"   # Energy
    ],
    "growth_stocks": [
        "TSLA", "NVDA", "AMD", "SHOP", "SNOW", "PLTR", "CRWD"
    ],
    "innovation_etfs": [
        "ARKK", "ARKG", "ARKF", "CIBR", "BOTZ"
    ],
    "crypto": [
        "BTC", "ETH", "SOL", "AVAX", "MATIC", "DOT"
    ]
}