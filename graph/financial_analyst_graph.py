#create a graph here
from langgraph.graph import StateGraph, START, END, Graph
from app.shared_state import AdvisorState
from app.profile_agent import profile_agent
from app.market_agent import market_agent
from app.advisor_agent import advisor_agent

def build_graph() -> Graph:
    """
    Build the LangGraph for the financial advisor app.
    
    Returns:
        Graph[AdvisorState]: The constructed graph for the financial advisor app.
    """
    builder = StateGraph(AdvisorState)
    builder.add_node("Profile Agent", profile_agent)
    builder.add_node("Market Agent", market_agent)
    builder.add_node("Advisor Agent", advisor_agent)

    builder.add_edge(START, "Profile Agent")
    builder.add_edge("Profile Agent","Market Agent")
    builder.add_edge("Market Agent", "Advisor Agent")
    builder.add_edge("Advisor Agent", END)

    return builder.compile()