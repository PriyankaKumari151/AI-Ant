# 🤖 Production-Style AI Assistant with Conversational Memory

A lightweight, enterprise-grade conversational AI web application built with Python, Streamlit, and Groq's high-speed API. This project demonstrates universal role-based message schemas, persistent multi-turn chat memory, secure cloud secret injection, and live deployment on Streamlit Community Cloud.

---

## 🚀 Live Demo

* **Deployed App:** [Access Live Streamlit Web App](https://ai-ant-aapiw39bgm2isjplypr9a6.streamlit.app/)

---

## 🛠️ Tech Stack & Architecture

| Component | Technology / Library | Purpose |
| :--- | :--- | :--- |
| **Frontend UI** | `Streamlit` | Pure-Python interactive web chat interface |
| **LLM Provider** | `Groq API` (OpenAI SDK) | High-speed open-weights model execution |
| **API Protocol** | `OpenAI Chat Completions` | Universal `/v1/chat/completions` REST specification |
| **Memory Management** | `st.session_state` | In-memory session tracking for stateful multi-turn history |
| **Secrets Management** | `python-dotenv` / `st.secrets` | Secure API key isolation for local dev and cloud deployment |
| **Hosting Platform** | `Streamlit Community Cloud` | Serverless cloud hosting with GitHub CI/CD auto-deployment |

---

## ✨ Key Features

* **Universal Message Schema:** Follows the standard `[{"role": "system|user|assistant", "content": "..."}]` array format compatible across major LLM providers (OpenAI, DeepSeek, Anthropic, Ollama).
* **Stateful Conversational Context:** Retains historical context across user interactions without re-initializing during UI re-renders.
* **Fault-Tolerant Execution:** Includes robust key-resolution logic that falls back seamlessly between local environment variables (`.env`) and cloud configuration (`st.secrets`).
* **Zero Infrastructure Overhead:** Deployed cleanly using containerized cloud builds from a minimal `requirements.txt`.

---

## 📁 Repository Structure

```text
ai-ant/
├── requirements.txt         # Minimal production dependencies
├── README.md                # Project documentation
└── Day_3/
    ├── app.py               # Streamlit web application & conversational UI
    └── production_style_api_call.py  # Standalone CLI backend implementation



💻 Local Environment Setup1. Initialize Virtual EnvironmentBash# Clone repository
git clone [https://github.com/priyankakumari151/ai-ant.git](https://github.com/priyankakumari151/ai-ant.git)
cd ai-ant

# Create isolated environment
python -m venv venv

# Activate environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
2. Configure DependenciesCreate a requirements.txt file in the root directory containing only your core imports (avoid global pip freeze dumps):Plaintextstreamlit
openai
python-dotenv
Install packages:Bashpip install -r requirements.txt
3. Secure Environment VariablesCreate a local .env file in the root folder:Code snippetGROQ_API_KEY=gsk_your_groq_api_key_here
Ensure .env is included in your .gitignore file:Plaintext.env
venv/
__pycache__/
⚙️ Core Application Implementation (Day_3/app.py)This implementation supports both local execution and cloud execution via dual secret resolution, and maintains stateful conversational memory using st.session_state.Pythonimport os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

# Load local environment variables if available
load_dotenv()

# Page Configuration
st.set_page_config(page_title="Groq AI Assistant", page_icon="🤖")
st.title("🤖 Groq AI Assistant with Memory")

# 1. Dual Secret Resolution (Streamlit Cloud Secrets -> Local .env)
api_key = st.secrets.get("GROQ_API_KEY") if hasattr(st, "secrets") and "GROQ_API_KEY" in st.secrets else os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Missing GROQ_API_KEY! Please configure it in .env or Streamlit Secrets.")
    st.stop()

# 2. Initialize OpenAI Client pointing to Groq's Endpoint
client = OpenAI(
    base_url="[https://api.groq.com/openai/v1](https://api.groq.com/openai/v1)",
    api_key=api_key,
)

# 3. Session State Initialization for Conversational Memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful enterprise software assistant. Keep responses clear and concise.",
        }
    ]

# 4. Render Conversation History in UI
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 5. Chat Input and Completion Loop
if prompt := st.chat_input("Ask a question..."):
    # Render user prompt
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call LLM API with full conversation context
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    temperature=0.0,
                    max_completion_tokens=300,
                    messages=st.session_state.messages,
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
                
                # Append assistant reply to session memory
                st.session_state.messages.append({"role": "assistant", "content": reply})

            except OpenAIError as e:
                st.error(f"API Error encountered: {e}")
                st.session_state.messages.pop()  # Rollback last user input on failure
☁️ Streamlit Cloud Deployment WorkflowGitHub Sync: Commit and push all changes to your main branch.Dashboard Setup: Log in to share.streamlit.io via GitHub.App Configuration:Repository: priyankakumari151/ai-antBranch: mainMain file path: Day_3/app.pySecret Configuration: Navigate to Advanced Settings → Secrets and enter your API key using TOML format:Ini, TOMLGROQ_API_KEY = "gsk_your_groq_api_key_here"
Deploy: Click Deploy!. Streamlit Cloud provisions the environment and installs packages from root requirements.txt.🛠️ Critical Troubleshooting LogIssueRoot CauseSolutionError 429 insufficient_quotaOpenAI account credit exhausted ($0 balance).Switched provider to Groq using standard OpenAI SDK via base_url="https://api.groq.com/openai/v1".Error 404 model_not_foundModel string changed or deprecated by provider tier.Queried active models using [m.id for m in client.models.list().data] and set active model string (openai/gpt-oss-120b).Invalid requirement: '3/requirements.txt'Directory path contained spaces (Day 3/app.py).Renamed directory to Day_3 and placed requirements.txt in the repository root.uv / pip dependency build failureBloated requirements.txt generated from global pip freeze.Cleaned requirements.txt to contain only explicit application imports (streamlit, openai, python-dotenv).Missing credentials on CloudApplication called os.getenv() on Streamlit Cloud where env vars aren't injected automatically.Used st.secrets.get("GROQ_API_KEY") as primary fallback before os.getenv().