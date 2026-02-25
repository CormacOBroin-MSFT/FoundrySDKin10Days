import time
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_client = AIProjectClient(
  endpoint="YOUR_PROJECT_ENDPOINT",
  credential=DefaultAzureCredential())

with project_client.get_openai_client() as openai_client:
  for i in range(10):
    response = openai_client.responses.create(
    model="gpt-4o",
    input="""
You are designing short beginner programming lab assignments.

Your task is to generate EXACTLY ONE programming-focused coding exercise that uses the Microsoft Foundry SDK within the assignment.

This request is sent as part of an automated loop.

Difficulty level: """ + str(i) + """
Difficulty scale: 0 to 9 (inclusive).

Interpret the difficulty as follows:
0–2 = Intro / very beginner (basic variables, loops, conditionals, simple lists/dicts, basic string handling)
3–5 = Beginner (functions, basic file I/O, simple data structures, basic validation)
6–7 = Intermediate (modular design, structured data manipulation, error handling, aggregation, multiple SDK calls)
8–9 = Advanced (abstractions, reusable components, chaining calls, state management, response validation, retry logic)

Timebox (MUST be quick):
- Difficulty 0–5: 8–12 minutes
- Difficulty 6–7: 12–18 minutes
- Difficulty 8–9: 18–25 minutes

Important constraints:
- Focus must be on core programming concepts and code structure.
- Must NOT focus on Azure configuration, authentication setup, deployment, infrastructure, or cloud architecture.
- The Foundry SDK must be used as a tool inside the program logic, not the main subject.
- The assignment MUST require writing Python code.
- The assignment MUST require at least one Foundry SDK call.
- The Foundry response MUST be processed programmatically (e.g., parsed, transformed, filtered, stored, aggregated, validated, or written to disk).
- Keep the scope small: a single script or two small modules; no large frameworks.

Output format constraints:
- Do NOT provide solution code.
- Do NOT provide example code.
- Do NOT provide hints.
- Do NOT provide step-by-step guidance.
- Do NOT explain your reasoning.
- Provide ONLY the following sections, in this exact order:

TITLE
OBJECTIVE
PROGRAMMING CONCEPTS PRACTICED
REQUIREMENTS
EXPECTED BEHAVIOR
DIFFICULTY RATING (0-9)

Generate exactly ONE exercise. Do not generate multiple options.
""",
)
    with open("exercises/exercises/exercise"+""+str(i)+".txt", "w") as f:
          f.write(response.output_text)
    print("Exercise " + str(i) + " Generated. Sleeping for 20 seconds to avoid rate limits...")
    time.sleep(20)

  