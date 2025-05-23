# 📨 AI Customer Email Responder

A lightweight, local web app that helps generate professional customer service replies using open-source AI models.

## ✨ Features

- Paste any customer email and generate a thoughtful reply
- Select a response tone: Friendly, Formal, or Concise
- 100% local processing with [TinyLLaMA](https://ollama.com/library/tinyllama)
- Clean and responsive UI built with Streamlit

## 🧠 Tech Stack

- **Frontend**: Streamlit
- **LLM Backend**: TinyLLaMA via [Ollama](https://ollama.com)
- **Language**: Python 3

## 🖥️ Demo Screenshot

> *(Add a screenshot of your app running at `http://localhost:8501`)*

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install streamlit
```

### 2. Install Ollama + Run Model

Download from [https://ollama.com](https://ollama.com)

```bash
ollama run tinyllama
```

### 3. Launch the App

```bash
streamlit run customer_email_responder.py
```

## ✅ Example Use Case

Paste an email like:

> *"I never received my order and it's been over 2 weeks. What gives?"*

Choose tone: `Friendly` → Receive a calm, polite, helpful reply.

## 📄 License

MIT — free to use and modify.
