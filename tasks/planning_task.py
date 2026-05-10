from crewai import Task
from agents.planner_agent import planner_agent

planning_task = Task(

    description="""
You are a professional AI travel planner.

You MUST generate a complete multi-day itinerary.

STRICT RULES:
- Generate ALL days from Day 1 to Day {days}
- Do NOT skip any day
- Do NOT ignore weather input
- Weather MUST influence every day's plan
- Do NOT invent data not provided

INPUTS:
Source: {source}
Destination: {destination}
Budget: {budget}
Days: {days}
Preferences: {preferences}
Weather: {weather}
Memory: {memory}

OUTPUT FORMAT (MANDATORY FOR EACH DAY):

# 🧳 Day X - {destination}

## 🌤 Weather (MANDATORY)
- Current weather: {weather}
- How it affects today's plan
- Indoor/outdoor adjustment strategy

## 🚇 Transport
- Travel plan for the day

## 📍 Activities
- Activity 1
- Activity 2
- Activity 3

## 🍽 Food
- Budget-friendly food suggestions

## 💰 Budget Estimate
- Breakdown

## 🧠 Personalization
- Based on memory (if available)

RULES:
- Weather section MUST appear in EVERY day
- Do NOT skip weather under any condition
- Do NOT output generic content
""",

    expected_output="""
A structured multi-day itinerary where each day includes weather-aware planning.
""",

    agent=planner_agent
)