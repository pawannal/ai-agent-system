from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory

from dotenv import load_dotenv
load_dotenv()


# -----------------------------
# LLM
# -----------------------------
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)


# -----------------------------
# TOOLS
# -----------------------------

# Calculator Tool
def calculator_tool(input_text: str):
    try:
        return str(eval(input_text))
    except:
        return "Error in calculation"


# Word Counter Tool
def word_count_tool(input_text: str):
    words = input_text.split()
    return f"Word count is {len(words)}"


# Register tools
tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Use this ONLY for mathematical calculations"
    ),
    Tool(
        name="WordCounter",
        func=word_count_tool,
        description="Useful for counting number of words in a sentence"
    )
]


# -----------------------------
# MEMORY
# -----------------------------
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)


# -----------------------------
# AGENT (ReAct + Memory)
# -----------------------------
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=False
)


# -----------------------------
# MAIN (Testing)
# -----------------------------
if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = agent.invoke({"input": user_input})
        print("Agent:", response["output"])