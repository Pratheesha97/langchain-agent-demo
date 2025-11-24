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

result = agent.invoke({
    "messages": [{"role": "user", "content": "What is 12 - 5?"}]
})

print(result["messages"][-1].content)

