# Foundry SDK in 10 Days

A simple project that uses the Azure AI Foundry SDK to generate 10 programming exercises of increasing difficulty. Complete them all at once, or tackle one a day as a **10-day challenge**.

## What It Does

`app.py` calls the Foundry SDK (via `gpt-4o`) to generate 10 themed coding exercises (difficulty 0–9) and saves each one to `exercises/exercises/`. Each exercise requires you to write Python code that uses the Foundry SDK as a tool within the solution.

The exercises follow a fun progression:

| Level | Theme |
|-------|-------|
| 0 | Generate and display a fantasy creature description |
| 1 | Create and filter a D&D character sheet |
| 2 | Generate movie reviews and count positive words |
| 3 | Build a joke collector and validator |
| 4 | Generate study flashcards and save to file |
| 5 | Create and analyze AI-generated product feedback |
| 6 | Generate weather summaries and aggregate insights |
| 7 | Simulate a news headline monitoring system |
| 8 | Build a multi-stage story generator with validation |
| 9 | Design a structured AI report processing pipeline |

Estimated time per exercise: 8–25 minutes depending on difficulty.

## Prerequisites

- Python 3.10+
- An [Azure AI Foundry](https://ai.azure.com) project with a deployed `gpt-4o` model
- Azure CLI installed and authenticated (`az login`)

## Setup

1. **Clone the repo**

   ```bash
   git clone <repo-url>
   cd FoundrySDK
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your endpoint**

   Copy the sample env file and fill in your Azure AI Foundry project endpoint:

   ```bash
   cp .env_sample .env
   ```

   Edit `.env`:

   ```
   PROJECT_ENDPOINT="https://<your-resource>.services.ai.azure.com/api/projects/<your-project>"
   ```

5. **Log in to Azure**

   ```bash
   az login
   ```

## Generate Exercises

```bash
python app.py
```

This will generate 10 exercise files (`exercise0.txt` – `exercise9.txt`) in the `exercises/exercises/` directory. There is a 30-second delay between each to avoid rate limiting (~5 minutes total).

## Complete the Exercises

Each exercise asks you to write a Python script that uses the Foundry SDK. Put your solutions in the `exercises/exerciseAnswers/` folder.

**All at once** — Work through all 10 in a single session.

**10-day challenge** — Complete one exercise per day, starting from difficulty 0 and working up to 9.

## Project Structure

```
├── app.py                          # Exercise generator script
├── requirements.txt                # Python dependencies
├── .env_sample                     # Sample environment config
├── .env                            # Your endpoint (git-ignored)
├── .gitignore
├── README.md
└── exercises/
    ├── exercises/                  # Generated exercise prompts
    │   ├── exercise0.txt
    │   ├── exercise1.txt
    │   └── ...
    └── exerciseAnswers/            # Your solutions go here
```
