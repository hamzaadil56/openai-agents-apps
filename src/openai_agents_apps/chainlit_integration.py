import chainlit as cl
from agents import Runner
from agent_factory import create_math_tutor, create_history_tutor, create_triage_agent, web_search_agent
from config import get_gemini_client, create_model, create_run_config


@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat session"""
    # You can store your agents and configuration in the user session
    client = get_gemini_client()
    model = create_model(client)
    cl.user_session.set("config", create_run_config(model, client))
    cl.user_session.set("triage_agent", create_triage_agent(
        [create_math_tutor(), create_history_tutor(), web_search_agent()]))


@cl.on_message
async def on_message(message: cl.Message):
    """Handle incoming messages"""
    config = cl.user_session.get("config")
    triage_agent = cl.user_session.get("triage_agent")

    # Create a Chainlit message to show typing indicator
    msg = cl.Message(content="Thinking...")
    await msg.send()

    # Run the agent
    result = await Runner.run(triage_agent, message.content, run_config=config)
    response_content = result.final_output
    msg.content = response_content
    await msg.update()

    # Update the message with the result
    # await cl.Message(content=result.final_output).send()

    # Optionally store conversation history or other state
    cl.user_session.set("last_result", result)
