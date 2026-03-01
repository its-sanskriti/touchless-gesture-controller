import logging
from dotenv import load_dotenv
from vision_agents.plugins import getstream, gemini
from vision_agents.core import Agent, User, Runner
from vision_agents.core.agents import AgentLauncher

load_dotenv()

logger = logging.getLogger(__name__)


async def create_agent(**kwargs):
    print("Creating Touchless Gesture Controller...")

    agent = Agent(
        edge=getstream.Edge(),
        agent_user=User(name="Gesture Controller AI"),

        # ⭐ UPGRADED INSTRUCTIONS
        instructions="""
You are an AI Touchless Gesture Controller.

Observe the user's hand gestures from the camera feed
and convert them into system commands.

Rules:
- Thumbs up → say "Command Accepted"
- Open palm → say "Paused"
- Victory sign → say "Next Action"
- Closed fist → say "Stopping System"

Always clearly announce the detected command.
""",

        llm=gemini.Realtime(fps=1)
    )

    return agent


async def join_call(agent, call_type, call_id, **kwargs):
    print("✅ Agent joined call and ready for gesture control")


if __name__ == "__main__":
    Runner(
        AgentLauncher(
            create_agent=create_agent,
            join_call=join_call
        )
    ).cli()