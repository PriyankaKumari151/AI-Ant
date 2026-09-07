##Day 4 
##Example Program


import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=api_key)

#1. Define Target Output Schema using Pydantic
class CustomerLead(BaseModel):
    client_name: str = Field(description="Full name of the client or company")
    budget_usd: float = Field(description="Estimated budget in USD. Return 0.0 if not specified")
    urgency: str = Field(description="Priority level: 'High', 'Medium', or 'Low'")
    requested_services: list[str] = Field(description="List of requested features or services.")

#2. Raw Unstructured Email Input
raw_email= """
Hi AI Team,
My name is Sarah Connor from Cyberdyne Systems. We urgently need a custom internal chatbot UI built with Streamlit
and linked to our private FAQ database. We have a budget of around $4500 set aside for this.
"""

#3. Request JSON Schema Output from LLM
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    temperature=0.0,
    response_format={
        "type":"json_object"
    },
    messages = [
        {
        "role":"system",
        "content": (
            "You are a strict data extraction engine. Extract information from the user text "
            f"and ouput strictly formmatted JSON matching this schema:\n{json.dumps(CustomerLead.model_json_schema())}"
        ),
        },
        {
            "role":"user",
            "content":raw_email
        },
    ],
)

#4. Parse & Validate JSON response with Pydantic
raw_json_str = response.choices[0].message.content
lead_data = CustomerLead.model_validate_json(raw_json_str)

print("----Validated Pydantic Object----")
print(f"Client: {lead_data.client_name}")
print(f"Budget: ${lead_data.budget_usd:.2f}")
print(f"Urgency: {lead_data.urgency}")
print(f"Services: {','.join(lead_data.requested_services)}")
