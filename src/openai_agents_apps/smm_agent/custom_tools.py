import json

from typing_extensions import TypedDict, Any

from agents import Agent, FunctionTool, RunContextWrapper, function_tool
from langchain_tavily import TavilySearch


class Location(TypedDict):
    lat: float
    long: float

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
    return "sunny"

@function_tool  
async def fetch_weather(location: Location) -> str:
    
    """Fetch the weather for a given location.

    Args:
        location: The location to fetch the weather for.
    """
    # In real life, we'd fetch the weather from a weather API
    return "sunny"


@function_tool(name_override="fetch_data")  
def read_file(ctx: RunContextWrapper[Any], path: str, directory: str | None = None) -> str:
    """Read the contents of a file.

    Args:
        path: The path to the file to read.
        directory: The directory to read the file from.
    """
    # In real life, we'd read the file from the file system
    return "<file contents>"


agent = Agent(
    name="Assistant",
    tools=[fetch_weather, read_file],  
)

for tool in agent.tools:
    if isinstance(tool, FunctionTool):
        print(tool.name)
        print(tool.description)
        print(json.dumps(tool.params_json_schema, indent=2))
        print()