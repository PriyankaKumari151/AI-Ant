import os
import json
from typing import Literal
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field, ValidationError

#Load local env variables
load_dotenv()

#Safe API Key Resolution
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    try:
        api_key=st.secrets["GROQ_API_KEY"]
    except  Exception:
        api_key=None

#Initialize OpenAI Client pointing to Groq
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
)

#1. Define Pydantic Output Schema
class CustomerLead(BaseModel):
    client_name: str = Field(description="Full name of the client or company")
    budget_usd: float = Field(ge=0, description="Estimated budget in USD. Return 0.0 if not specified")
    urgency: Literal["High","Medium","Low"] = Field(description="Priority level strictly limited to 'High', 'Medium' or 'Low'")
    requested_services: list[str] = Field(description="List of requested features or services")

#Page Config
st.set_page_config(page_title="AI Lead Extractor", page_icon="📊", layout="wide")
st.title("📊 Enterprise Lead Extractor & Schema Enforcer")

#2. Sidebar Parameters
with st.sidebar:
    st.header("Model Settings")
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.0,
        step=0.05,
        help="0.0 is completely deterministic; higher values increase creativity."
    )

#3. Input
st.subheader("Input Unstructures Client Data")
raw_text = st.text_area(
    "Paste raw email, inquiry, or meeting transcript below:",
    height=150,
    placeholder="Hi, I am Alex from Acme Corp. We urgently need a chatbot built with a $10,000 budget."
)

#4. Processing Action
if st.button("⚡Extract Structured Lead", type="primary"):
    if not raw_text.strip():
        st.warning("Please enter some text to process.")
    else:
        with st.spinner("Analyzing text and enforcing Pydantic schema..."):
            try:
                #Call API with explicit JSON Schema instruction
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    temperature=temperature,
                    response_format={
                        "type":"json_object"
                    },
                    messages=[
                        {
                            "role":"system",
                            "content":(
                                "You are a precise data extraction engine. Extract information from the user text "
                                f"and return ONLY valid JSON strictly matching this schema:\n{json.dumps(CustomerLead.model_json_schema())}"
                            ),
                        },
                        {
                            "role":"user",
                            "content":raw_text
                        },
                ],
                )
                #Parse and Validate with  Pydantic
                raw_json_str = response.choices[0].message.content
                validated_lead = CustomerLead.model_validate_json(raw_json_str)

                st.success("Data successfully extracted and validated!")

                #Display Results in Structured Layout
                col1, col2, col3 = st.columns(3)
                col1.metric("Client Name",validated_lead.client_name)
                col2.metric("Estimated Budget", f"${validated_lead.budget_usd:,.2f}")
                col3.metric("Urgency",validated_lead.urgency)

                st.markdown("###Requested Services")
                st.write(validated_lead.requested_services)

                #Inspect Raw Validated JSON
                with st.expander("🔍 View Raw Validated JSON"):
                    st.json(validated_lead.model_dump())
            
            except validationError as ve:
                st.error(f"⚠️ AI Output Schema Violation")
                st.code(str(ve), language="json")
            except Exception as e:
                #Triggered for API Keys, network errors, or timeout issues
                st.error(f"System Error: {e}")

                