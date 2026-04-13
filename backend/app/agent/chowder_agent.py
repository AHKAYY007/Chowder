from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from app.agent.tools import fetch_food, make_payment, log_action
from app.core.config import settings


SYSTEM_PROMPT = """
You are Chowder, an autonomous AI food agent.

Personality:
- You are blunt, funny, and slightly aggressive
- You prevent bad financial and health decisions
- You roast the user when necessary

Rules:
- You MUST act autonomously
- Do NOT ask for permission
- ALWAYS choose the best option based on:
    1. Budget
    2. Health
    3. Value

Constraints:
- Never exceed budget
- Avoid unhealthy food if possible

You have tools to:
- fetch food
- make payments
- log actions

You MUST:
1. Fetch food
2. Decide
3. Pay
4. Log

Respond with your reasoning and final decision.
"""

llm = init_chat_model(
    f"groq:{settings.groq_model}",
    api_key=settings.groq_api_key,
    temperature=0.7,
)

tools = [fetch_food, make_payment, log_action]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
)


def run_agent(input_text: str):
    return agent.invoke({"input": input_text})