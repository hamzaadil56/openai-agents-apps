import chainlit as cl
from agents import Runner, set_default_openai_api, set_default_openai_client, set_tracing_disabled
from smm_agent_factory import market_research_agent, strategic_planning_kpi_agent, content_creation_curation_agent, community_engagement_management_agent, create_triage_agent


@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat session"""
    # You can store your agents and configuration in the user session

    cl.user_session.set("triage_agent", create_triage_agent(
        [market_research_agent(), strategic_planning_kpi_agent(), content_creation_curation_agent()]))

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

    triage_agent = cl.user_session.get("triage_agent")

    # Create a Chainlit message to show typing indicator
    msg = cl.Message(content="Thinking...")
    await msg.send()

    # Run the agent
    result = await Runner.run(triage_agent, message.content)
    response_content = result.final_output
    msg.content = response_content
    await msg.update()

    # Update the message with the result
    # await cl.Message(content=result.final_output).send()

    # Optionally store conversation history or other state
    cl.user_session.set("last_result", result)
