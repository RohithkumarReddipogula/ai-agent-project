import os
import math
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent

load_dotenv()

st.set_page_config(
    page_title="Rohith's AI Agent",
    page_icon=" ",
    layout="centered"
)

st.title("AI Agent — ReAct System")
st.markdown("**Built by Rohith Kumar Reddipogula** | LangGraph + Gemini + 3 Tools")
st.markdown("---")

# ── LLM ──────────────────────────────────────────────────────────────────────
@st.cache_resource
def load_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.environ.get("GOOGLE_API_KEY"),
        temperature=0
    )

    search = DuckDuckGoSearchRun()

    @tool
    def web_search(query: str) -> str:
        """Search the internet for current information about any topic."""
        return search.run(query)

    @tool
    def calculator(expression: str) -> str:
        """Evaluate a mathematical expression. Examples: '2 + 2', 'sqrt(16)'"""
        try:
            allowed = {k: v for k, v in math.__dict__.items()
                      if not k.startswith("_")}
            result = eval(expression, {"__builtins__": {}}, allowed)
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"

    @tool
    def rag_retrieval(query: str) -> str:
        """Search knowledge base about ML, NLP, and RAG systems."""
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

    tools = [web_search, calculator, rag_retrieval]
    agent = create_react_agent(llm, tools)
    return agent

# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown("### Ask me anything")
st.markdown("The agent will decide which tool to use:  Web Search ·  Calculator ·  RAG Retrieval")

with st.expander(" Example questions to try"):
    st.markdown("""
    - `What is 144 divided by 12 then multiplied by 7?`
    - `What is Retrieval Augmented Generation?`
    - `What are the latest AI developments in 2026?`
    - `Search for information about LangGraph`
    """)

question = st.text_input("Your question:", placeholder="Type your question here...")

if st.button("Ask Agent ", type="primary") and question:
    with st.spinner("Agent is thinking..."):
        try:
            agent = load_agent()
            response = agent.invoke({
                "messages": [{"role": "user", "content": question}]
            })
            answer = response["messages"][-1].content

            st.markdown("### Answer")
            st.success(answer)

        except Exception as e:
            st.error(f"Error: {str(e)}")

st.markdown("---")
st.markdown("Stack: Python · LangChain · LangGraph · Google Gemini · DuckDuckGo · FAISS RAG")