# 🤖 AI Agent System (ReAct + Memory)

## 🚀 Live Features
- ReAct reasoning agent
- Tool calling (Calculator, WordCounter)
- Conversational memory

A production-ready AI agent built using **LangChain** with tool calling, reasoning (ReAct), and conversational memory.

---

## 🚀 Features

* 🧠 ReAct-based reasoning (Thought → Action → Observation)
* 🔧 Multi-tool support (Calculator, Word Counter)
* 💬 Conversational memory (context-aware responses)
* 🤖 LLM-powered decision making (OpenAI)
* 🧩 Modular and extensible design

---

## 🧠 Architecture

User → Agent → Tools → LLM → Response

---

## 🛠 Tech Stack

* Python
* LangChain
* OpenAI
* python-dotenv

---

## ⚙️ Setup

```bash
git clone https://github.com/your-username/ai-agent-system.git
cd ai-agent-system

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run

```bash
python app/agent.py
```

---

## 📌 Example Use Cases

* "What is 10 + 5?" → Uses calculator
* "My name is Pawan" → Stores in memory
* "What is my name?" → Retrieves from memory
* "Count words in: Gen AI is powerful" → Uses WordCounter

---

## ⚠️ Notes

* `eval()` is used for calculator (not safe for production — will be improved)
* Uses deprecated LangChain APIs (will upgrade in next iteration)

---

## 🎯 Status

✔ Multi-tool agent
✔ Memory-enabled conversational agent
🚧 Next: FastAPI integration

---

## 📈 Learning Outcome

This project demonstrates:

* Agent architecture (ReAct pattern)
* Tool calling and decision-making
* Memory handling in LLM systems
* Real-world GenAI system design
