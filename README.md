# Thoughtful AI Support Agent

A modular, CLI-based support agent for answering common questions about Thoughtful AI using semantic matching and optional OpenAI fallback.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Project Structure](#project-structure)
7. [Usage](#usage)
8. [Extending the Agent](#extending-the-agent)
9. [Logging](#logging)
10. [Contributing](#contributing)
11. [License](#license)

---

## Project Overview

The Thoughtful AI Support Agent is a simple command-line tool that answers user queries about Thoughtful AI’s services. It first tries to semantically match questions against a predefined Q&A dataset. If no confident match is found, it can optionally fall back to OpenAI’s GPT-based API.

## Features

- **Semantic Matching**: Uses sentence-transformers to embed and compare user questions against predefined ones.
- **Configurable Threshold**: Adjust similarity threshold via environment variable.
- **OpenAI Fallback**: Optionally delegates unmatched questions to an LLM (gpt-3.5-turbo).
- **Modular Design**: Clear separation of configuration, data loading, matching logic, and CLI.
- **Logging**: Records all interactions to both console and `support_agent.log`.

## Prerequisites

- Python 3.13+
- An OpenAI API key (optional, for fallback).
- `pip` for installing dependencies.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/dkasti/thoughtful-ask.git
   cd thoughtful-ai-agent
   ```

2. **Create & activate a virtual environment**:

   ```bash
   python -m venv .venv
   source venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**:

   ```bash
   poetry install --no-root
   ```

## Configuration

1. Copy the example `.env` into the project root:

   ```bash
   cp template.env .env
   ```

2. Edit `.env` and set your OpenAI API key and optional settings:

   ```ini
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. Prepare `qna.json` with your Q&A pairs. An example structure:

   ```json
   {
     "questions": [
       {
         "question": "What does the eligibility verification agent (EVA) do?",
         "answer": "EVA automates the process of verifying a patient’s eligibility..."
       },
       {
         "question": "What are the benefits of Thoughtful AI's agents?",
         "answer": "Using Thoughtful AI's Agents can significantly reduce..."
       }
     ]
   }
   ```

## Project Structure

```
├── template.env         # Sample environment variables
├── data
   ├── qna.json          # Predefined Q&A data
├── src
   ├───qna_loader.py     # Reads and validates qna.json
   ├── llm_client.py     # Wraps OpenAI calls with error handling
   ├── agent.py          # Core semantic matching and fallback logic
   ├── main.py           # CLI entrypoint
├── poetry.lock          # Python detailed dependencies for recreation
├── pyproject.toml       # Poetry based pyproject.toml dependency file
├── README.md
├── .gitignore
└── support_agent.log    # Generated at runtime
```

## Usage

Run the CLI tool:

```bash
python -m main.py
```

Example session:

```text
Welcome to Thoughtful AI Support Agent! (type 'exit' to quit)
You: how does the payment posting agent work?
Support Agent: PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.

You: Is there any benefit to using that agent?
Support Agent: Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting.
```

## Extending the Agent

- **Add Q&A pairs**: Edit `data/qna.json` and reload.
- **UI Layer**: Wrap `SupportAgent` in a web UI using Streamlit, Gradio, or Flask.

## Logging

All interactions (questions & answers) and errors are logged to `support_agent.log` with timestamps and severity levels.

## License

MIT License © Thoughtful AI
