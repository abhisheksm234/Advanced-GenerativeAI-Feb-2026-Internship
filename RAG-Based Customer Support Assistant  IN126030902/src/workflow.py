from langgraph.graph import StateGraph
from typing import TypedDict
from src.retriever import get_retriever
from src.llm import generate_answer
from src.intent_router import detect_intent
from src.hitl import human_escalation

class State(TypedDict):
    query: str
    context: str
    answer: str
    intent: str
    confidence: float
    escalate: bool

retriever = get_retriever()

def process_node(state):
    query = state["query"]

    docs = retriever.invoke(query)
    context = "\n".join([d.page_content for d in docs])

    answer = generate_answer(context, query)
    intent = detect_intent(query)

    confidence = len(docs)

    escalate = (
        intent in ["human", "escalate"] or
        confidence < 2 or
        "I don't know" in answer
    )

    return {
        "context": context,
        "answer": answer,
        "intent": intent,
        "confidence": confidence,
        "escalate": escalate
    }

def output_node(state):
    return {"answer": state["answer"]}

def hitl_node(state):
    human_answer = human_escalation(state["query"])
    return {"answer": human_answer}

def route(state):
    if state["escalate"]:
        return "hitl"
    return "output"

def build_graph():
    graph = StateGraph(State)

    graph.add_node("process", process_node)
    graph.add_node("output", output_node)
    graph.add_node("hitl", hitl_node)

    graph.set_entry_point("process")

    graph.add_conditional_edges(
        "process",
        route,
        {
            "output": "output",
            "hitl": "hitl"
        }
    )

    return graph.compile()