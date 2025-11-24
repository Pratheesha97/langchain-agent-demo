from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from dotenv import load_dotenv
import re

load_dotenv()

@tool
def add_numbers(query: str) -> str:
    """Add numbers."""
    nums = re.findall(r"\d+", query)
    return str(int(nums[0]) + int(nums[1]))

llm = ChatOpenAI(model="gpt-4o")

agent = create_agent(llm, [add_numbers])

print(agent.invoke({"input": "What is 12 + 5?"}))
