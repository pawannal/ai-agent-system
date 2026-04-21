from typing import TypedDict
from langgraph.graph import StateGraph, START
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import logging
import ast
import operator

# -----------------------------
# Setup
# -----------------------------
load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------------
# LLM (with retry)
# -----------------------------
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_retries=2
)

# -----------------------------
# STATE
# -----------------------------
class AgentState(TypedDict):
    input: str
    output: str
    decision: str


# -----------------------------
# SAFE CALCULATOR (NO eval)
# -----------------------------
allowed_ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def safe_calculate(expr):
    def eval_node(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return allowed_ops[type(node.op)](
                eval_node(node.left),
                eval_node(node.right)
            )
        else:
            raise ValueError("Unsupported expression")

    tree = ast.parse(expr, mode="eval")
    return eval_node(tree.body)


def calculator(state: AgentState):
    try:
        result = safe_calculate(state["input"])
        return {"output": str(result)}
    except Exception as e:
        logger.error(f"Calculator error: {e}")
        return {"output": "Error in calculation"}


def word_counter(state: AgentState):
    words = state["input"].split()
    return {"output": f"Word count is {len(words)}"}


# -----------------------------
# LLM DECISION (STRICT)
# -----------------------------
def decide_tool(state: AgentState):
    prompt = f"""
You are a strict decision system.

Choose ONLY ONE:
- calculator
- word_counter

Rules:
- Use calculator for math
- Use word_counter for text

Return ONLY one word.

Input: {state["input"]}
"""

    try:
        response = llm.invoke(prompt).content.strip().lower()

        # Validation
        if response not in ["calculator", "word_counter"]:
            logger.warning(f"Invalid LLM output: {response}")
            response = "word_counter"

        return {"decision": response}

    except Exception as e:
        logger.error(f"LLM error: {e}")
        return {"decision": "word_counter"}  # fallback


# -----------------------------
# ROUTER
# -----------------------------
def route(state: AgentState):
    return state["decision"]


# -----------------------------
# BUILD GRAPH
# -----------------------------
builder = StateGraph(AgentState)

builder.add_node("decide", decide_tool)
builder.add_node("calculator", calculator)
builder.add_node("word_counter", word_counter)

builder.add_edge(START, "decide")

builder.add_conditional_edges(
    "decide",
    route,
    {
        "calculator": "calculator",
        "word_counter": "word_counter"
    }
)

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