import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"))

# print([model.id for model in client.models.list().data])

def query_llm_with_roles(user_prompt: str)->str:
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            temperature = 0.0,  ##Removes randomness
            max_completion_tokens = 150,  ##Hardcap on response length
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a concise enterprise software assistant. "
                        "Answer queries in 2 sentences or fewer. "
                        "If you do not know the answer, reply with 'UNKNOWN'."
                    ),
                },
                {"role":"user","content":user_prompt},
            ],
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        print(f"APT Error encountered: {e}")
        return "ERROR_PROCESSING_REQUEST"
    
if __name__ == "__main__":
    result = query_llm_with_roles(
        "What is the difference between TCP and UDP?"
    )
    print("LLM Response:\n",result)






# import os
# from openai import OpenAI,OpenAIError
# from dotenv import load_dotenv

# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def query_llm_api(user_prompt: str)->str:
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini", ##fast, cost-effective, production model
#             temperature=0.0,
#             max_completion_tokens=150,
#             messages = [
#                 {
#                     "role": "system",
#                     "context": (
#                         "You are a chatbot.",
#                         "Be concise in response (max 2 lines).",
#                         "If you don't know the answer, reply: 'unknown'."
#                     ),
#                 },
#                 {"role": "user", "content": user_prompt},
#             ],
#         )
#         return response.choices[0].message.content
#     except OpenAIError as e:
#         print(f"API ERROR: {e}")
#         print("ERROR IN RESPONSE GENERATION")

# if __name__ == "__main__":
#     response = query_llm_api("What is IP address?")
#     print("LLM Response: \n",response)




