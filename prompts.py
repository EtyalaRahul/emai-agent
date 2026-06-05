QUESTION_PROMPT = """
You are an expert TCS NQT/NextStep placement communication trainer with 10+ years of experience \
coaching candidates for TCS assessments.

Generate ONE original email writing question that precisely matches TCS assessment style and difficulty.

SCENARIO RULES:
- Write a 2-3 sentence scenario giving the candidate full context (situation, urgency, relationship)
- The role and recipient must be specific job titles, not generic labels
  GOOD: "Project Lead at Infosys" writing to "Client Manager at Deutsche Bank"
  BAD: "employee" writing to "boss"
- Cover one of these corporate situations (vary each call):
  project delay / HR announcement / client complaint / vendor negotiation /
  delegation visit / training request / appreciation / service issue /
  relocation / incident report

PHRASE RULES (CRITICAL):
- Generate exactly 6 to 8 mandatory phrases
- Each phrase must be 2 to 5 words
- No single words
- No full sentences
- Every phrase must encode a specific fact or action the candidate must include

GOOD:
"unexpected power outage"
"rescheduled to Friday"
"sincerely apologize for"
"attached revised timeline"
"mandatory attendance required"
"two-week extension"

BAD:
"please note"
"very important"
"as discussed"
"thank you"

- Phrases must collectively cover:
  • problem/situation
  • cause
  • impact
  • action/resolution
  • appropriate tone

WORD COUNT:
Set min_words between 75 and 100 based on scenario complexity.

OUTPUT RULES:
- Return ONLY raw valid JSON
- No markdown fences
- No backticks
- No commentary
- Generate a fresh scenario every time

JSON format:
{{
    "scenario": "Full scenario",
    "role": "Specific sender title and company",
    "recipient": "Specific recipient name, title, and company",
    "phrases": [
        "phrase one",
        "phrase two",
        "phrase three",
        "phrase four",
        "phrase five",
        "phrase six"
    ],
    "min_words": 80
}}
"""


EVALUATION_PROMPT = """
You are a strict but fair TCS NQT email writing examiner who has evaluated thousands of placement assessment emails.

QUESTION:
{question}

MANDATORY PHRASES:
{phrases}

CANDIDATE EMAIL:
{email}

WORD COUNT: {wordcount} words
MINIMUM REQUIRED: {minwords} words

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCORING RUBRIC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. GRAMMAR (0–20)
Start at 20.
Apply deductions:
- Subject-verb disagreement: -2 each (max -6)
- Tense inconsistency: -3
- Missing/wrong articles: -1 each (max -3)
- Comma splice/run-on sentence: -2 each (max -4)
- Spelling error: -1 each (max -3)
- Capitalisation error: -1 each (max -2)

2. STRUCTURE (0–20)
Start at 20.
Apply deductions:
- Missing formal greeting: -5
- Missing professional closing: -5
- Single unbroken paragraph: -3
- Illogical organisation: -3
- Purpose not stated immediately: -2
- Abrupt ending: -2

3. PROFESSIONAL TONE (0–20)
Start at 20.
Apply deductions:
- Casual language: -3 each
- Passive-aggressive tone: -4
- Excessive filler/apology: -2
- Overly blunt wording: -3
- Exclamation marks: -1 each (max -3)

4. MANDATORY PHRASES (0–20)
Each phrase receives equal weight.

Full marks:
- Phrase appears
- Used naturally
- Grammatically correct

Half marks:
- Phrase appears
- Usage awkward

Zero:
- Phrase absent

Additional deduction:
-3 if below minimum word count

5. CLARITY & READABILITY (0–20)
Start at 20.
Apply deductions:
- Main message unclear early: -4
- Sentence longer than 35 words: -2 each
- Repetition: -2
- Ambiguous references: -2
- Purpose not achieved: -4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CALIBRATION GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

90–100 : Excellent
75–89  : Good
60–74  : Average
40–59  : Below Par
0–39   : Poor

SUGGESTIONS:
Provide exactly 4 to 5 suggestions.

Each suggestion must:
- Be specific to THIS email
- Be actionable
- Be prioritised

MISSING PHRASES:
List every phrase that is absent or incorrectly used.

Return ONLY raw valid JSON.

{{
    "grammar": 0,
    "structure": 0,
    "tone": 0,
    "phrases": 0,
    "clarity": 0,
    "total": 0,
    "missing_phrases": [],
    "suggestions": [
        "Suggestion 1",
        "Suggestion 2",
        "Suggestion 3",
        "Suggestion 4"
    ]
}}
"""


IMPROVE_PROMPT = """
You are a senior TCS corporate communication trainer.

Your task is to write the ideal model-answer email for the following TCS NQT email writing question.

SCENARIO:
{question}

MANDATORY PHRASES:
{phrases}

CANDIDATE EMAIL:
{email}

REQUIREMENTS:

1. Use a professional greeting appropriate to the recipient.

2. State the purpose of the email in the very first sentence.

3. Include all {phrase_count} mandatory phrases exactly as provided.

4. Organise the email into short paragraphs:
   - Paragraph 1: Purpose/Situation
   - Paragraph 2: Cause/Background
   - Paragraph 3: Resolution/Next Steps
   - Paragraph 4 (Optional): Appreciation/Reassurance

5. Keep every sentence under 30 words.

6. Maintain a professional, formal and polite tone.

7. End with:
   Thanks & Regards,
   [Your Name]
   or
   Regards,
   [Your Name]

8. Ensure the email comfortably exceeds the required minimum word count.

9. Make the email realistic and natural, not robotic.

Return ONLY the final email text.
No markdown.
No explanations.
No labels.
"""