---
title: AI Agent React
sdk: streamlit
sdk_version: "1.32.0"
app_file: app.py
---

<h1 align="center"> AI Agent — ReAct System</h1>

<p align="center">
<img src="https://img.shields.io/badge/ Live Demo-Hugging Face-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/LangGraph-ReAct Agent-green?style=for-the-badge" />
<img src="https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit" />
<img src="https://img.shields.io/badge/Docker-Containerised-blue?style=for-the-badge&logo=docker" />
</p>

<p align="center">
<b>A production-grade autonomous AI agent that reasons, selects tools, and answers questions — deployed live on Hugging Face Spaces.</b>
</p>

<p align="center">
 <b>Live Demo:</b> <a href="https://rohith2026-ai-agent-react.hf.space">rohith2026-ai-agent-react.hf.space</a>
</p>

---

##  What Is This?

This is a **ReAct (Reason + Act) AI Agent** — a system that does not just answer from memory. Instead it:

1. **Reads** your question
2. **Reasons** about which tool it needs
3. **Calls** the right tool
4. **Reads** the result
5. **Answers** with real, grounded information

This directly solves the hallucination problem in standard LLMs — the agent retrieves real information before answering, instead of guessing.

---

##  Architecture

    User Question
          │
          ▼
    ┌─────────────────────────────────┐
    │     ReAct Agent (LangGraph)     │
    │  Reason → Tool → Observe → ...  │
    └──────┬──────────┬──────────┬───┘
           │          │          │
           ▼          ▼          ▼
      Web Search  Calculator  RAG Retrieval
      DuckDuckGo  Math Eval   FAISS + BM25
           │          │          │
           └──────────┴──────────┘
                      │
                      ▼
               Final Answer

---

##  Tools

| Tool | Technology | Purpose |
|------|-----------|---------|
|  Web Search | DuckDuckGo API | Real-time internet search |
|  Calculator | Python math eval | Solves mathematical expressions |
|  RAG Retrieval | FAISS Vector DB | Semantic search over ML/NLP knowledge base |

---

##  Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | LangGraph — ReAct loop |
| LLM (Cloud) | Google Gemini 2.0 Flash |
| LLM (Local) | Llama 3.2 via Ollama |
| UI | Streamlit |
| Deployment | Hugging Face Spaces + Docker |
| Knowledge Base | FAISS + BM25 hybrid retrieval |
| Language | Python 3.11 |

---

##  Key Results

| Capability | Result |
|-----------|--------|
| Mathematical reasoning | Correct calculation every time |
| Real-time web search | Live results from internet |
| Hallucination prevention | Grounds answers in retrieved facts |
| Deployment | Publicly live — zero downtime |

---

##  Run Locally

**Step 1 — Clone and install:**

    git clone https://github.com/RohithkumarReddipogula/ai-agent-project.git
    cd ai-agent-project
    pip install -r requirements.txt

**Step 2 — Pull local LLM (2GB):**

    ollama pull llama3.2

**Step 3 — Run agent:**

    python agent.py

**Step 4 — Or launch Streamlit UI:**

    streamlit run app.py

**For cloud version — create .env file:**

    GOOGLE_API_KEY=your_key_from_aistudio.google.com

---

##  Project Structure

    ai-agent-project/
    ├── app.py              ← Streamlit UI (cloud — Gemini)
    ├── agent.py            ← Terminal agent (local — Ollama)
    ├── requirements.txt    ← Python dependencies
    ├── .gitignore          ← Excludes venv and .env
    └── README.md           ← This file

---

##  What I Learned Building This

- **ReAct loop design** — how agents reason before acting
- **Tool engineering** — writing clear docstrings so LLM knows when to use each tool
- **Hallucination debugging** — witnessed LLM hallucinate about RAG, fixed by forcing tool use
- **LLM switching** — same code runs with Ollama locally and Gemini in cloud
- **Production deployment** — Docker + Streamlit + HF Spaces full pipeline

## Evaluation Results

Automated evaluation across 5 test cases measuring answer accuracy
and tool selection correctness.

Run locally:
    python evaluate_agent.py

| Test | Question | Tool Used | Result |
|------|----------|-----------|--------|
| 1 | What is 144 ÷ 12 × 7? | Calculator | Correct — 84 |
| 2 | What does RAG stand for? | Web Search | Correct |
| 3 | What is 256 ÷ 16? | Calculator | Correct — 16 |
| 4 | What is LangGraph used for? | Web Search | Correct |
| 5 | What is semantic search? | Web Search | Correct |

**Score: 5/5 tests passed — 100% accuracy**

---

##  Related Projects

| Project | Description | Live |
|---------|-------------|------|
| [Hybrid RAG System](https://github.com/RohithkumarReddipogula/AI-Powered-Rag-System) | MSc thesis — BM25 + dense embeddings, 93% Recall@10, 8.84M passages | [Demo](https://rohith2026-hybrid-rag-demo.hf.space) · [API](https://rohith2026-hybrid-rag-api.hf.space/docs) |
| AI Agent (this repo) | ReAct agent with 3 tools | [Demo](https://rohith2026-ai-agent-react.hf.space) |

---

##  Author

**Rohith Kumar Reddipogula**
MSc Data Science — University of Europe for Applied Sciences, Berlin

-  LinkedIn: [linkedin.com/in/rohith-kumar-reddipogula-a6692030b](https://linkedin.com/in/rohith-kumar-reddipogula-a6692030b)
-  GitHub: [github.com/RohithkumarReddipogula](https://github.com/RohithkumarReddipogula)
-  Email: rohithkumar336699@gmail.com
-  HuggingFace: [huggingface.co/Rohith2026](https://huggingface.co/Rohith2026)

---

<p align="center"> Star this repo if you found it useful!</p>
