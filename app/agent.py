from langchain_openai import ChatOpenAI
from langchain.agents import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

# -----------------------------
# LLM (Brain of system)
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
        description="Use this to count number of words in a sentence"
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
# PROMPT (ReAct template)
# -----------------------------
prompt = hub.pull("hwchase17/react")

# -----------------------------
# AGENT (reasoning engine)
# -----------------------------
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# -----------------------------
# EXECUTOR (runtime engine)
# -----------------------------
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=False
)

# -----------------------------
# OPTIONAL: Local testing
# -----------------------------
if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = agent_executor.invoke({"input": user_input})
        print("Agent:", response["output"])