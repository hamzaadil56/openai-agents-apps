import json

from typing_extensions import TypedDict, Any

from agents import RunContextWrapper, function_tool
from langchain_tavily import TavilySearch
import requests


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


@function_tool
def post_to_facebook(page_id, access_token, message):
    """
    Posts a message to a Facebook page.

    Parameters:
    - page_id: str, the ID of the Facebook page.
    - access_token: str, the long-lived Page Access Token.
    - message: str, the content to post.

    Returns:
    - Response JSON from Facebook Graph API.
    """
    post_url = f"https://graph.facebook.com/v19.0/{page_id}/feed"
    payload = {
        'message': message,
        'access_token': access_token
    }
    response = requests.post(post_url, data=payload)
    return response.json()
