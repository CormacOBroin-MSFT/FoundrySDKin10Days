import os
import time
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv

load_dotenv()

project_client = AIProjectClient(
  endpoint=os.getenv("PROJECT_ENDPOINT"),
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

0 = Level 0 — Generate and Display a Fantasy Creature Description using Microsoft Foundry SDK  
    (Call Foundry to generate a short creature description and print it cleanly to the console.)

1 = Level 1 — Create and Filter a Dungeons & Dragons Character Sheet using Microsoft Foundry SDK  
    (Generate a simple character profile and filter out specific attributes before displaying it.)

2 = Level 2 — Generate Short Movie Reviews and Count Positive Words using Microsoft Foundry SDK  
    (Request multiple short reviews and count how often positive words appear.)

3 = Level 3 — Build a Simple Joke Collector and Validator using Microsoft Foundry SDK  
    (Generate several jokes, discard ones that exceed a length limit, and organize the rest.)

4 = Level 4 — Generate Study Flashcards and Save Them to a File using Microsoft Foundry SDK  
    (Create structured Q&A pairs and write them to disk after validating format.)

5 = Level 5 — Create and Analyze AI-Generated Product Feedback Reports using Microsoft Foundry SDK  
    (Generate structured feedback entries and compute summary statistics.)

6 = Level 6 — Generate Daily Weather Summaries and Aggregate Temperature Insights using Microsoft Foundry SDK  
    (Request multiple structured weather summaries and compute averages or trends.)

7 = Level 7 — Simulate a News Headline Monitoring System using Microsoft Foundry SDK  
    (Make multiple SDK calls for headlines, validate structure, aggregate keyword trends.)

8 = Level 8 — Build a Multi-Stage Story Generator with Structured Scene Validation using Microsoft Foundry SDK  
    (Chain multiple SDK calls to generate story parts, validate format, and maintain state.)

9 = Level 9 — Design a Structured AI Report Processing Pipeline using Microsoft Foundry SDK  
    (Generate structured multi-section reports, validate schema, retry on invalid responses, and produce a cleaned final output.)

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
    print("Exercise " + str(i) + " Generated. Sleeping for 30 seconds to avoid rate limits...")
    time.sleep(30)

  