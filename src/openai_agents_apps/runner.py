import asyncio
from agents import Runner

async def run_agent_with_query(agent, query, run_config):
    """Run an agent with a specified query and configuration"""
    result = await Runner.run(agent, query, run_config=run_config)
    return result

async def print_agent_response(agent, query, run_config):
    """Run an agent and print its response"""
    result = await run_agent_with_query(agent, query, run_config)
    print(result.final_output)
    return result

async def stream_agent_events(agent, query, run_config):
    """Stream events from an agent run"""
    result = await Runner.run(agent, query, run_config=run_config)
    async for event in result.stream_events():
        print(event)
    return result