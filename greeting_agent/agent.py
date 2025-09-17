import os # 1. Import the 'os' module to read environment variables
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from utils.gcs_utils import fetch_instructions
from utils.context_utils import fetch_document

# 2. Import the LiteLlm class from the ADK's model library
from google.adk.models.lite_llm import LiteLlm

# 3. Create the configured LiteLLM client instance
#    We'll use a powerful default model from OpenRouter.
lite_llm_client = LiteLlm(
    model="openrouter/deepseek/deepseek-chat-v3-0324", # 164k context + 671B params
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# --- The Resume Reader Tool ---

resume_reader_tool = FunctionTool(func=fetch_document)

def get_live_instructions(ctx) -> str:
    """This function is passed to the Agent and called on every run."""
    print("--- FETCHING LIVE INSTRUCTIONS via callable argument ---")
    return fetch_instructions("greeting_agent")

# 4. Update the Agent to use the new LiteLLM client
root_agent = Agent(
    name="greeting_agent",
    model=lite_llm_client, # <-- This is the only line that changes here
    description="Greeting agent",
    instruction=get_live_instructions,
    tools=[resume_reader_tool]
)