import asyncio

from mcp_agent.core.fastagent import FastAgent

agents = FastAgent(name="A2A Convo")

@agents.agent(
    name="Detective",
    instruction="""
You are a detective trying to come to the truth about a fugitive on the run.
    """,
)
@agents.agent(
    name="Fugitive",
    instruction="""
You are a fugitive on the run for robbing a bank who doesn't want anyone to know the truth.""",
)
# @agents.evaluator_optimizer(
#     generator="Fugitive",
#     evaluator="Detective",
#     max_refinements=5,
#     min_rating="EXCELLENT",
#     name="Detective_Fugitive",
# )
@agents.chain(
  "Detective_Fugitive",
  sequence=["Detective","Fugitive","Detective","Fugitive"]
)
async def main() -> None:
    async with agents.run() as agent:
        await agent.prompt("Detective_Fugitive")


if __name__ == "__main__":
    asyncio.run(main())