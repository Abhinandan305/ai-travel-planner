from crewai import Agent
from llm import llm

planner_agent = Agent(

    role="Travel Planner",

    goal="""
    Create detailed personalized
    travel itineraries.
    """,

    backstory="""
    Expert travel planner with years
    of tourism experience.
    """,

    llm=llm,

    verbose=True
)