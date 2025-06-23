## This script will act as the profile agent for the financial advisor app.
import sys
import os

# Add the directory of this file to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shared_state import userInputs, AdvisorState


## Define a function for  profiling the user inputs
def profile_agent(state: AdvisorState) -> AdvisorState:
    """
    This function processes the user inputs to create a profile for the financial advisor app.
    
    Parameters:
    user_inputs (dict): A dictionary containing user inputs such as investment amount, risk appetite, and additional comments.
    
    Returns:
    dict: A dictionary containing the processed profile information.
    """
    
    # Process the user inputs to create a profile
    ui=state.get("user_input", {})

    profile = {
        "Investment Amount": ui.get("investment_amount", 0),
        "Risk Appetite": ui.get("risk_appetite", "Medium"),
        "Additional Comments": ui.get("additional_comments", "")
    }

    state["profile"] = profile
    
    return state
