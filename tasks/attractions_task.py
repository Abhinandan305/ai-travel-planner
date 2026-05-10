from crewai import Task
from agents.attractions_agent import attractions_agent

attractions_task = Task(

    description="""
You are a travel attractions expert.

Suggest the best attractions for the destination.

INPUTS:
Destination: {destination}
Preferences: {preferences}
Weather: {weather}
Days: {days}

STRICT RULES:
- Only suggest real attractions
- Adapt suggestions based on weather
- Avoid repetition from planning task

OUTPUT FORMAT:

# 📍 Top Attractions

## Must Visit
- Attraction 1
- Attraction 2
- Attraction 3

## Hidden Gems
- Place 1
- Place 2

## Weather-Based Suggestions
- Best indoor/outdoor options

## Timing Suggestions
- Best time to visit each place
""",

    expected_output="A structured list of attractions and recommendations.",
    agent=attractions_agent
)