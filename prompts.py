QUESTION_PROMPT = """
You are an expert TCS placement communication assessment creator.

Generate a NEW email writing question.

Rules:
1. Similar difficulty to TCS communication assessments.
2. Create realistic corporate scenarios.
3. Generate 5 to 8 mandatory phrases.
4. Minimum words should be between 70 and 120.
5. Return ONLY valid JSON.
6. Do not wrap JSON inside markdown.
7. Do not provide explanations.

Format:

{{
    "scenario": "Detailed email writing scenario",
    "role": "Sender role",
    "recipient": "Recipient role",
    "phrases": [
        "phrase1",
        "phrase2",
        "phrase3",
        "phrase4",
        "phrase5"
    ],
    "min_words": 75
}}
"""


EVALUATION_PROMPT = """
You are a strict TCS communication assessment evaluator.

Question:
{question}

Mandatory Phrases:
{phrases}

Candidate Email:
{email}

Evaluate the email on:

1. Grammar (0-20)
2. Structure (0-20)
3. Professional Tone (0-20)
4. Mandatory Phrase Usage (0-20)
5. Clarity and Readability (0-20)

Check:
- Greeting
- Body
- Closing
- Professional language
- Grammar mistakes
- Missing mandatory phrases
- Word count adequacy

Return ONLY valid JSON.

Format:

{{
    "grammar": 18,
    "structure": 19,
    "tone": 17,
    "phrases": 16,
    "clarity": 18,
    "total": 88,
    "missing_phrases": [
        "phrase1"
    ],
    "suggestions": [
        "Improve closing statement",
        "Use more professional wording"
    ]
}}
"""


IMPROVE_PROMPT = """
You are a senior corporate communication expert.

Question:
{question}

Candidate Email:
{email}

Requirements:

1. Rewrite the email professionally.
2. Ensure all mandatory phrases are naturally included.
3. Improve grammar.
4. Improve structure.
5. Improve tone.
6. Keep the email concise and professional.

Return ONLY the improved email.
"""