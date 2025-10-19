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

code_executor = BuiltInCodeExecutor()

def get_live_instructions(ctx) -> str:
    return fetch_instructions("calc_agent")

# 3. Instantiate the Agent in the original, simple way.
#    The ADK will now use our global configuration when it creates
#    its internal client for this model string.
root_agent = Agent(
    model="gemini-2.5-flash",
    name="calc_agent",
    description="Calculator agent",
    instruction=get_live_instructions,
    code_executor=code_executor, # THIS MAKES THE AGENT MEMORY FAIL BUT THE TOOL WORKSs
)