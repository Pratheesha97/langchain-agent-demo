import os
import getpass
from dotenv import load_dotenv, find_dotenv

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Import the tools
from agents.tools import add_numbers, subtract_numbers

# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Ensure Google API Key exists
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Provide your Google API Key: ")

def main():
    # Initialize Gemini LLM through LangChain
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.9)

    # Register tools
    tools = [add_numbers, subtract_numbers]

    # Create the agent
    agent = create_agent(llm, tools)

    print("\nLangChain Python Agent is running!")
    print("Type 'exit' to quit.\n")

    # Store chat history
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

if __name__ == "__main__":
    main()
