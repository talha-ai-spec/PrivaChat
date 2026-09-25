<div align="center">

# 🔒 PrivaChat — Private Local AI Chatbot

**A sleek, privacy-focused conversational web application powered by Streamlit and Ollama. Run powerful LLMs entirely offline on your local machine with real-time streaming.**

[![Python Version](https://img.shields.io/badge/Python-3.13%2B-blue.svg?logo=python&logoColor=white)](#prerequisites)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.64%2B-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20Engine-black.svg?logo=ollama&logoColor=white)](https://ollama.com/)
[![Privacy](https://img.shields.io/badge/Privacy-100%25%20Offline-success.svg)](#-key-features)
[![Package Manager](https://img.shields.io/badge/Managed%20by-uv-DE5FE9.svg?logo=astral&logoColor=white)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Features](#-features) • [Quick Start](#-quick-start) • [Supported Models](#-supported-models) • [Project Structure](#-project-structure) • [Troubleshooting](#-troubleshooting)

---

</div>

## 🌟 Overview

**PrivaChat** delivers a ChatGPT-like desktop experience without sending a single byte of your data to cloud servers. By pairing **Streamlit**'s rapid UI rendering with **Ollama**'s high-performance local inference runtime, PrivaChat lets you chat with cutting-edge open-source models (such as Llama 3, Gemma, Mistral, and DeepSeek) securely, offline, and with real-time token streaming.

---

## 🚀 Features

- 🔒 **100% Local & Private**: No cloud API keys, no tracking, and no external data transfers. Everything runs entirely on your hardware.
- ⚡ **Real-Time Token Streaming**: Watch responses generate word-by-word with dynamic markdown rendering and cursor effects.
- 🔄 **Dynamic Model Auto-Discovery**: Automatically queries your local Ollama daemon for installed models and populates an interactive dropdown.
- 💬 **Session Context & History**: Maintains conversation memory across turns with the option to reset history anytime via the sidebar.
- 🎨 **Minimal & Modern UI**: Built with Streamlit's native chat components (`st.chat_message`, `st.chat_input`) for an intuitive interface.
- 📦 **Fast Dependency Management**: Configured with `uv` for instant reproducible environment setups.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **[Streamlit](https://streamlit.io/)** | Reactive web frontend and conversation UI |
| **[Ollama](https://ollama.com/)** | Local LLM inference engine and model runner |
| **[Python 3.13+](https://www.python.org/)** | Application core runtime |
| **[uv](https://github.com/astral-sh/uv)** | Next-generation Python package installer |

---

## 🏁 Quick Start

### 1. Prerequisites

1. **Install Ollama**: Download and run Ollama from [ollama.com](https://ollama.com/).
2. **Download at least one LLM**:
   ```bash
   # Lightweight model (great for laptops and standard CPUs)
   ollama pull gemma3:1b

   # Popular general-purpose models
   ollama pull llama3
   ollama pull mistral
   ```

### 2. Installation

Clone this repository and set up your virtual environment:

```bash
# Clone the repository
git clone https://github.com/talha-ai-spec/PrivaChat.git
cd PrivaChat

# Install dependencies using uv (recommended)
uv sync

# Or install using standard pip
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate
pip install -e .
```

### 3. Launching the App

Ensure your Ollama service is running, then launch PrivaChat:

```bash
# Using uv:
uv run streamlit run app.py

# Or within activated virtualenv:
streamlit run app.py
```

The app will automatically launch in your default web browser at `http://localhost:8501`.

---

## 🧠 Supported Models

PrivaChat dynamically detects any model pulled to your Ollama runtime. Recommended models include:

| Model | Command | Best For |
|---|---|---|
| **Gemma 3 (1B)** | `ollama pull gemma3:1b` | Ultra-fast responses, low RAM/VRAM usage |
| **Llama 3 (8B)** | `ollama pull llama3` | General chat, problem-solving, and reasoning |
| **Mistral (7B)** | `ollama pull mistral` | Creative writing, structured outputs |
| **DeepSeek R1** | `ollama pull deepseek-r1:8b` | Advanced step-by-step reasoning and logic |
| **Qwen 2.5 Coder** | `ollama pull qwen2.5-coder:7b` | Code generation and debugging |

---

## 📁 Project Structure

```
PrivaChat/
├── .gitignore            # Git exclusion patterns
├── .python-version       # Python version specification (3.13)
├── LICENSE               # MIT License
├── app.py                # Main Streamlit application and Ollama streaming logic
├── pyproject.toml        # Project dependencies and configuration
├── README.md             # Project documentation
├── uv.lock               # Dependency lockfile
└── src/
    └── privachat/
        └── __init__.py   # Package initialization
```

---

## 🔧 Troubleshooting

<details>
<summary><b>1. "Choose a model" dropdown is empty or defaults to fallback</b></summary>

- Make sure Ollama is actively running in the background. You can verify by opening a terminal and running `ollama list`.
- If you haven't pulled any models yet, run `ollama pull gemma3:1b` and refresh the browser page.
</details>

<details>
<summary><b>2. Connection Error: Failed to connect to Ollama</b></summary>

- Verify that the Ollama local daemon is running at `http://localhost:11434`.
- On Windows, verify that the Ollama icon is visible in your system tray.
</details>

---

## 👤 Author

- **Talha Adnan** — [@talha-ai-spec](https://github.com/talha-ai-spec)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
