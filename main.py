import streamlit as st
import pandas as pd
import numpy as np

def run_code():
    
    st.header("Financial Stock Analysis")
    prompt=st.chat_input("Enter your message here...")

    if prompt:
        st.write("You entered:", prompt)
        # Here you can add the logic to process the input and display results


if __name__ == "__main__":
    # This is a comment
    # print("Hello")
    # print("
    run_code()
    