# Directory: llm_rag/

# -----------------------------
# File: README.md
# -----------------------------
# LLM RAG Pipeline 🚀

A **production-grade, modular Retrieval-Augmented Generation (RAG)** system to supercharge Large Language Models (LLMs) with your private documents.

## ✨ Features
- 📄 Upload & chunk documents (.txt, .pdf, .md, .docx)
- 🤖 Generate embeddings using OpenAI or HuggingFace
- 🧠 Store & retrieve chunks from vector DB (Chroma, FAISS)
- 🧩 Chain-based RAG: retrieve relevant chunks → generate answers
- 🖥️ Clean CLI and sleek Gradio web UI for querying
- 🛠️ Fully modular & extensible Python codebase
- 🔐 API key entry via `.env` or UI textbox
- 📦 Clean project structure, logging, error handling

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Harish-coder360/llm-rag-pipeline
   cd llm-rag-pipeline
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your environment:**
   - Rename `.env.example` → `.env`
   - Add your OpenAI key or other configs

## 🚀 Run It

### 🔍 CLI Mode
```bash
python ingest.py --path ./docs  # optional, loads default dir
python main.py --query "What is retrieval-augmented generation?"
```

### 🖼️ Web UI Mode
```bash
python app.py  # launches Gradio app
```

## 🧩 Extend It
- Swap embeddings or vector DB in `config.py`
- Add file types in `app.py > process_uploaded_file()`
- Hook other LLMs or chunking logic

---

Made with 💡 by developers, for developers. Perfect for building document-aware AI assistants.
