from agents import Agent, FileSearchTool, Runner, WebSearchTool


def create_math_tutor():
    """Create and return a math tutor agent"""
    return Agent(
        name="Math Tutor",
        instructions="You provide help with math problems. Explain your reasoning at each step and include examples"
    )


def create_history_tutor():
    """Create and return a history tutor agent"""
    return Agent(
        name="History Tutor",
        handoff_description="Specialist agent for historical questions",
        instructions="You provide assistance with historical queries. Explain important events and context clearly.",
    )


def web_search_agent(model: str):
    """Create and return a web search agent"""
    return Agent(
        model=model,
        name="Web Search Agent",
        handoff_description="Specialist agent for searching the web and returning the best resources from the internet.",
        instructions="You provide assistance with web searches. Return the best resources from the internet.",
        tools=[
            WebSearchTool(),
            FileSearchTool(
                max_num_results=3,
                vector_store_ids=["VECTOR_STORE_ID"],
            ),
        ],
    )


agent = Agent(
    name="Assistant",
    tools=[
        WebSearchTool(),
        FileSearchTool(
            max_num_results=3,
            vector_store_ids=["VECTOR_STORE_ID"],
        ),
    ],
)


def create_triage_agent(handoff_agents):
    """Create and return a triage agent with specified handoff agents"""
    return Agent(
        name="Triage Agent",
        instructions="You determine which agent to use based on the user's homework question",
        handoffs=handoff_agents
    )
