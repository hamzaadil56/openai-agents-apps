from agents.tool import function_tool
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


@function_tool("get_weather")
def get_weather(location: str, unit: str = "C") -> str:
    """
    Fetch the weather for a given location, returning a short description.
    """
    # Example logic
    return f"The weather in {location} is 22 degrees {unit}."


@function_tool("piaic_student_finder")
def student_finder(student_roll: int) -> str:
    """
    find the PIAIC student based on the roll number
    """
    data = {1: "Qasim",
            2: "Sir Zia",
            3: "Daniyal"}

    return data.get(student_roll, "Not Found")


async def run_agent_with_tools():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        tools=[get_weather, student_finder],  # add tools here
        model=model
    )

    result = await Runner.run(agent, "Share PIAIC roll no1 student details.")
    print(result.final_output)
