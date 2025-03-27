# agents_module/config.py
import os
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel, AsyncOpenAI
from agents.run import RunConfig


def load_environment():
    """Load environment variables from .env file"""
    load_dotenv()


def get_gemini_client():
    """Create and return a configured AsyncOpenAI client for Gemini"""
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    # Check if the API key is present; if not, raise an error
    if not gemini_api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

    # Reference: https://ai.google.dev/gemini-api/docs/openai
    return AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )


def create_model(client, model_name="gemini-2.0-flash"):
    """Create a model instance with the specified client and model name"""

    return OpenAIChatCompletionsModel(
        model=model_name,
        openai_client=client
    )


def create_run_config(model, client):
    """Create a run configuration for agents"""
    return RunConfig(
        model=model,
        model_provider=client,
        tracing_disabled=True
    )
