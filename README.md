# Multimodal RAG

A Python project for exploring multimodal retrieval-augmented generation (RAG). The goal is to build a system that can retrieve relevant information from more than one type of content and use that context to help answer user questions.

> **Project status:** Initial setup. The application code, data sources, and model/provider integrations have not been added yet.

## Requirements

- [uv](https://docs.astral.sh/uv/)
- Python 3.12

## Set up the environment

Run these commands from the project directory.

1. List Python installations that uv can find:

   ```cmd
   uv python list
   ```

2. Create a virtual environment named `env` with Python 3.12:

   ```cmd
   uv venv env --python 3.12
   ```

3. Activate the environment in Command Prompt:

   ```cmd
   env\Scripts\activate.bat
   ```

4. Install project dependencies:

   ```cmd
   uv pip install -r requirements.txt
   ```

   Dependencies should be added to `requirements.txt` as the application is developed. The file is currently empty.

## Verify Python

With the environment activated, confirm the selected interpreter:

```cmd
python --version
```

It should report Python 3.12.x.

## Project structure

```text
multimodal-rag/
├── README.md
├── requirements.txt
└── env/                 # Local virtual environment; not committed
```

## Running the project

There is no application entry point yet. Add the source code and its run instructions here when the first runnable component is available.
