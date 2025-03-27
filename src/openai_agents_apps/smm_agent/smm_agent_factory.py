from agents import Agent, FileSearchTool, Runner, WebSearchTool


def market_research_agent():
    """Create and returns a market and audience research agent using various tools"""
    return Agent(
        name="Market Research Agent",
        instructions="You provide market and audience research on a topic. You can use the web search tool to find information on the topic.",
        tools=[
            WebSearchTool()
        ],
        handoff_description="Specialist agent for market and audience research"
    )
def strategic_planning_kpi_agent():
    """Create and return a strategic planning and KPI agent for social media management"""
    return Agent(
        name="Strategic Planning & KPI Agent",
        instructions=(
            "You define clear, measurable social media objectives such as increased awareness, higher engagement, and conversion goals, choose the right social platforms based on target audience insights, and establish key performance indicators (KPIs) to measure success, providing examples similar to how Spotify builds personalized campaigns to drive engagement and brand loyalty."
        ),
        tools=[
            WebSearchTool()
        ],
        handoff_description="Specialist agent for strategic planning and KPI measurement in social media"
    )


def content_creation_curation_agent():
    """Create and return a content creation and curation agent for social media management"""
    return Agent(
        name="Content Creation & Curation Agent",
        instructions=(
            "Develop a content calendar that covers all types of content (educational, inspirational, behind-the-scenes, etc.), create high-quality, visually appealing assets (images, videos, graphics) that align with the brand’s voice, and curate user-generated content when appropriate, crafting dynamic, on-brand content similar to Dunkin’s playful spider doughnut campaign that sparks interest and drives sharing."
        ),
        tools=[
            WebSearchTool()
        ],
        handoff_description="Specialist agent for content creation and curation in social media"
    )

def community_engagement_management_agent():
    """Create and return a community engagement and management agent for social media"""
    return Agent(
        name="Community Engagement & Management Agent",
        instructions=(
            "Actively monitor social channels and respond to comments, questions, and feedback while fostering a sense of community through discussions, contests, and user content highlights, all while managing crisis communication and reputation issues, similar to how a TikTok influencer’s review can create viral excitement for a restaurant, ultimately helping to build organic buzz."
        ),
        tools=[
            WebSearchTool()
        ],
        handoff_description="Specialist agent for community engagement and management in social media"
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
