import json
from pydantic import BaseModel, Field

class Cereal(BaseModel):
    name: str
    price_per_kg: int
    origin: str


##Schema Generation
cereal_schema = Cereal.model_json_schema()
print(type(cereal_schema))
print(json.dumps(cereal_schema,indent=2))