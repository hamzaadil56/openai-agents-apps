import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio
import chainlit as cl


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError(
        "GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


async def run_agent():
    math_tutor_agent = Agent(
        name="Math Tutor",
        instructions="You provide help with math problems. Explain your reasoning at each step and include examples")

    history_tutor_agent = Agent(
        name="History Tutor",
        handoff_description="Specialist agent for historical questions",
        instructions="You provide assistance with historical queries. Explain important events and context clearly.",
    )
    triage_agent = Agent(
        name="Triage Agent",
        instructions="You determine which agent to use based on the user's homework question",
        handoffs=[history_tutor_agent, math_tutor_agent]
    )

    result = await Runner.run(
        triage_agent, "What is x2+2x+1=0?", run_config=config)
    print(result.final_output)

    # async for e in result.stream_events():
    #     print(e)
    # Function calls itself,
    # Looping in smaller pieces,
    # Endless by design.
