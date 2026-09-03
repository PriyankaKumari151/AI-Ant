from pydantic import BaseModel, Field, ValidationError
from typing import Dict, List
import asyncio
import os
from dotenv import load_dotenv
import json


class AIResponse(BaseModel):
    query_id: str
    confidence_score: float = Field(
        ..., ge=0.0, le=1.0)
    tags: List[str]
    execution_time_ms: int

async def mock_fetch_llm_data(query: str)->str:
    await asyncio.sleep(1)
    mock_data = {
        "query_id": "q76",
        "confidence_score": 0.6,
        "tags": ["apple","banana","grapes"],
        "execution_time_ms": 4
        }
    return json.dumps(mock_data)

async def main():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        print(f"GROQ API Keys are fetched successfully")

    result1, result2 = await asyncio.gather(mock_fetch_llm_data("Extract entities"),
    mock_fetch_llm_data("Summarize text"))
    obj1 = AIResponse.model_validate_json(result1)
    obj2 = AIResponse.model_validate_json(result2)
    print(f"JSON dump corresponding to string: Extract entities \n{obj1.model_dump_json(indent=2)}")
    print(f"JSON dump corresponding to string: Summarize text \n{obj2.model_dump_json(indent=2)}")

if __name__ == "__main__":
    asyncio.run(main())