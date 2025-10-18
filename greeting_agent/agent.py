from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from utils.gcs_utils import fetch_instructions
from utils.context_utils import fetch_document

# --- The Resume Reader Tool ---
resume_reader_tool = FunctionTool(func=fetch_document)

def get_live_instructions(ctx) -> str:
    """This function is passed to the Agent and called on every run."""
    print("--- FETCHING LIVE INSTRUCTIONS via callable argument ---")
    return fetch_instructions("greeting_agent")

# 4. Update the Agent to use Vertex
root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash", 
    description="Greeting agent",
    instruction=get_live_instructions,
    tools=[resume_reader_tool]
)