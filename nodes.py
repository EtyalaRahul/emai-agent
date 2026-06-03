import json
import re

from langchain_google_genai import ChatGoogleGenerativeAI

from prompts import (
    QUESTION_PROMPT,
    EVALUATION_PROMPT,
    IMPROVE_PROMPT
)


def get_llm(api_key):
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.8
    )


def extract_json(text):
    """
    Extract JSON from Gemini response.
    """

    text = text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )

    if not match:
        raise ValueError(
            f"No JSON found.\n\nResponse:\n{text}"
        )

    return json.loads(
        match.group()
    )


def generate_question(state):

    llm = get_llm(
        state["api_key"]
    )

    response = llm.invoke(
        QUESTION_PROMPT
    )

    question = extract_json(
        response.content
    )

    return {
        "question": question
    }


def evaluate_email(state):

    llm = get_llm(
        state["api_key"]
    )

    prompt = EVALUATION_PROMPT.format(
        question=state["question"]["scenario"],
        phrases=", ".join(
            state["question"]["phrases"]
        ),
        email=state["email"]
    )

    response = llm.invoke(
        prompt
    )

    evaluation = extract_json(
        response.content
    )

    return {
        "evaluation": evaluation
    }


def improve_email(state):

    llm = get_llm(
        state["api_key"]
    )

    prompt = IMPROVE_PROMPT.format(
        question=state["question"]["scenario"],
        email=state["email"]
    )

    response = llm.invoke(
        prompt
    )

    return {
        "improved_email": response.content
    }