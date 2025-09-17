# /product_agent/agent.py
import os
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from utils.gcs_utils import fetch_instructions
from utils.context_utils import fetch_context

# 1. Import the LiteLlm class
from google.adk.models.lite_llm import LiteLlm

# 2. Create the configured LiteLLM client instance
lite_llm_client = LiteLlm(
    model="openrouter/openai/gpt-5-nano",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


# --- Tool and Instruction logic ---
product_context_tool = FunctionTool(func=fetch_context)

def get_live_instructions(ctx) -> str:
    return fetch_instructions("product_agent")

# 3. Update the Agent to use the new LiteLLM client
root_agent = Agent(
    name="product_agent",
    model=lite_llm_client, 
    description="Product Specialist agent",
    instruction=get_live_instructions,
    tools=[product_context_tool]
)
