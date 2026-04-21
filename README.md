# 🤖 AI Agent System (ReAct + Memory)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![LangChain](https://img.shields.io/badge/LangChain-AI-orange)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent-red)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-black)

---

## 🔥 Overview
This project implements an AI Agent system using LangGraph and FastAPI.

The agent uses LLM-based reasoning (ReAct) to decide actions and dynamically execute tools such as calculators and text processors, while maintaining conversational context.

---

## 🏗️ Architecture

![Architecture](./assets/architecture.png)

### 🔄 Flow
User → FastAPI → LangGraph Agent → LLM Decision → Tool Execution → Response

---

## 🚀 Features

- 🧠 ReAct-based reasoning (Thought → Action → Observation)
- 🔧 Tool calling (Calculator, Word Counter)
- 💬 Conversational memory (context-aware responses)
- 🤖 LLM-powered decision making
- 🧩 Modular and extensible design

---

## 🛠 Tech Stack

- Python
- FastAPI
- LangChain
- LangGraph
- OpenAI
- Pydantic
- python-dotenv

---

## ⚙️ Setup

```bash
git clone https://github.com/your-username/ai-agent-system.git
cd ai-agent-system

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

## 📈 Learning Outcome

This project demonstrates:

* Agent architecture (ReAct pattern)
* Tool calling and decision-making
* Memory handling in LLM systems
* Real-world GenAI system design
