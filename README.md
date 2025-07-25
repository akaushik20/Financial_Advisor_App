# 💸 Financial Advisor App — Agentic AI Workflow

This app simulates a multi-agent financial advisor using real-time data, OpenAI-powered insights, and an interactive Streamlit UI. It's designed to provide personalized investment advice based on user inputs, market conditions, and risk preferences — just like a human advisor would.

---

## 🧠 What It Does

- 🧑‍💼 **Profile Agent**: Collects user inputs (investment amount, risk appetite, goals)
- 📊 **Market Agent**: Fetches real-time stock data from Polygon.io based on user risk profile
- 🤖 **Advisor Agent**: Uses OpenAI LLMs to generate friendly, explainable investment advice
- ✅ (Optional) **Compliance Agent**: Placeholder for rule-checking against investment policies

---

## ⚙️ Tech Stack

- **LangGraph** for multi-agent workflow orchestration
- **Streamlit** for frontend interaction
- **OpenAI API** for generating human-like financial suggestions
- **Polygon.io** for stock/ETF prices (real-time)
- **Finnhub** (planned): For analyst sentiment and financial fundamentals

---

## 🚀 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/akaushik20/Financial_Advisor_App.git
   cd Financial_Advisor_App
