import os
import json
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

#Client setup
api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = OpenAI(base_url="https://api.groq.com/openai/v1",api_key=api_key)

#----------------------------------------------
# Step 1: Define Backend Executable Functions
#----------------------------------------------

def lookup_company_db(domain: str)->str:
    """Simulates querying an enterprise data provider (e.g., Clearbit/Apollo)."""
    mock_data = {
        "stripe.com": {"company": "Stripe", "employees":8000, "funding": "$8.7B", "tech_stack":["Ruby","Go","AWS"]},
        "notion.so": {"company": "Notion", "employees": 1200, "funding": "$343M", "tech_stack": ["Typescript","React","GCP"]},
    }
    result = mock_data.get(domain.lower(), {"company": domain, "employees": 25, "funding": "Bootstrapped", "tech_stack": ["Unknown"]})
    return json.dumps(result)

def trigger_crm_alert(company_name: str, lead_score: int, reason: str)->str:
    """Simulates sending a webhook to Slack or HubSpot."""
    return f"SUCCESS: Alert posted for '{company_name} (Score: {lead_score}/10). Rationale: {reason}"


tool_dispatcher = {
    "lookup_company_db": lookup_company_db,
    "trigger_crm_alert": trigger_crm_alert
}

#-------------------------------------------
#Step 2: Define OpenAI Tool Schemas
#-------------------------------------------

tools = [
    {
        "type": "function",
        "function": {
            "name": "lookup_company_db",
            "description": "Fetch real company headcount, funding , and tech stack by domain.",
            "parameters": {
                "type": "object",
                "properties": {
                    "domain" : {
                        "type": "string", "description": "Target company domain, e.g., strip.com"},
                    },
                    "required": ["domain"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "trigger_crm_alert",
                "description": "Send a prioritized lead alert to the sales team's CRM  or Slack channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "company_name": {"type": "string", "description": "Name of target company"},
                        "lead_score" :{"type": "integer", "description": "Priority score from 1 (lowest) to 10 (highest)"},
                        "reason": {"type": "string", "description": "Brief explanation for the assigned score"},    
                    },
                    "required": ["company_name", "lead_score","reason"],
                },
            },
        },
]

#--------------------------------------------------
# Step 3: Streamlit Intetface & Orchestration Loop
#---------------------------------------------------

st.set_page_config(page_title="RevOps Tool Calling Agent", page_icon="⚙️", layout="wide")
st.title("⚙️ RevOps Intelligence & CRM Action Agent")

prompt = st.text_area(
    "Instruction:",
    value="Check out stripe.com. If they have more than 1,000 employees, trigger a high-priority CRM alert with a score of 9.",
    height=100
)

if st.button("🚀 Run Agent Loop", type="primary"):
    messages = [{"role": "user", "content": prompt}]

    with st.spinner("Processing request through tool-calling pipeline..."):
        max_turns = 5
        turn = 0
       
        while turn < max_turns:
            turn += 1

            #First Inference Pass
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages,
                tools=tools,
                tool_choice="auto",
            )
            response_msg = response.choices[0].message
            print(response_msg)
            print(turn)
            messages.append(response_msg)
            print(messages)

            #Tool Execution Loop
            if response_msg.tool_calls:
                st.markdown("###🔄️ Execution Trace")
                for tool_call in response_msg.tool_calls:
                    fn_name = tool_call.function.name
                    fn_args = json.loads(tool_call.function.arguments)

                    st.info(f"**Executing Tool:** `{fn_name}`")
                    st.json(fn_args)

                    #Execute Python local function
                    if fn_name in tool_dispatcher:
                        execution_result = tool_dispatcher[fn_name](**fn_args)

                        #Feed output back to message history
                        messages.append({
                            "role":"tool",
                            "tool_call_id":tool_call.id,
                            "name":fn_name,
                            "content":str(execution_result),
                        })
                    
                    # #Final Synthesis Pass
                    # final_response = client.chat.completions.create(
                    #     model="openai/gpt-oss-120b",
                    #     messages=messages,
                    # )

                    # st.markdown("### 📝 Final Synthesis")
                    # st.success(final_response.choices[0].message.content)

            else:
                st.markdown("### 📝 Final Synthesis")
                st.success(response_msg.content)
                break