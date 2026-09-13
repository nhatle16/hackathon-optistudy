import os
from langchain_nebius import ChatNebius
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# Initialize Nebius Chat Model
chat = ChatNebius(
    model="openai/gpt-oss-120b",
    temperature=0.3,     # agent thinks more straightforward, less creative
    max_tokens=300,
    reasoning_effort="low"  # skip internal inference
)

# Invoke the model
messages = [HumanMessage(content="Explain briefly what is derivative?")]
response = chat.invoke(messages)

print(response.content)
