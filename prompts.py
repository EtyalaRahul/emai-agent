QUESTION_PROMPT = """
You are an expert TCS NQT/NextStep placement communication trainer with 10+ years of experience coaching candidates for TCS assessments.

Generate ONE original email writing question that closely matches the actual TCS NQT Email Writing section.

IMPORTANT:
- Focus on communication skills, not technical knowledge.
- The candidate should be able to understand the scenario without industry-specific expertise.
- Avoid technical jargon, software architecture terms, finance terminology, engineering terminology, legal terminology, or domain-specific concepts.
- The scenario should sound like a typical workplace situation faced by employees, managers, HR teams, clients, vendors, or departments.

GOOD TCS-STYLE SCENARIOS:
- Project deadline extension
- Client complaint about delayed service
- Employee training program
- Office relocation
- Vendor delivery delay
- Appreciation for team contribution
- Meeting rescheduling
- Network or service outage
- HR policy announcement
- Incident report
- Delegation visit
- Resource request
- Leave management issue
- Customer service issue

AVOID:
- Trade Analytics module failure
- Database migration issues
- Cloud infrastructure incidents
- Reconciliation process failures
- API deployment problems
- Cybersecurity vulnerabilities
- Any highly technical scenario

SCENARIO RULES:
- Write 2-3 sentences.
- Use simple professional English.
- Clearly explain:
  1. What happened
  2. Why the email is needed
  3. What the sender wants to communicate

ROLE RULES:
- Use realistic corporate roles.

Examples:
- Project Coordinator at Infosys
- HR Executive at Wipro
- Operations Manager at TCS
- Client Relationship Executive at HCL
- Training Coordinator at Cognizant
- Administrative Officer at Accenture

RECIPIENT RULES:
- Use specific names and designations.

Examples:
- Mr. David Chen, Client Manager
- Ms. Priya Sharma, HR Director
- Mr. Rahul Mehta, Operations Head

PHRASE RULES:
- Generate exactly 6 to 8 mandatory phrases.
- Each phrase must be 2 to 5 words.
- No single words.
- No complete sentences.

GOOD:
"unexpected power outage"
"service delivery delay"
"mandatory attendance required"
"sincerely apologize for"
"attached revised schedule"
"rescheduled to Friday"
"training session scheduled"
"appreciate your cooperation"

BAD:
"please note"
"thank you"
"as discussed"
"important"

The phrases must collectively cover:
- Situation/problem
- Cause
- Impact
- Resolution/action
- Professional tone

WORD COUNT:
Set min_words between 75 and 100.

DIFFICULTY:
Match actual TCS NQT level.
The scenario should be understandable within 30 seconds by a college student.

OUTPUT RULES:
- Return ONLY valid JSON.
- No markdown.
- No explanations.
- No commentary.

JSON format:
{{
    "scenario": "Full scenario",
    "role": "Specific sender title and company",
    "recipient": "Specific recipient name, title and company",
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