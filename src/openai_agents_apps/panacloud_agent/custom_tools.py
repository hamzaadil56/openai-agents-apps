from typing import Any
from agents import RunContextWrapper, function_tool
from langchain_tavily import TavilySearch
import requests


@function_tool(name_override="search_courses")
async def search_courses(ctx: RunContextWrapper[Any], query: str) -> str:
    """Search for courses and learning materials.

    Args:
        query: The search query for courses and learning materials.
    """
    tool = TavilySearch(
        max_results=5,
        topic="education",
    )
    return tool.invoke({"query": query})


@function_tool(name_override="search_career_info")
async def search_career_info(ctx: RunContextWrapper[Any], query: str) -> str:
    """Search for career information and job market trends.

    Args:
        query: The search query for career information.
    """
    tool = TavilySearch(
        max_results=5,
        topic="career",
    )
    return tool.invoke({"query": query})


@function_tool(name_override="search_community")
async def search_community(ctx: RunContextWrapper[Any], query: str) -> str:
    """Search for community resources and events.

    Args:
        query: The search query for community resources.
    """
    tool = TavilySearch(
        max_results=5,
        topic="community",
    )
    return tool.invoke({"query": query})


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
def post_to_forum(forum_id: str, access_token: str, message: str):
    """
    Posts a message to the Panacloud forum.

    Parameters:
    - forum_id: str, the ID of the forum
    - access_token: str, the authentication token
    - message: str, the content to post

    Returns:
    - Response JSON from the forum API
    """
    post_url = f"https://api.panacloud.com/v1/forums/{forum_id}/posts"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'message': message
    }
    response = requests.post(post_url, headers=headers, json=payload)
    return response.json()


@function_tool
def get_course_progress(user_id: str, course_id: str, access_token: str):
    """
    Retrieves a user's progress in a specific course.

    Parameters:
    - user_id: str, the ID of the user
    - course_id: str, the ID of the course
    - access_token: str, the authentication token

    Returns:
    - Response JSON containing course progress information
    """
    progress_url = f"https://api.panacloud.com/v1/users/{user_id}/courses/{course_id}/progress"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(progress_url, headers=headers)
    return response.json()
