🧳 AI Travel Itinerary Planner (Multi-Agent AI System)

An AI-powered travel planner that generates personalized multi-day itineraries using a multi-agent architecture. Built with CrewAI, FastAPI, Streamlit, and deployed on AWS EC2.

🚀 Live Features
✈️ AI-generated multi-day travel itineraries
💰 Budget-aware planning
🌍 Destination-based recommendations
🍜 Preference-based customization (food, travel style, interests)
🧠 Memory system for returning users
🌦 Weather-aware suggestions (optional integration)
📄 Downloadable PDF itinerary
☁️ Cloud deployment on AWS EC2

🧠 System Architecture

                        ┌────────────────────┐
                        │   Streamlit UI     │
                        │  (Frontend Layer)  │
                        └─────────┬──────────┘
                                  │ REST API
                                  ▼
                        ┌────────────────────┐
                        │   FastAPI Backend  │
                        │  /plan-trip API    │
                        └─────────┬──────────┘
                                  │
                                  ▼
        ┌────────────────────────────────────────────┐
        │           CrewAI Multi-Agent System        │
        │                                            │
        │  ┌──────────────┐   ┌──────────────────┐   │
        │  │ Planner Agent │   │ Budget Agent     │   │
        │  └──────┬───────┘   └────────┬─────────┘   │
        │         │                     │             │
        │         ▼                     ▼             │
        │  ┌──────────────────────────────────────┐   │
        │  │ Attractions Agent                    │   │
        │  └──────────────────────────────────────┘   │
        └───────────────┬────────────────────────────┘
                        │
                        ▼
        ┌────────────────────────────────────┐
        │ Memory Layer (ChromaDB / Storage)  │
        └────────────────────────────────────┘
                        │
                        ▼
        ┌────────────────────────────────────┐
        │ LLM (Ollama / OpenAI / Local LLM)  │
        └────────────────────────────────────┘
🏗️ Tech Stack
Backend: FastAPI, Python
Frontend: Streamlit
AI Framework: CrewAI, LangChain
Memory: ChromaDB (vector storage)
LLM: Ollama / OpenAI (configurable)
Cloud: AWS EC2 (Ubuntu)
Other: REST APIs, PDF generation, Linux server setup

⚙️ Installation
1. Clone repository
git clone https://github.com/your-username/ai-travel-planner.git
cd ai-travel-planner
2. Create virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
4. Run FastAPI backend
uvicorn api.main:app --host 0.0.0.0 --port 8000
5. Run Streamlit frontend
streamlit run frontend/streamlit_app.py
☁️ AWS Deployment (EC2)
Deployed on Ubuntu EC2 instance (t3.micro)
Configured security groups:
HTTP: 80
HTTPS: 443
API: 8000
Backend runs using:
uvicorn api.main:app --host 0.0.0.0 --port 8000

🧩 Key Challenges Solved
Fixed Python environment conflicts (3.13 → 3.11 migration)
Resolved AI dependency issues (CrewAI, LangChain, ChromaDB)
Managed EC2 disk and memory limitations
Handled REST communication between frontend and backend
Debugged multi-agent workflow execution issues

📸 Example Output
Day-wise itinerary generation
Budget breakdown per activity
Travel route optimization
Food and attraction recommendations

🔮 Future Improvements
Real-time flight & hotel API integration
Map-based itinerary visualization
Dockerized deployment
User authentication system
Mobile app version
