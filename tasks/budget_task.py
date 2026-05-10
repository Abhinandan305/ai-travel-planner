from crewai import Task
from agents.budget_agent import budget_agent

budget_task = Task(

    description="""
You are a budget optimization expert for travel planning.

Analyze the trip and optimize spending.

INPUTS:
Destination: {destination}
Budget: {budget}
Days: {days}
Preferences: {preferences}

STRICT RULES:
- Stay within budget
- Suggest cheaper alternatives where possible
- Do NOT invent new variables
- No unnecessary text

OUTPUT FORMAT:

# 💰 Budget Optimization

## Daily Budget Allocation
- Accommodation:
- Food:
- Transport:
- Activities:

## Cost Saving Suggestions
- Tip 1
- Tip 2
- Tip 3

## Final Recommendation
- Summary of optimized plan
""",

    expected_output="A structured budget breakdown and optimization plan.",
    agent=budget_agent
)