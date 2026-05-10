from crewai import LLM

llm = LLM(
    model="ollama/phi3",
    base_url="http://localhost:11434"
)