import asyncio
from typing import Dict, List, Optional

#1. Type Hints Example
def process_skills(user_id: int, raw_skills: List[str])->Dict[str,int]:
    return {"user_id": user_id, "total_skills": len(raw_skills)}

#2. Async Python Example
async def simulate_llm_api_call(prompt: str)->str:
    print(f"Sending prompt to LLM: '{prompt}'...")
    #asyncio.sleep simulates network delay without stopping the whole CPU thread
    await asyncio.sleep(2)
    return f"Response for '{prompt}': Processed successfully."

async def main():
    #Calling async functions requires 'await' inside  an async context
    result = await simulate_llm_api_call("Extract keywords from resume")
    print(result)

#Standard entry point to run async functions in Python
if __name__ == "__main__":
    asyncio.run(main())
    # # run(main())
    # main()





#Example Program by Priyanka Kumari (2022UCP1669)


# import asyncio
# import statistics
# from typing import Dict, List, Optional


# async def process_Salary(employee_id: int, dept: str, yearlySalary: Dict[str,int])->Dict[int,int]:
#     print(f"Calculating Annual Average Salary for Employee_ID {employee_id}")
#     await asyncio.sleep(2)
#     annualAvgSalary =statistics.mean(yearlySalary.values())
#     return {employee_id: annualAvgSalary}

# async def main():
#     employee_id = 102
#     dept = "SRE"
#     yearlySalary = {
#         'Jan': 20000,
#         'Feb': 10000,
#         'Mar': 15000,
#         'Apr': 19000,
#         'May': 15000,
#         'June': 15000,
#         'July': 14900,
#         'Aug': 17000
#     }

#     result = await process_Salary(employee_id,dept,yearlySalary)
#     print(f"The annual average salary for employee {employee_id} is {result}")

# if __name__ == "__main__":
#     asyncio.run(main())


