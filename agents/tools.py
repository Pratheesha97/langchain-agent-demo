from langchain.tools import tool
import re

@tool
def add_numbers(query: str) -> str:
    """Add numbers mentioned in the query."""
    nums = re.findall(r"\d+", query)
    if len(nums) < 2:
        return "Please provide at least two numbers."
    return str(int(nums[0]) + int(nums[1]))

@tool
def subtract_numbers(query: str) -> str:
    """Subtract numbers mentioned in the query."""
    nums = re.findall(r"\d+", query)
    if len(nums) < 2:
        return "Please provide at least two numbers."
    return str(int(nums[0]) - int(nums[1]))
