from langchain.tools import tool
import re
import requests


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


@tool
def fetch_sales_data(query: str = "") -> str:
    """Fetch sales data from the local FastAPI REST API."""
    try:
        response = requests.get("http://localhost:8000/sales")
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Failed to fetch sales data: {str(e)}"
