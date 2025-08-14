import asyncio

from dotenv import load_dotenv
load_dotenv()

from browser_use import Agent
from browser_use.llm.openai.chat import ChatOpenAI

async def main():
    llm = ChatOpenAI("gpt-4.1-mini")
    task = """
         Go to the website https://quotes.toscrape.com/  and extract following information:
         - The first 5 quotes on the page
         - The author of each quote
         - The tags associated with each quote

         present the information in a clear and structured format like:
         Quote 1: "[quote text]" - Author: [author name] - Tags: [tag1, tag2]
         Quote 2: "[quote text]" - Author: [author name] - Tags: [tag1, tag2]
         etc

        """
    agent = Agent(task=task, llm=llm)
    result = await agent.run()
    print(f"Final answer is : {result.final_result()}")

if __name__ == "__main__":
    asyncio.run(main())