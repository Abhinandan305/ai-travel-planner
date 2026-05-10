from crewai import Agent
from llm import llm

attractions_agent = Agent(

    role="Local Attractions Expert",

    goal="""
    Recommend attractions
    and activities.
    """,

    backstory="""
    Local tourism specialist.
    """,

    llm=llm,

    verbose=True
)