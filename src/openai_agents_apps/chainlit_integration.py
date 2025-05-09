import chainlit as cl
from agents import Runner, set_default_openai_api, set_default_openai_client, set_tracing_disabled
from agent_factory import create_math_tutor, create_history_tutor, create_triage_agent, web_search_agent
from config import get_gemini_client, create_model, create_run_config
from config import load_environment


@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat session"""
    # You can store your agents and configuration in the user session
    load_environment()
    client = get_gemini_client()
    model = create_model(client)
    set_default_openai_client(client=client, use_for_tracing=False)
    # set_default_openai_api("chat_completions")
    # set_tracing_disabled(disabled=True)
    cl.user_session.set("model", model)

    cl.user_session.set("config", create_run_config(model, client))
    cl.user_session.set("triage_agent", create_triage_agent(
        [create_math_tutor(), create_history_tutor(), web_search_agent(model=model)]))


@cl.on_message
async def on_message(message: cl.Message):
    """Handle incoming messages"""
    config = cl.user_session.get("config")
    model = cl.user_session.get("model")
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
