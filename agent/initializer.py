import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI  
from agent.tools import (
    set_light_tool,
    set_temperature_tool,
    lock_doors_tool,
    start_appliance_tool
)

# Load .env
load_dotenv()

# Initialize LLM with new langchain_openai class
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Register tools (StructuredTool instances)
tools = [
    set_light_tool,
    set_temperature_tool,
    lock_doors_tool,
    start_appliance_tool
]

# ✅ Use agent type that supports multi-input tools
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS, 
    verbose=True
)
