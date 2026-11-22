
import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    return a * b


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

agent = create_agent(
    model=llm,
    tools=[multiply],
    system_prompt="You are a helpful AI assistant. Use tools when appropriate."
)


def get_response(query: str):
    result = agent.invoke({
        "messages": [{"role": "user", "content": query}]
    })

    return result["messages"][-1].content


if __name__ == "__main__":
    response = get_response("What is 25 multiplied by 4?")
    print(response)
