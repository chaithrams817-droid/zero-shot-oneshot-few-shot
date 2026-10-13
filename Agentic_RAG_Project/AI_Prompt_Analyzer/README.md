# AI Prompt Analyzer & Improver

A lightweight Streamlit app for analyzing prompts and generating improved versions of them using a local Ollama model.

## Overview

This project helps users understand how a prompt is structured and which prompting techniques it uses. It can:

- classify a prompt as zero-shot, one-shot, or few-shot prompting
- detect role-based prompting patterns
- explain the reasoning behind the classification
- rewrite the prompt to make it clearer and more effective
- generate a response from the improved prompt using a local LLM

## Features

- Prompt analysis with lightweight heuristic detection
- Role prompting and example pattern detection
- Improved prompt generation using a local model
- Side-by-side comparison of original vs. improved outputs
- Easy browser-based UI using Streamlit

## Project Structure

```text
AI_Prompt_Analyzer/
├── app.py                 # Streamlit application entry point
├── prompt_analyzer.py     # Detects prompting techniques in the user's prompt
├── prompt_improver.py     # Generates improved prompts and model responses
├── test_analyzer.py       # Basic prompt analysis checks
├── test_improver.py       # Basic prompt improvement smoke test
├── .venv                  # Local Python virtual environment
└── README.md             # Project documentation
```

## Requirements

Before running the project, make sure you have:

- Python 3.10+
- Streamlit
- Ollama installed and running locally
- The model `qwen3:1.7b` pulled in Ollama

## Setup

1. Open a terminal in the project folder.
2. Activate the project environment if you are using the included `.venv`:

```bash
.venv\Scripts\activate
```

3. Install the required Python packages:

```bash
pip install streamlit ollama
```

4. Make sure Ollama is installed and running. Then pull the required model:

```bash
ollama pull qwen3:1.7b
```

## Run the App

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (typically `http://localhost:8501`).

## How It Works

1. Enter a prompt in the app.
2. The app analyzes it using `prompt_analyzer.py`.
3. The app generates the original response using the configured Ollama model.
4. You can review the analysis and click the improve button.
5. The app rewrites the prompt and generates a new response for comparison.

## Notes

- The prompt analysis is heuristic-based and focuses on common prompting patterns.
- The app depends on a local Ollama service for model inference.
- If the model is unavailable or Ollama is not running, the app will display an error message instead of generating output.

## License

This project does not currently declare a license. Add one if you plan to share or distribute the code publicly.
