from typing import TypedDict
from langgraph.graph import StateGraph, START

# -----------------------------
# STATE (data flowing)
# -----------------------------
class AgentState(TypedDict):
    input: str
    output: str


# -----------------------------
# TOOLS
# -----------------------------
def calculator(state: AgentState):
    try:
        result = eval(state["input"])
        return {"output": str(result)}
    except:
        return {"output": "Error in calculation"}


def word_counter(state: AgentState):
    words = state["input"].split()
    return {"output": f"Word count is {len(words)}"}


# -----------------------------
# DECISION NODE
# -----------------------------
def decide_tool(state: AgentState):
    text = state["input"]

    if any(char.isdigit() for char in text):
        return "calculator"
    else:
        return "word_counter"


# -----------------------------
# BUILD GRAPH
# -----------------------------
builder = StateGraph(AgentState)

# Add nodes
builder.add_node("calculator", calculator)
builder.add_node("word_counter", word_counter)

# Add conditional edge from START
builder.add_conditional_edges(
    START,
    decide_tool,
    {
        "calculator": "calculator",
        "word_counter": "word_counter"
    }
)

# Compile graph
graph = builder.compile()


# -----------------------------
# TEST
# -----------------------------
if __name__ == "__main__":
    while True:
        user_input = input("User: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        result = graph.invoke({"input": user_input})
        print("Agent:", result["output"])