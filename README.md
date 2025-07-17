# LLM RAG Pipeline

A professional, modular Retrieval-Augmented Generation (RAG) pipeline for leveraging Large Language Models (LLMs) with your own data.

## Features
- Ingest and chunk documents (code, markdown, text, etc.)
- Embed chunks using state-of-the-art embedding models
- Store embeddings in a vector database (ChromaDB by default)
- Query pipeline: User question → retrieve relevant chunks → LLM generates answer
- CLI interface for interaction
- Modular, extensible codebase
- Configurable via `.env` or YAML
- Logging and error handling

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables:**
   - Copy `.env.example` to `.env` and set your API keys (if using OpenAI or similar)

## Usage
- **Ingest your data:**
  ```bash
  python ingest.py --path /path/to/your/data
  ```
- **Ask questions:**
  ```bash
  python main.py --question "What does this repo do?"
  ```

## Extending
- Swap out embedding models or vector stores in `config.py`
- Add new data loaders in `ingest.py`

---

**Built with ❤️ for professional, production-ready RAG workflows.** 