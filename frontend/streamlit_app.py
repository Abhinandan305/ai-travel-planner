import streamlit as st
import requests
import uuid

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# -------------------------
# SESSION USER ID (FIXED)
# -------------------------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fb;
    }

    .hero {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }

    .hero p {
        font-size: 1.2rem;
        opacity: 0.9;
    }

    .trip-card {
        background: white;
        padding: 1.5rem;
        border-radius: 18px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
        margin-top: 1rem;
    }

    .stButton>button {
        width: 100%;
        background: linear-gradient(to right, #ff512f, #dd2476);
        color: white;
        border: none;
        padding: 0.8rem;
        border-radius: 12px;
        font-size: 1rem;
        font-weight: bold;
    }

    .stButton>button:hover {
        background: linear-gradient(to right, #dd2476, #ff512f);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# HERO SECTION
# -------------------------
st.markdown(
    """
    <div class="hero">
        <h1>✈️ Multi-Agent AI Travel Planner</h1>
        <p>Personalized itineraries powered by CrewAI, LangChain & Ollama</p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------
# INPUT UI
# -------------------------
col1, col2 = st.columns(2)

with col1:
    source = st.text_input("📍 Departure City", placeholder="London")
    destination = st.text_input("🌍 Destination", placeholder="Paris")
    budget = st.number_input("💰 Budget (£)", min_value=100, value=1000)

with col2:
    days = st.number_input("📅 Number of Days", min_value=1, value=3)

    travel_style = st.selectbox(
        "🎒 Travel Style",
        ["Luxury", "Budget", "Adventure", "Romantic", "Family", "Solo"]
    )

    preferences = st.text_input(
        "🍜 Interests & Preferences",
        placeholder="Food, museums, nightlife, beaches"
    )

# -------------------------
# GENERATE TRIP
# -------------------------
if st.button("Generate AI Travel Plan"):

    payload = {
        "user_id": st.session_state.user_id,
        "source": source,
        "destination": destination,
        "budget": budget,
        "days": days,
        "preferences": preferences.split(",")
    }

    with st.spinner("AI agents are planning your trip..."):

        try:
            response = requests.post(
                "http://127.0.0.1:8000/plan-trip",
                json=payload
            )

            if response.status_code == 200:

                data = response.json()

                st.markdown('<div class="trip-card">', unsafe_allow_html=True)

                st.subheader("🧳 Your AI Generated Itinerary")

                st.markdown(
                    data["itinerary"],
                    unsafe_allow_html=True
                )

                st.markdown('</div>', unsafe_allow_html=True)

                # PDF download
                with open("trip_itinerary.pdf", "rb") as file:
                    st.download_button(
                        label="📄 Download PDF Itinerary",
                        data=file,
                        file_name="trip_itinerary.pdf",
                        mime="application/pdf"
                    )

            else:
                st.error("Backend Error")
                st.text(response.text)

        except Exception as e:
            st.error(f"Application Error: {str(e)}")

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("🌎 Features")

st.sidebar.markdown("""
- Multi-Agent AI Planning
- Budget Optimization
- Personalized Recommendations
- Persistent Memory
- PDF Itinerary Export
- Local LLM with Ollama
- CrewAI + LangChain
""")

st.sidebar.success("Running Fully Local & Free")

# -------------------------
# MEMORY CONTROLS
# -------------------------
st.sidebar.title("🧠 Memory Controls")

st.sidebar.write(
    f"Session ID: {st.session_state.user_id[:8]}..."
)

if st.sidebar.button("🧹 Clear Memory"):

    res = requests.delete(
        f"http://127.0.0.1:8000/clear-memory/{st.session_state.user_id}"
    )

    if res.status_code == 200:
        st.sidebar.success("Memory cleared successfully")
    else:
        st.sidebar.error("Failed to clear memory")
