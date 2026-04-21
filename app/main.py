import time
import logging
from fastapi import FastAPI, HTTPException
from app.models import ChatRequest, ChatResponse
from app.agent import agent

# -----------------------------
# Logging setup
# -----------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI(
    title="AI Agent API",
    description="Agent with tools + memory",
    version="1.1.0"
)

# -----------------------------
# Health check
# -----------------------------
@app.get("/")
def health():
    return {"status": "ok", "message": "Agent API running"}


# -----------------------------
# Chat endpoint
# -----------------------------
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        if not req.message.strip():
            raise ValueError("Message cannot be empty")

        logger.info(f"Incoming request: {req.message}")

        start_time = time.time()

        result = agent.invoke({"input": req.message})

        latency = (time.time() - start_time) * 1000

        logger.info(f"Response generated in {latency:.2f} ms")

        return ChatResponse(
            response=result["output"],
            latency_ms=latency
        )

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")