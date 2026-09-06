import os
from dotenv import load_dotenv
from openai import OpenAI,OpenAIError


load_dotenv()

conversation_history = [
    {
        "role":"system",
        "content":"Generate answers in plain bullet points.",
    }
]

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key = os.getenv("GROQ_API_KEY")
)

# print([model.id for model in client.models.list().data])

def query_llm_api(history: list)->str:
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            temperature=0.0,
            max_completion_tokens=150,
            messages=history 
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        print("API Error encountered: ",{e})
        return None


if __name__ == "__main__":
    print("---- Session started (Type 'exit' to quit) ----\n")

    while True:
        user_input = input("Enter the query: ").strip()
     
        if user_input.lower()=="exit":
            print("LLM: Bye")
            break
        if not user_input:
            continue

        conversation_history.append({
            "role":"user",
            "content":user_input
        })

        response = query_llm_api(conversation_history)

        if response:
            conversation_history.append(
                {
                    "role":"assistant",
                    "content":response
                }
            )
            print(f"\nLLM: {response}\n")
        else:
            conversation_history.pop()
