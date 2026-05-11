# AI Research Paper Assistant

An AI-powered Research Paper Assistant built using Retrieval-Augmented Generation (RAG).

Users can upload research papers in PDF format and ask contextual questions about the paper. The system retrieves relevant chunks from the document using semantic search and generates answers using a Large Language Model (LLM).

---

# Features

- Upload research papers (PDF)
- Ask contextual questions
- Semantic search using embeddings
- Retrieval-Augmented Generation (RAG)
- Conversational chat interface
- Streamlit web application
- FAISS vector database
- Hugging Face LLM integration

---

# Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face Transformers
- Sentence Transformers

---

# Project Architecture

```text
PDF Upload
    ↓
PDF Loader
    ↓
Text Chunking
    ↓
Embeddings Generation
    ↓
FAISS Vector Store
    ↓
Retriever
    ↓
LLM
    ↓
Answer Generation

#Folder Structure

research-paper-assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│
├── vectorstore/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm_model.py
│   └── qa_chain.py

Usage
Upload a research paper PDF.
Wait for processing.
Ask questions related to the paper.
Receive contextual answers generated using RAG.
Example Questions
What problem does this paper solve?
Explain the methodology in simple terms.
What are the limitations of this paper?
Summarize the conclusion.
What datasets were used?
Models Used
Embedding Model
sentence-transformers/all-MiniLM-L6-v2
LLM
#google/flan-t5-small
Future Improvements
Multi-PDF support
Chat memory
Paper summarization
Citation generation
PDF highlighting
Conversational RAG
LangGraph integration
Better open-source LLMs
Deployment

The application is deployed using Streamlit Community Cloud.

#Learning Outcomes

#This project demonstrates practical understanding of:

RAG pipelines
Vector databases
Embeddings
Semantic retrieval
LLM integration
Streamlit deployment
LangChain workflows
#uthor

Basava Kiran Lakshmi Venkata Swaminaidu

B.Tech CSE Student
link:  https://ai-research-paper-assistantbykiran.streamlit.app/
