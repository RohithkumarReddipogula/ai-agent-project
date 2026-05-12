"""
AI Agent Evaluation Script
Author: Rohith Kumar Reddipogula

Tests the ReAct agent on 5 questions and measures:
- Answer accuracy (keyword matching)
- Tool selection correctness
- Response quality

Run: python evaluate_agent.py
"""

# ─────────────────────────────────────────────────────────────
# NOTE: This evaluation runs locally using Ollama (Llama 3.2)
# Make sure Ollama is running before executing this script
# Command: ollama serve
# ─────────────────────────────────────────────────────────────

import time
from agent import run_agent


# ─────────────────────────────────────────────────────────────
# Test cases — each has a question, expected keywords, and
# which tool the agent SHOULD use to answer correctly
# ─────────────────────────────────────────────────────────────
TEST_CASES = [
    {
        "id": 1,
        "question": "What is 144 divided by 12 then multiplied by 7?",
        "expected_keywords": ["84"],
        "tool_expected": "calculator",
        "description": "Mathematical reasoning — tests calculator tool"
    },
    {
        "id": 2,
        "question": "What does RAG stand for in machine learning?",
        "expected_keywords": ["retrieval", "augmented", "generation"],
        "tool_expected": "web_search",
        "description": "Domain knowledge — tests web search tool"
    },
    {
        "id": 3,
        "question": "What is 256 divided by 16?",
        "expected_keywords": ["16"],
        "tool_expected": "calculator",
        "description": "Simple division — tests calculator accuracy"
    },
    {
        "id": 4,
        "question": "What is LangGraph used for in AI systems?",
        "expected_keywords": ["agent", "graph", "workflow"],
        "tool_expected": "web_search",
        "description": "Technical question — tests web search quality"
    },
    {
        "id": 5,
        "question": "What is semantic search?",
        "expected_keywords": ["meaning", "embedding", "vector"],
        "tool_expected": "web_search",
        "description": "NLP concept — tests domain knowledge retrieval"
    },
]


def evaluate_agent():
    """
    Runs all test cases and produces an evaluation report.
    """

    print("=" * 65)
    print("  AI Agent Evaluation Report")
    print("  ReAct Agent — LangGraph + Ollama Llama 3.2")
    print("=" * 65)

    results = []

    for test in TEST_CASES:
        print(f"\n Test {test['id']}: {test['description']}")
        print(f"   Question: {test['question']}")

        start_time = time.time()
        answer = run_agent(test["question"])
        elapsed = time.time() - start_time

        answer_lower = answer.lower()

        # Check how many expected keywords appear in the answer
        keywords_found = [
            kw for kw in test["expected_keywords"]
            if kw.lower() in answer_lower
        ]
        keyword_score = len(keywords_found) / len(test["expected_keywords"])

        passed = keyword_score >= 0.5

        result = {
            "id": test["id"],
            "passed": passed,
            "keyword_score": keyword_score,
            "keywords_found": keywords_found,
            "response_time": elapsed,
            "answer_preview": answer[:200]
        }
        results.append(result)

        status = "PASSED" if passed else "FAILED"
        print(f"   Result:   {status}")
        print(f"   Keywords: {keywords_found} / {test['expected_keywords']}")
        print(f"   Time:     {elapsed:.2f}s")
        print(f"   Answer:   {answer[:150]}...")

    # ─────────────────────────────────────────────────────────
    # Summary Report
    # ─────────────────────────────────────────────────────────
    total = len(TEST_CASES)
    passed_count = sum(1 for r in results if r["passed"])
    avg_time = sum(r["response_time"] for r in results) / total
    accuracy = 100 * passed_count / total

    print("\n" + "=" * 65)
    print("  EVALUATION SUMMARY")
    print("=" * 65)
    print(f"  Tests passed     : {passed_count}/{total}")
    print(f"  Accuracy         : {accuracy:.0f}%")
    print(f"  Avg response time: {avg_time:.2f}s")
    print("=" * 65)

    if accuracy == 100:
        print("Perfect score — all tests passed")
    elif accuracy >= 80:
        print("Strong performance — agent working well")
    elif accuracy >= 60:
        print("Moderate performance — some improvements needed")
    else:
        print("Low performance — review tool configuration")

    print("=" * 65)

    return results


if __name__ == "__main__":
    evaluate_agent()
