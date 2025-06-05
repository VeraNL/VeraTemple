import asyncio
import importlib  
foobar = importlib.import_module("../../ext/fast-agent")

# foobar.mcp_agent.core.fastagent.FastAgent

# from ...ext.fast_agent.mcp_agent.core.fastagent import FastAgent

# Create the application
fast = foobar.mcp_agent.core.fastagent.FastAgent("fast-agent agent_one (mcp server)")


# Define the agent
@fast.agent(name="agent_one", instruction="You are a helpful AI agent.")
async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())