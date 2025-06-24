## This will act as main.py for the whole flow

import streamlit as st
import pandas as pd
import numpy as np

from app.profile_agent import profile_agent
from app.shared_state import userInputs, AdvisorState
from graph.financial_analyst_graph import build_graph


def run_code():
    
    st.header("Financial Stock Analysis")
    #prompt=st.chat_input("Enter your message here...")

    amt=st.number_input("Enter the amount you are planning to invest: ")
    risk_app=st.selectbox("Select the Risk Appetite for your investment Portfolio: ", ["High", "Medium", "Low"])
    prompt = st.text_input("Anything else you would like to add?", max_chars=5000)

    input_submit=st.button("Submit")
    
    user_inputs = {}
    if input_submit:
        #create a dictionary to store the user inputs
        user_inputs = {
            "investment_amount": amt,
            "risk_appetite": risk_app,
            "additional_comments": prompt
            }
        # Display the user inputs in a table
        st.write("User Inputs:")
        st.write(pd.DataFrame(user_inputs, index=[0]))
    return user_inputs

if __name__ == "__main__":
    user_inputs=run_code()
    
    if user_inputs:
        #call Profile Agent
        st.write("Advisor Agent is being called...")

        state: AdvisorState = {
            "user_input": user_inputs,
            "profile": None,
            "market_data": None,
            "advice": None,
            "compliance_check": None
        }

        # Build the graph
        graph = build_graph()
        final_state=graph.invoke(state)

        # Call the profile agent with the user inputs
        #st.subheader("Profile Agent Output")
        #st.json(final_state["profile"])

        #st.subheader("Market Agent Output.")
        #st.json(final_state["market_data"])

        st.subheader("Advice Agent Output")
        st.markdown(final_state["advice"]["advice"])




