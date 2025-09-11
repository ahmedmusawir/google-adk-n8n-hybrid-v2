# /product_agent/agent.py
from google.adk import Agent  
from google.adk.tools import FunctionTool
from utils.gcs_utils import fetch_instructions
from utils.context_utils import fetch_context
from google.adk.code_executors import BuiltInCodeExecutor

# 1. Create the tool by wrapping our new fetch_context function.
#    The agent will automatically read its description and arguments
#    from the function's docstring.
product_context_tool = FunctionTool(func=fetch_context)

# Creating the built in code executor
# code_executor = BuiltInCodeExecutor() --> this will not work when tools are used

def get_live_instructions(ctx) -> str:
    return fetch_instructions("product_agent")

# 2. Defined the product_agent, w/ code_executor & context reader tool.
root_agent = Agent(
    name="product_agent",
    model="gemini-2.5-flash",
    description="Product Specialist agent",
    instruction=get_live_instructions,
    # code_executor=code_executor, --> this will not work when tools are used
    tools=[product_context_tool]
)
