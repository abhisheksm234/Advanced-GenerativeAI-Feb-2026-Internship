# 🚀 RAG-Based Customer Support Assistant (LangGraph + HITL)

## 📌 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** based Customer Support Assistant that answers user queries using a PDF knowledge base.  
It combines **semantic retrieval** with a **locally hosted LLM** to generate accurate, context-aware responses while minimizing hallucination.

The system also includes a **Human-in-the-Loop (HITL)** mechanism to handle low-confidence or complex queries.

---

## 🎯 Problem Statement
Traditional chatbots often generate incorrect or hallucinated responses because they rely only on pre-trained knowledge.

This project solves that by:
- Retrieving relevant information from a document
- Grounding responses in real data
- Escalating to humans when needed

---

## 🧠 Key Features

- 📄 PDF ingestion and processing  
- ✂️ Intelligent chunking (500 tokens, overlap 50)  
- 🔍 Semantic search using embeddings  
- 🗄️ Vector database using ChromaDB  
- 🤖 Context-aware response generation  
- 🔁 Graph-based workflow using LangGraph  
- 🎯 Intent-based routing  
- 🧍 Human-in-the-Loop (HITL) escalation  
- 💻 Fully local setup (no paid APIs)  

---

## 🏗️ System Architecture


User
↓
UI (CLI / Streamlit)
↓
LangGraph Workflow
↓
Retriever → ChromaDB
↓
LLM (Ollama - LLaMA 3)
↓
Decision Layer (Intent + Confidence)
↓
→ Output OR HITL


---

## 🔄 End-to-End Workflow

1. PDF is loaded and split into chunks  
2. Chunks are converted into embeddings  
3. Embeddings are stored in ChromaDB  
4. User submits a query  
5. Relevant chunks are retrieved  
6. Context + query sent to LLM  
7. Response generated  
8. If low confidence → HITL triggered  

---

## 🛠️ Tech Stack

- **LangChain** – RAG pipeline  
- **LangGraph** – Workflow orchestration  
- **ChromaDB** – Vector database  
- **Ollama (LLaMA 3)** – Local LLM  
- **Sentence Transformers** – Embeddings  
- **Streamlit** – UI (optional)  
- **PyPDF** – PDF processing  

---

## 📂 Project Structure

```
rag-customer-support/
│
├── data/
│ └── knowledge_base.pdf
│
├── src/
│ ├── ingestion.py
│ ├── retriever.py
│ ├── llm.py
│ ├── intent_router.py
│ ├── hitl.py
│ ├── workflow.py
│ └── main.py
│
├── app.py
├── requirements.txt
├── README.md

```
---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/rag-customer-support.git
cd rag-customer-support
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Install Ollama & Pull Model
```
Download Ollama: https://ollama.com
```
ollama pull llama3
```
▶️ Running the Project

Run CLI version:
python -m src.main
Run Web UI (Streamlit):
```
streamlit run app.py
```

🧪 Sample Queries

Try these:
```
What is grievance redressal?
How can customers contact support?
Explain customer service policy
HITL Test:
What is refund policy?
## ⚠️ Important Notes
Do not upload .env or chroma_db/ to GitHub
Ensure Ollama is running before execution
Use clean, text-based PDFs for best results
```
## 🧠 Key Learnings
Designing end-to-end RAG systems
Reducing hallucination using retrieval
Workflow orchestration with LangGraph
Implementing decision-based AI systems
Integrating Human-in-the-Loop for reliability

## 🚀 Future Enhancements
Multi-document support
Chat history / memory
Feedback-based learning
Deployment (cloud/web app)
Advanced intent classification