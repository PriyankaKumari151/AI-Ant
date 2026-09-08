from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

#Define enums for restricted choices
class PriorityLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

#Nested complex object
class Contact(BaseModel):
    name: str = Field(..., description="Full name of contact person")
    email: str = Field(..., description="Business email address")
    role: Optional[str] = Field(None, description="Job title or department")

#Main tool parameter schema
class CreateEnterpriseLeadInput(BaseModel):
    company_name: str = Field(..., description="Target organization name")
    annual_revenue: float = Field(..., description="Estimated revenue in USD")
    priority: PriorityLevel = Field(..., description="Lead urgency level")
    tech_stack: List[str] = Field(..., description="Technologies used by company")
    contacts: List[Contact] = Field(..., description="Key decision makers")

tools = [
    {
        "type": "function",
        "function": {
            "name": "create_enterprise_lead",
            "description": "Register a full multi-contact enterprise deal in the CRM.",
            #Auto generates the entire nested JSON schema dictionary
            "parameters": CreateEnterpriseLeadInput.model_json_schema()            
        } 
        
    }
]

print(tools)