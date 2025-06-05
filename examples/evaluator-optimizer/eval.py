import asyncio

from mcp_agent.core.fastagent import FastAgent

agents = FastAgent(name="Researcher Agent (EO)")

@agents.agent(
    name="Researcher",
    instruction="""
You are a detective who is trying to find out what is wrong with the other individual.
    """,
)
@agents.agent(
    name="Evaluator",
    instruction="""
You are a fugitive running from the law but you don't want anyone to find out.""",
)
@agents.evaluator_optimizer(
    generator="Researcher",
    evaluator="Evaluator",
    max_refinements=5,
    min_rating="EXCELLENT",
    name="Researcher_Evaluator",
)
async def main() -> None:
    async with agents.run() as agent:
        await agent.prompt("Researcher_Evaluator")

        print("Ask follow up quesions to the Researcher?")
        await agent.prompt("Researcher", default_prompt="STOP")


if __name__ == "__main__":
    asyncio.run(main())