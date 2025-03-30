import chainlit as cl
from agents import Runner
from smm_agent_factory import market_research_agent
from openai_agents_apps.config import get_gemini_client, create_model, create_run_config, load_environment


@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat session"""
    # You can store your agents and configuration in the user session

    load_environment()
    client = get_gemini_client()
    model = create_model(client)
    config = create_run_config(model=model, client=client)

    cl.user_session.set("market_research_agent", market_research_agent())
    cl.user_session.set("run_config", config)

    heading_content = "Welcome to the Chatbot"

    # Create a Text element with increased font size
    heading_element = cl.Text(
        name="Social Media Marketer Agent",
        content=heading_content,
        style={"font-size": "24px", "font-weight": "bold"}
    )

    # Send a message with the heading element
    await cl.Message(elements=[heading_element], content="").send()


@cl.on_message
async def on_message(message: cl.Message):
    """Handle incoming messages"""

    market_research_agent = cl.user_session.get("market_research_agent")
    run_config = cl.user_session.get("run_config")

    # Create a Chainlit message to show typing indicator
    msg = cl.Message(content="Thinking...")
    await msg.send()

    # Run the agent
    result = await Runner.run(market_research_agent, message.content, run_config=run_config)
    response_content = result.final_output
    msg.content = response_content
    await msg.update()

    cl.user_session.set("last_result", result)
