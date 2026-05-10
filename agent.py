import os
import math
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent

load_dotenv()

# ── LLM — runs on your laptop, no API key needed ──────────────────────────────
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

# ── TOOL 1: Web Search ────────────────────────────────────────────────────────
search = DuckDuckGoSearchRun()

@tool
def web_search(query: str) -> str:
    """Search the internet for current information about any topic."""
    return search.run(query)

# ── TOOL 2: Calculator ────────────────────────────────────────────────────────
@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression.
    Examples: '2 + 2', '10 * 5', 'sqrt(16)'
    """
    try:
        allowed = {k: v for k, v in math.__dict__.items()
                   if not k.startswith("_")}
        result = eval(expression, {"__builtins__": {}}, allowed)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# ── TOOL 3: RAG Retrieval ─────────────────────────────────────────────────────
@tool
def rag_retrieval(query: str) -> str:
    """Search a knowledge base about ML, NLP, and RAG systems."""
    import requests
    try:
        response = requests.post(
            "https://rohith2026-hybrid-rag-api.hf.space/search",
            json={"query": query, "top_k": 3},
            timeout=15
        )
        if response.status_code == 200:
            return str(response.json())
        return f"Status {response.status_code}"
    except Exception as e:
        return f"RAG unavailable: {str(e)}"

# ── BUILD AGENT ───────────────────────────────────────────────────────────────
tools = [web_search, calculator, rag_retrieval]
agent = create_react_agent(llm, tools)

# ── RUN AGENT ─────────────────────────────────────────────────────────────────
def run_agent(question: str) -> str:
    print(f"\n{'='*60}")
    print(f"Question: {question}")
    print(f"{'='*60}\n")
    response = agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    final = response["messages"][-1].content
    print(f"Answer: {final}\n")
    return final

# ── TEST ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    run_agent("Use the web_search tool to find what RAG Retrieval Augmented Generation means and summarise it")