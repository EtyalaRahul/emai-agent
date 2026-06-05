from typing import TypedDict, Optional, Dict, Any
from langgraph.graph import StateGraph
from langgraph.graph import END

from nodes import (
    generate_question,
    evaluate_email,
    improve_email
)


class EmailState(TypedDict, total=False):

    api_key: str

    action: str

    question: Dict[str, Any]

    email: str

    evaluation: Dict[str, Any]

    improved_email: str


# -----------------------------
# Router
# -----------------------------

def route_action(state: EmailState):

    action = state.get("action")

    if action == "generate":
        return "question_generator"

    if action == "evaluate":
        return "email_evaluator"

    return "question_generator"


# -----------------------------
# Build Graph
# -----------------------------

builder = StateGraph(
    EmailState
)

# Nodes

builder.add_node(
    "question_generator",
    generate_question
)

builder.add_node(
    "email_evaluator",
    evaluate_email
)

builder.add_node(
    "email_improver",
    improve_email
)

# Entry

builder.set_conditional_entry_point(
    route_action,
    {
        "question_generator":
            "question_generator",

        "email_evaluator":
            "email_evaluator"
    }
)

# Question Flow

builder.add_edge(
    "question_generator",
    END
)

# Evaluation Flow

builder.add_edge(
    "email_evaluator",
    "email_improver"
)

builder.add_edge(
    "email_improver",
    END
)

# Compile

graph = builder.compile()