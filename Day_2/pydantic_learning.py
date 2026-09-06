# from typing import List, Optional
# from pydantic import BaseModel, Field, ValidationError

# class Skill(BaseModel):
#     name: str
#     years_experience: float = Field(
#         ..., ge=0, description="Must be greater than or equal to 0"
#     )


# class DeveloperProfile(BaseModel):
#     name: str
#     email: str
#     is_active: bool = True
#     skills: List[Skill]
#     github_url: Optional[str] = None


# # ----1. Constructing & Validating Data ----
# valid_data = {
#     "name": "Alex",
#     "email": "alex@example.com",
#     "skills": [
#         {"name": "Python", "years_experience": 2.5},
#         {"name": "FastAPI", "years_experience": 1.0},
#     ],
# }


# # Instantiate Model
# profile = DeveloperProfile(**valid_data)
# print(f"Validated Name: {profile.name}")

# #----2. Exporting Data  (Serialization) ----
# # Convert back to Python dict
# profile_dict = profile.model_dump()
# # print(profile_dict)
# #Convert directly to clean JSON string (Ready to return via API)
# json_output = profile.model_dump_json(indent=2)
# print("Pydantic Exported JSON: \n",json_output)


# # --- 3. Parsing Raw JSON Strings (Deserialization) ----
# raw_json_from_llm = '{"name": "Sarah", "email": "sarah@test.com", "skills": [{"name": "SQL","years_experience": 3 }]}'
# parsed_profile = DeveloperProfile.model_validate_json(raw_json_from_llm)

# # parsed_profile = DeveloperProfile.model_validate(valid_data)
# print(f"Parsed Sarah's primary skill: {parsed_profile.skills[0].name}")



from typing import List, Optional
from pydantic import Field, BaseModel, ValidationError

class research_paper(BaseModel):
    title: str
    subject: str
    branch: str
    citation: Optional[int] = None

class scientist_profile(BaseModel):
    name: str
    email: str
    Id: str
    dept: str
    research_papers: List[research_paper]

scientist_info = {
    "name": "Dr. BK Goyal",
    "email": "dr.bkgoyal@email.com",
    "Id": "MR2310",
    "dept": "Mathematics",
    "research_papers": [
        {
            "title": "Vector Geometry",
            "subject": "Geometry",
            "branch": "Applied Mathematics",
        }
    ]
}

#Instantiation
scientist_01 = scientist_profile(**scientist_info)

#Serialization
scientist_detailed_JSON = scientist_01.model_dump_json(indent=2)
print(f"The JSON for the scientist info is as follows: \n{scientist_detailed_JSON}")