from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
import re
import getpass
import os

load_dotenv(find_dotenv(), override=True)

if 'GOOGLE_API_KEY' not in os.environ:
    os.environ['GOOGLE_API_KEY'] = getpass.getpass('Provide your Google API Key: ')

@tool
def add_numbers(query: str) -> str:
    """Add numbers."""
    nums = re.findall(r"\d+", query)
    return str(int(nums[0]) + int(nums[1]))

@tool
def subtract_numbers(query: str) -> str:
    """Subtract numbers."""
    nums = re.findall(r"\d+", query)
    return str(int(nums[0]) - int(nums[1]))

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.9)

agent = create_agent(llm, [add_numbers, subtract_numbers])

# Conversation loop to keep the agent interactive by maintaining full chat history
history = []

print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    history.append({"role": "user", "content": user_input})

    result = agent.invoke({"messages": history})

    reply = result["messages"][-1].content
    print("Agent:", reply)

    history.append({"role": "assistant", "content": reply})


