from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Define a tool
@tool
def calculator(a: int, b: int) -> int:
    """Useful for adding two numbers."""
    return a + b

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Create agent
agent = create_agent(
    model=llm,
    tools=[calculator]
)

# Invoke agent
result = agent.invoke(
    {
        "messages": [
            HumanMessage(content="What is 5 plus 10?")
        ]
    }
)

# Print final response
print(result["messages"][-1].content)