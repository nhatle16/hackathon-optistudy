import os
from langchain_nebius import ChatNebius
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

from src.tools.pdf_tools import extract_syllabus_text

load_dotenv()

# Initialize Nebius Chat Model
model = ChatNebius(
    model="openai/gpt-oss-120b",
    temperature=0.3,     # agent thinks more straightforward, less creative
    max_tokens=300,
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.getenv("NEBIUS_API_KEY"),
    reasoning_effort="low"  # skip internal inference
)

# Create an agent
agent = create_agent(
    model=model,
    tools=[extract_syllabus_text]
)

# Invoke the agent
query = "Explain briefly what is derivative?"
response = agent.invoke({"messages": [HumanMessage(content=query)]})

print(response["messages"][-1].content)
