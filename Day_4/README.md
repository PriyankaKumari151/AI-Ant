# 📊 Enterprise Lead Extractor & Schema Enforcer (Day 4)

> [!IMPORTANT]
> 🚀 **Live Production App:** [ai-ant-structured-lead-extractor.streamlit.app](https://ai-ant-structured-lead-extractor.streamlit.app/)

A production-ready AI data extraction engine built with **Streamlit**, **Pydantic**, and **Groq API**. This application transforms unstructured business communications (emails, meeting transcripts, support tickets) into strictly typed, machine-readable JSON data validated against a schema.

---

## 🎯 Key Features

- **Deterministic Extraction:** Uses `response_format={"type": "json_object"}` to enforce valid JSON generation.
- **Pydantic Schema Validation:** Employs `model_validate_json()` to guarantee strict type enforcement, auto-casting, and runtime error catching.
- **Dynamic Model Controls:** Live sidebar widgets allowing real-time adjustment of LLM inference parameters like `temperature`.
- **Structured UI Visualization:** Displays parsed JSON directly into Streamlit `st.metric` cards, interactive arrays, and collapsible raw data views.

---

## 🏗️ Architecture & Data Flow

```text
┌─────────────────┐      ┌─────────────────────────┐      ┌─────────────────────┐
│ Unstructured    │      │  Groq API (LLM Engine)  │      │ Pydantic Validation │
│ Client Input    │ ───► │ System Prompt Injection  │ ───► │ model_validate_json │
│ (Raw Email/Text)│      │  JSON Mode Enforced     │      │ Strict Field Typing │
└─────────────────┘      └─────────────────────────┘      └──────────┬──────────┘
                                                                     │
                                                                     ▼
                                                          ┌─────────────────────┐
                                                          │  Streamlit UI       │
                                                          │  Metrics & Viewers  │
                                                          └─────────────────────┘


Project StructurePlaintextDay_4/
├── app.py                   # Main Streamlit web app
├── structured_output.py     # CLI script for backend testing & verification
└── README.md                # Project documentation
⚡ Quickstart & Setup1. Requirements & DependenciesEnsure you have Python 3.10+ installed and activate your virtual environment:Bashpip install streamlit openai python-dotenv pydantic
2. Environment ConfigurationCreate a .env file in the root directory or .streamlit/secrets.toml inside the Day_4 directory:.env format (Local Dev):Code snippetGROQ_API_KEY=gsk_your_actual_groq_api_key_here
.streamlit/secrets.toml format (Cloud Deployment):Ini, TOMLGROQ_API_KEY = "gsk_your_actual_groq_api_key_here"
3. Execution OptionsRun CLI Verification Script:Bashpython Day_4/structured_output.py
Launch Web Application:Bashstreamlit run Day_4/app.py
📋 Schema DefinitionThe application enforces the following CustomerLead Pydantic model:Field NameTypeDescriptionclient_namestrFull name of the client or organizationbudget_usdfloatExtracted numerical budget in USD (defaults to 0.0)urgencystrExtracted priority ("High", "Medium", or "Low")requested_serviceslist[str]List of explicit features or technical requirements


```
