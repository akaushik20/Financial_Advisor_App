from typing_extensions import TypedDict
from typing import Optional, Dict
#Define the State for the user inputs

class userInputs(TypedDict):
    """
    This class defines the structure for user inputs in the financial advisor app.
    
    Attributes:
    Investment Amount (float): The amount the user plans to invest.
    Risk Appetite (str): The user's risk appetite, e.g., "High", "Medium", "Low".
    Additional Comments (str): Any additional comments or information provided by the user.
    """
    Investment_Amount: float
    Risk_Appetite: str
    Additional_Comments: str

class AdvisorState(TypedDict):
    """
    This class defines the state for the financial advisor app.
    
    Attributes:
    userInputs (userInputs): The user inputs for the financial advisor app.
    """
    user_input: Optional[userInputs]
    profile: Optional[Dict[str, any]]
    market_data: Optional[Dict[str, any]]
    advice: Optional[Dict[str, any]]
    compliance_check: Optional[Dict[str, any]]
