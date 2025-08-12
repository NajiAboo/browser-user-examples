from dotenv import load_dotenv
load_dotenv()

import asyncio
import os

from browser_use import Agent
from browser_use.llm.openai.chat import ChatOpenAI

async def main():
    llm = ChatOpenAI('gpt-4.1-mini')

    task = """ 
    Go to https://httpbin.org/forms/post and fillout the contact form with :

    - Customer Name: John Doe
    - Telephone: 111-111-1111
    - Email: job.doe@test.com
    - Size: Medium
    - Toppings: Cheese
    - Delivery: Time: 1:30 PM 
    - Comments: My place is near the supermarket    


    Then Submit the form and tell me the reponse

    """

    agent = Agent(task=task, llm=llm)

    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
