# 🚀 Enterprise Applied AI Portfolio (RAG & Profile Auditor)

This repository contains two production-ready Generative AI applications built with **Python, Streamlit, ChromaDB, and Google Gemini SDK**.

## 📌 Projects Included

### 1. 🧠 Enterprise RAG Document Intelligence System (`rag_app.py`)
- **Overview:** A zero-hallucination Retrieval-Augmented Generation (RAG) assistant that allows users to upload enterprise PDFs and ask context-grounded questions.
- **Tech Stack:** Python, ChromaDB (Vector Storage), `pypdf` (Sliding-Window Chunking), Google GenAI (`gemini-3.5-flash` with multi-model fallback routing), Streamlit.

### 2. 🎯 Enterprise AI Profile Auditor & Match Engine (`app.py`)
- **Overview:** Evaluates candidate resumes against target job roles in real time using high-speed token streaming and structured system prompts.
- **Tech Stack:** Python, Google GenAI Streaming SDK, `pypdf`, Streamlit Custom Dark UI.

## ⚙️ How to Run Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Add your `GEMINI_API_KEY` inside a `.env` file.
3. Run the RAG App: `python -m streamlit run rag_app.py`
