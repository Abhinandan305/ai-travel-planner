from crewai import Agent
from llm import llm

budget_agent = Agent(

    role="Budget Optimizer",

    goal="""
    Optimize travel spending.
    """,

    backstory="""
    Expert in travel budgeting.
    """,

    llm=llm,

    verbose=True
)