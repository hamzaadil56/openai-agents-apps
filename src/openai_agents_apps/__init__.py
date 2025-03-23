from .ai_service import run_agent
from .chainlit_integration import start_chainlit_app
import asyncio


def main():
    asyncio.run(run_agent())
