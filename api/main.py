from fastapi import FastAPI
from pydantic import BaseModel

from crewai import Crew

from agents.planner_agent import planner_agent
from agents.budget_agent import budget_agent
from agents.attractions_agent import attractions_agent

from tasks.planning_task import planning_task
from tasks.budget_task import budget_task
from tasks.attractions_task import attractions_task

from memory.chroma_store import (
    save_memory,
    retrieve_memory,
    clear_memory
)

from pdf.pdf_generator import generate_pdf

from tools.weather_tool import get_weather

app = FastAPI()

# -----------------------------------
# REQUEST MODEL
# -----------------------------------
class TripRequest(BaseModel):

    user_id: str
    source: str
    destination: str
    budget: int
    days: int
    preferences: list

# -----------------------------------
# PLAN TRIP API
# -----------------------------------
@app.post("/plan-trip")
def plan_trip(data: TripRequest):

    # -----------------------------
    # MEMORY CONTEXT
    # -----------------------------
    memory_context = ""

    if data.user_id:

        previous_memory = retrieve_memory(
            data.user_id
        )

        memory_context = "\n".join(
            previous_memory
        )

    # -----------------------------
    # WEATHER DATA
    # -----------------------------
    weather_data = get_weather(
        data.destination
    )

    weather_summary = "Unknown"

    if weather_data.get("weather"):

        weather_summary = weather_data[
            "weather"
        ][0]["description"]

    # -----------------------------
    # CREATE CREW
    # -----------------------------
    crew = Crew(

        agents=[
            planner_agent,
            budget_agent,
            attractions_agent
        ],

        tasks=[
            planning_task,
            budget_task,
            attractions_task
        ],

        verbose=True
    )

    # -----------------------------
    # RUN CREW
    # -----------------------------
    result = crew.kickoff(

        inputs={

            "source": data.source,
            "destination": data.destination,
            "budget": data.budget,
            "days": data.days,
            "preferences": data.preferences,
            "memory": memory_context,
            "weather": weather_summary
        }
    )

    # -----------------------------
    # SAVE MEMORY
    # -----------------------------
    if data.user_id:

        save_memory(

            data.user_id,

            f"""
            Destination: {data.destination}
            Preferences: {data.preferences}
            Budget: {data.budget}
            Days: {data.days}
            Weather: {weather_summary}
            """
        )

    # -----------------------------
    # GENERATE PDF
    # -----------------------------
    generate_pdf(str(result))

    # -----------------------------
    # RETURN RESPONSE
    # -----------------------------
    return {

        "itinerary": str(result),

        "weather": weather_summary,

        "memory_used": bool(data.user_id)
    }

# -----------------------------------
# CLEAR MEMORY API
# -----------------------------------
@app.delete("/clear-memory/{user_id}")
def delete_memory(user_id: str):

    clear_memory(user_id)

    return {
        "message": f"Memory cleared for {user_id}"
    }

# -----------------------------------
# HEALTH CHECK
# -----------------------------------
@app.get("/")
def health_check():

    return {
        "status": "running",
        "service": "Multi-Agent AI Travel Planner"
    }