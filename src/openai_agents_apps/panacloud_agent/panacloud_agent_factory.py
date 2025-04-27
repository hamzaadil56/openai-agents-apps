from agents import Agent, FileSearchTool, Runner, WebSearchTool
from typing import List
from custom_tools import search_internet
from agents import enable_verbose_stdout_logging


def create_web_developer_agent():
    """Create and return a web development specialist agent"""
    return Agent(
        name="Web Development Specialist",
        instructions=(
            "You are a Panacloud Web Development Specialist who helps with web development queries and guidance. "
            "You can assist with frontend development (HTML, CSS, JavaScript, React, Vue), "
            "backend development (Node.js, Python, PHP), and full-stack development. "
            "You can provide code examples, best practices, and debugging assistance."
        ),
        tools=[search_internet],
        handoff_description="Specialist agent for web development queries and guidance"
    )


def create_app_developer_agent():
    """Create and return a mobile app development specialist agent"""
    return Agent(
        name="App Development Specialist",
        instructions=(
            "You are an App Development Specialist who helps with mobile and desktop application development. "
            "You can assist with native app development (iOS/Swift, Android/Kotlin), "
            "cross-platform development (Flutter, React Native), and desktop applications. "
            "You can provide architecture guidance, performance optimization tips, and platform-specific best practices."
        ),
        tools=[search_internet],
        handoff_description="Specialist agent for mobile and desktop application development"
    )


def create_backend_developer_agent():
    """Create and return a backend development specialist agent"""
    return Agent(
        name="Backend Development Specialist",
        instructions=(
            "You are a Backend Development Specialist who helps with server-side development. "
            "You can assist with API development, database design, microservices architecture, "
            "and cloud infrastructure. You can provide guidance on best practices for scalability, "
            "security, and performance optimization."
        ),
        tools=[search_internet],
        handoff_description="Specialist agent for backend development and server-side architecture"
    )


def create_devops_developer_agent():
    """Create and return a DevOps specialist agent"""
    return Agent(
        name="DevOps Specialist",
        instructions=(
            "You are a DevOps Specialist who helps with deployment, automation, and infrastructure management. "
            "You can assist with CI/CD pipelines, containerization (Docker, Kubernetes), "
            "cloud services (AWS, Azure, GCP), and monitoring solutions. You can provide guidance "
            "on infrastructure as code, deployment strategies, and system reliability."
        ),
        tools=[search_internet],
        handoff_description="Specialist agent for DevOps, deployment, and infrastructure management"
    )


def create_agentic_ai_developer_agent():
    """Create and return an AI development specialist agent with backend and DevOps tools"""
    # Create backend and DevOps agents as tools
    backend_developer = create_backend_developer_agent()
    devops_developer = create_devops_developer_agent()

    return Agent(
        name="Agentic AI Development Specialist",
        instructions=(
            "You are a Panacloud Agentic AI Development Specialist who helps with AI and machine learning development. "
            "You can assist with LLM integration, agent development, AI model training, "
            "and AI application architecture. You can provide guidance on OpenAI's API, "
            "agent frameworks, and best practices for building intelligent applications. "
            "You have access to backend and DevOps specialists to help with deployment and infrastructure needs."
        ),
        tools=[
            search_internet,
            backend_developer.as_tool(
                tool_name="backend_development",
                tool_description="Get assistance with backend development and server-side architecture"
            ),
            devops_developer.as_tool(
                tool_name="devops_support",
                tool_description="Get assistance with deployment, automation, and infrastructure management"
            )
        ],
        handoff_description="Specialist agent for AI and machine learning development with backend and DevOps support"
    )


def create_panacloud_triage_agent():
    """Create and return the main Panacloud Assistant triage agent"""
    # Create all specialized agents
    web_developer = create_web_developer_agent()
    app_developer = create_app_developer_agent()
    ai_developer = create_agentic_ai_developer_agent()

    # Create the triage agent with all specialized agents as handoffs
    return Agent(
        name="Panacloud AI Assistant",
        instructions=(
            "You are the Panacloud AI Assistant, a triage agent that helps route user queries to the appropriate specialist agent. "
            "Your role is to understand the user's needs and determine which specialist agent can best help them. "
            "Available specialist agents include:\n"
            "1. Web Development Specialist - For web development queries and guidance\n"
            "2. App Development Specialist - For mobile and desktop application development\n"
            "3. Agentic AI Development Specialist - For AI and machine learning development (with backend and DevOps support)\n\n"
            "Analyze the user's query and determine which specialist agent would be most appropriate to handle their request. "
            "If the query is unclear, ask clarifying questions before making a handoff."
        ),
        tools=[search_internet],
        handoffs=[
            web_developer,
            app_developer,
            ai_developer
        ]
    )

# Example usage


async def main():
    # Enable verbose logging
    enable_verbose_stdout_logging()

    # Create the triage agent
    panacloud_assistant = create_panacloud_triage_agent()

    # Example queries to test different handoffs
    queries = [
        "I want to build a web application with React. Can you help me?",
        "How do I create a mobile app using Flutter?",
        "I need to integrate GPT-4 into my application and deploy it to AWS. Can you guide me?",
        "What's the best way to build a full-stack Agentic AI application?"
    ]

    for query in queries:
        result = await Runner.run(panacloud_assistant, query)
        print(f"\nQuery: {query}")
        print(f"Response: {result.final_output}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
