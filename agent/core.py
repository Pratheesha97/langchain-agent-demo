import os
import getpass
from dotenv import load_dotenv, find_dotenv

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from agent.tools import (
    add_numbers,
    subtract_numbers,
    fetch_sales_data
)

# Load API keys from .env
load_dotenv(find_dotenv(), override=True)

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Provide your Google API Key: ")


def main():
    """Initialize and run the LangChain Agent."""

    # Initialize Gemini through LangChain
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.7,
    )

    # Register tools
    tools = [
        add_numbers,
        subtract_numbers,
        fetch_sales_data
    ]

    # Create the agent
    agent = create_agent(llm, tools)

    print("\nAgent with REST API Integration is running!")
    print("Type 'exit' to quit.\n")

    # Chat history storage
    history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        history.append({"role": "user", "content": user_input})

        try:
            result = agent.invoke({"messages": history})
            reply = result["messages"][-1].content

            print("Agent:", reply)
            history.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("Error:", e)
