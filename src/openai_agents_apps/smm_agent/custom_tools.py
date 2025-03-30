import json

from typing_extensions import TypedDict, Any

from agents import RunContextWrapper, function_tool
from langchain_tavily import TavilySearch


@function_tool(name_override="research")
async def search_internet(ctx: RunContextWrapper[Any], query: str) -> str:
    """Search the internet and gather the important information.

    Args:
        query: The query to search for.
    """
    tool = TavilySearch(
        max_results=5,
        topic="general",
    )
    return tool.invoke({"query": query})
