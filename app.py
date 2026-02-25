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
You are designing short programming lab assignments that explore the capabilities available in Microsoft Foundry *and* Foundry Tools (formerly Azure AI services).

Your task is to generate EXACTLY ONE programming-focused coding exercise that uses:
- at least one Microsoft Foundry SDK call (models/agents/responses) OR
- at least one Foundry Tools SDK call (Vision, Speech, Language, Translator, Document Intelligence, Content Understanding, Content Safety),
and the response/output MUST be processed programmatically in Python.

This request is sent as part of an automated loop.

Capability track index: """ + str(i) + """
Capability track scale: 0 to 9 (inclusive).

Interpret the capability track as follows (each track is a prescriptive scenario tied to a specific Foundry / Foundry Tools capability):

0 = Track 0 — Image OCR Receipt Reader using Azure Vision (Foundry Tools)  
    (Run OCR on 1 image, extract line items/prices with string parsing, compute the total, and write a cleaned receipt summary to disk.)

1 = Track 1 — Form-to-JSON Invoice Extractor using Document Intelligence (Foundry Tools)  
    (Analyze a document, validate required fields exist, normalize currency/date formats, and output a JSON file with a strict schema.)

2 = Track 2 — Audio Transcript Cleaner using Azure Speech to Text (Foundry Tools)  
    (Transcribe a short audio clip, remove filler words, split into sentences, and produce a timestamped transcript summary.)

3 = Track 3 — Language Analytics Report using Azure AI Language (Foundry Tools)  
    (Analyze a set of short texts for key phrases/entities/sentiment, aggregate results across inputs, and print a compact report.)

4 = Track 4 — Auto-Translator + Quality Check using Azure Translator (Foundry Tools)  
    (Translate a list of phrases into a target language, detect failures/empty outputs, and write a bilingual glossary (CSV/JSON).)

5 = Track 5 — Multimodal Content Structurer using Content Understanding (Foundry Tools)  
    (Run an analyzer over a provided document/image/audio, produce structured fields, validate schema, and store a searchable index file.)

6 = Track 6 — Safety Gate for User Messages using Content Safety (Foundry Tools)  
    (Score a batch of user messages, block/allow based on thresholds, and generate a summary of flagged categories and counts.)

7 = Track 7 — Visual Caption Sorter using Foundry Models (Multimodal Model Inference)  
    (Generate captions for multiple images, rank them by a rule (keyword/length), and save a ranked list plus reasons.)

8 = Track 8 — Retrieval Grounded FAQ Builder using Foundry (Files/Retrieval + Model)  
    (Answer 3–5 questions grounded in provided text/files, log which sources were used per answer, and write a JSON Q&A pack.)

9 = Track 9 — Cross-Service Processing Pipeline using Foundry + Foundry Tools  
    (Combine at least TWO services in one pipeline, e.g., OCR → translate → safety check, with validation at each stage and a final consolidated report.)

Timebox (MUST be quick):
- Tracks 0–6: 10–20 minutes
- Tracks 7–9: 15–30 minutes

Important constraints:
- Assume the learner already knows basic Python; focus on applying SDK capabilities through programming.
- Must NOT focus on Azure configuration, authentication setup, deployment, infrastructure, or cloud architecture.
- Do NOT use Azure Bot Service or bot framework tasks.
- The SDK/service calls must be a tool within the logic, not the main subject.
- The assignment MUST require writing Python code.
- The assignment MUST require at least one SDK/service call from Foundry or Foundry Tools.
- The returned output MUST be processed programmatically (parsed, transformed, filtered, stored, aggregated, validated, and/or written to disk).
- Keep the scope small: one script or two small modules; no large frameworks.

Output format constraints:
- Do NOT provide solution code
- Do NOT provide example code
- Do NOT provide hints
- Do NOT provide step-by-step guidance
- Do NOT explain your reasoning
- Provide ONLY the following sections, in this exact order:

TITLE
OBJECTIVE
PROGRAMMING CONCEPTS PRACTICED
REQUIREMENTS
EXPECTED BEHAVIOR
CAPABILITY TRACK (0-9)

Generate exactly ONE exercise. Do not generate multiple options.
""",
)
    with open("exercises/exercises/exercise"+""+str(i)+".txt", "w") as f:
          f.write(response.output_text)
    print("Exercise " + str(i) + " Generated. Sleeping for 30 seconds to avoid rate limits...")
    time.sleep(30)

  