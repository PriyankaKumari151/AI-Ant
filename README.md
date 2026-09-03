# 🚀 30-Day Production AI Engineering Roadmap

A hands-on, code-first 30-day curriculum designed to transition software engineers and computer science graduates into job-ready **AI Engineers**, **Applied ML Developers**, and **Forward Deployed Engineers**.

---

## 🎯 Purpose & Philosophy

Traditional Machine Learning courses focus heavily on theoretical math, Jupyter Notebooks, and model training from scratch. However, industry production AI engineering requires connecting state-of-the-art LLM APIs and Vector Databases to enterprise business data using robust web backends.

This repository tracks a 30-day sprint focused exclusively on **Applied AI Software Engineering**:
* **Zero Notebook Fluff:** Writing modular, production-ready Python (`.py`) scripts.
* **Schema Enforcement:** Guaranteeing deterministic, typed JSON outputs from probabilistic LLMs.
* **Scalable Backends:** Exposing AI capabilities over async REST APIs using FastAPI and Docker.
* **Retrieval-Augmented Generation (RAG):** Grounding LLMs on custom context to eliminate hallucination.

---

## 🛠 Tech Stack

| Domain | Technology |
| :--- | :--- |
| **Language & Core** | Python 3.10+, Type Hints, `asyncio`, `python-dotenv` |
| **Data Validation** | Pydantic V2 |
| **Backend & APIs** | FastAPI, Uvicorn, RESTful Standards, JSON Schema |
| **LLM Orchestration** | OpenAI API / Anthropic API, Structured Outputs |
| **Vector DB & Search** | ChromaDB, Pinecone, Embeddings, Hybrid Search |
| **Deployment & Ops** | Docker, Docker Compose, Render / Hugging Face Spaces |

---

## 📅 Day-by-Day Learning Roadmap

### Week 1: Production Python, Pydantic & FastAPI Backends
Focus on building asynchronous web APIs, managing environment secrets, and forcing LLMs to return strict JSON using Pydantic.

* **Day 1:** Environment Secrets (`python-dotenv`), Type Annotations, and `async`/`await` Concurrency.
* **Day 2:** Pydantic V2 Foundations: `BaseModel`, `Field` validation, Serialization (`model_dump_json`), and Deserialization (`model_validate_json`).
* **Day 3:** OpenAI SDK Setup: Messages Roles (`system`, `user`, `assistant`), Temperature tuning, and Token limits.
* **Day 4:** Native Structured Outputs: Converting Pydantic models to JSON Schemas (`model_json_schema()`) for guaranteed LLM output parsing.
* **Day 5:** FastAPI Fundamentals: Routes, Path/Query parameters, and Request/Response body schemas.
* **Day 6:** Robust Error Handling: HTTP status codes, validation error catching, and API middleware.
* **Day 7:** **Capstone Project 1:** *API-First Resume Structurer & Job Scorer API.*

---

### Week 2: RAG Pipelines & Vector Databases
Learn to ingest unstructured documents, generate vector embeddings, and retrieve accurate context to prevent LLM hallucinations.

* **Day 8:** Unstructured Data Ingestion: Parsing PDFs, Markdown, and text files using `PyPDF` and Python tools.
* **Day 9:** Chunking Strategies: Character vs. Token overlap vs. Semantic chunking trade-offs.
* **Day 10:** Vector Embeddings: Math behind Cosine Similarity and generating dense vectors via OpenAI Embeddings API.
* **Day 11:** Vector Databases: Setting up and querying local ChromaDB and cloud Pinecone indexes.
* **Day 12:** Vector Retrieval & Metadata Filtering: Performing hybrid searches with targeted metadata constraints.
* **Day 13:** RAG Pipeline Assembly: Combining Retrieval + Dynamic Prompt Context Insertion + LLM Generation.
* **Day 14:** **Capstone Project 2:** *Document Q&A Engine with Source Citation & Page Reference Tracking.*

---

### Week 3: Security, Containerization & Cloud Deployment
Transform local Python scripts into isolated, containerized web microservices hosted live on public endpoints.

* **Day 15:** Security & Privacy: PII/PHI masking/anonymization and prompt injection guardrails.
* **Day 16:** Docker Foundations: Writing clean `Dockerfiles`, `.dockerignore`, and building images.
* **Day 17:** Container Orchestration: Multi-container setups using `docker-compose`.
* **Day 18:** Cloud Deployment: Hosting FastAPI containers live on Render / Railway.
* **Day 19:** Frontend Integration: Connecting Streamlit or React web UIs to FastAPI backends.
* **Day 20:** Security Layer: CORS configuration, API Key authentication, and environment security.
* **Day 21:** **Capstone Project 3:** *Fully Containerized RAG Web Application Deployed Live.*

---

### Week 4: Observability, Optimization & Career Launch
Optimize systems for low latency, track API metrics, polish GitHub portfolio projects, and execute targeted outreach.

* **Day 22:** LLM Observability & Telemetry: Tracking cost, latency, and tokens using LangSmith or Phoenix.
* **Day 23:** Performance Optimization: Response streaming (`EventSourceResponse`) and caching frequent queries.
* **Day 24:** Advanced Retrieval: Reranking search results using Cohere/BGE rerankers.
* **Day 25–27:** **Final Portfolio Project:** End-to-end industry-grade AI application build.
* **Day 28:** System Architecture Documentation: Drawing data flow diagrams (User → API → Vector DB → LLM).
* **Day 29:** Portfolio Optimization: Creating 60-second video walkthroughs and technical GitHub `README` files.
* **Day 30:** Career Launch: ATS resume alignment and direct outbound outreach to Engineering Managers.

---

## 💡 Key Engineering Takeaways

1. **Validation at the Boundary:** Never trust raw strings returned by an LLM. Always run inputs and outputs through Pydantic models before passing data downstream.
2. **Async by Default:** Network calls to LLM APIs introduce latency. Using `async`/`await` prevents blocking thread pools under concurrent traffic.
3. **Decoupled Architecture:** Keep data ingestion, vector storage, and web presentation separated into isolated modules rather than monolithic scripts.
4. **Proof of Work over Certificates:** Deployed API endpoints, green CI/CD badges, Dockerized containers, and clear architecture diagrams carry significantly more weight than passive certificates.