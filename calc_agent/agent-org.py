# /calc_agent/agent.py

import os
# 1. Import the necessary base library and ADK components.
from google import genai
from google.adk.agents import Agent
from google.adk.code_executors import BuiltInCodeExecutor
from utils.gcs_utils import fetch_instructions

# 2. Configure the global genai session for Vertex AI.
#    This is the crucial step. We run it for its side effect.
#    Any subsequent ADK action will use these settings.
genai.Client(
    vertexai=True,
    project=os.getenv("GOOGLE_PROJECT_ID"),
    location=os.getenv("GOOGLE_LOCATION"), # "us-east1" or "global" 
)

# code_executor = BuiltInCodeExecutor()

def get_live_instructions(ctx) -> str:
    return fetch_instructions("calc_agent")

def calculate(expression: str) -> float:
    """
    Calculator tool for mathematical expressions.
    Supports: +, -, *, /, **, sqrt, sin, cos, tan, log
    
    Example: "2 + 2" or "sqrt(16) * 3"
    """
    import math
    import re
    
    # Replace function names
    expression = expression.replace('sqrt', 'math.sqrt')
    expression = expression.replace('sin', 'math.sin')
    expression = expression.replace('cos', 'math.cos')
    expression = expression.replace('tan', 'math.tan')
    expression = expression.replace('log', 'math.log')
    
    # Safe eval with restricted scope
    allowed_names = {
        'math': math,
        'abs': abs,
        'round': round,
        'min': min,
        'max': max,
    }
    
    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return float(result)
    except Exception as e:
        raise ValueError(f"Cannot calculate '{expression}': {str(e)}")

# 3. Instantiate the Agent in the original, simple way.
#    The ADK will now use our global configuration when it creates
#    its internal client for this model string.
root_agent = Agent(
    model="gemini-2.5-flash",
    name="calc_agent",
    description="Calculator agent with long-term memory",
    instruction=get_live_instructions,
    tools=[calculate],  # Custom Calculator tool
)