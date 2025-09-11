import os
# 1. Import the necessary base library and ADK components.
from google import genai
from google.adk.agents import Agent
from google.adk.tools import google_search
from utils.gcs_utils import fetch_instructions

# 2. Configure the global genai session for Vertex AI.
#    This is the crucial step. We run it for its side effect.
#    Any subsequent ADK action will use these settings.
genai.Client(
    vertexai=True,
    project=os.getenv("GOOGLE_PROJECT_ID"),
    location=os.getenv("GOOGLE_LOCATION"), # "us-east1" or "global" 
)

# --- Get Instruction Set from gcs bucket ---
def get_live_instructions(ctx) -> str:
    """This function is passed to the Agent and called on every run."""
    return fetch_instructions("jarvis_agent")


# 3. Update the Agent to use the new LiteLLM client
root_agent = Agent(
    name="jarvis_agent",
    model="gemini-2.5-pro", 
    description="Jarvis agent",
    instruction=get_live_instructions,
    tools=[google_search],
)