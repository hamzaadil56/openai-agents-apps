import chainlit as cl
from agents import Runner


@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat session"""
    # You can store your agents and configuration in the user session
    cl.user_session.set("config", cl.user_session.get("run_config"))


@cl.on_message
async def on_message(message):
    """Handle incoming messages"""
    config = cl.user_session.get("config")
    triage_agent = cl.user_session.get("triage_agent")

    # Create a Chainlit message to show typing indicator
    msg = cl.Message(content="", author="Agent")
    await msg.send()

    # Run the agent
    result = await Runner.run(triage_agent, message.content, run_config=config)

    # Update the message with the result
    await msg.update(content=result.final_output)

    # Optionally store conversation history or other state
    cl.user_session.set("last_result", result)
