# Foundry SDK Exercise Generator

A simple project that uses the Azure AI Foundry SDK to generate 10 programming exercises of increasing difficulty. Complete them all at once, or tackle one a day as a **10-day challenge**.

## What It Does

`app.py` calls the Foundry SDK to generate 10 coding exercises (difficulty 0–9) and saves each one to `exercises/exercises/`. Each exercise requires you to write Python code that uses the Foundry SDK as a tool within the solution.

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
   pip install azure-ai-projects azure-identity openai
   ```

4. **Update the endpoint**

   Open `app.py` and replace the `endpoint` value with your own Azure AI Foundry project endpoint:

   ```python
   project_client = AIProjectClient(
       endpoint="https://<your-resource>.services.ai.azure.com/api/projects/<your-project>",
       credential=DefaultAzureCredential())
   ```

5. **Log in to Azure**

   ```bash
   az login
   ```

## Generate Exercises

```bash
python app.py
```

This will generate 10 exercise files (`exercise0.txt` – `exercise9.txt`) in the `exercises/exercises/` directory. There is a 20-second delay between each to avoid rate limiting.

## Complete the Exercises

Each exercise asks you to write a Python script that uses the Foundry SDK. Put your solutions in the `exercises/exerciseAnswers/` folder.

**All at once** — Work through all 10 in a single session.

**10-day challenge** — Complete one exercise per day, starting from difficulty 0 and working up to 9.

## Project Structure

```
├── app.py                          # Exercise generator script
├── requirements.txt
├── .gitignore
├── README.md
└── exercises/
    ├── exercises/                  # Generated exercise prompts
    │   ├── exercise0.txt
    │   ├── exercise1.txt
    │   └── ...
    └── exerciseAnswers/            # Your solutions go here
```
