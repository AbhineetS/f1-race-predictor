import streamlit as st
import requests

# Page Detailings
st.set_page_config(
    page_title="F1 Race Predictor",
    page_icon="🏎️",
    layout="wide",
)

# URL setup for FastAPI (backend)
BACKEND_URL = "http://127.0.0.1:8000"

st.title(" 🏁 F1 Race Predictor 🏁")
st.markdown("*Powered by your FastAPI backend & OpenF1 API Data*")
st.markdown("---")

# This is the Input Interface
col1, col2 = st.columns(2)

with col1:
    st.subheader("📍 Session Lookup")
    
    # Select Filters
    country = st.text_input("Enter Country (e.g., India, Bahrain, Monaco, Great Britain)", value="Bahrain")
    year = st.number_input("Enter Year", min_value=2023, max_value=2026, value=2024, step=1)
    
    # Button to pull actual data from your FastAPI backend
    fetch_sessions = st.button("Predict 🔍: ", use_container_width=True)

with col2:
    st.subheader("👥 The Live Grid")
    # I have added only a few names that I kew you can add more.
    driver_1 = st.selectbox("Driver 1", ["Max Verstappen", "Lando Norris", "Charles Leclerc", "Lewis Hamilton"])
    driver_2 = st.selectbox("Driver 2 (Rival)", ["Oscar Piastri", "George Russell", "Carlos Sainz", "Sergio Perez"])

st.markdown("---")

# Backend Communications
if fetch_sessions:
    with st.spinner("Talking to FastAPI backend..."):
        try:
            # Hitting your exact @app.get("/sessions") endpoint with parameters
            response = requests.get(
                f"{BACKEND_URL}/sessions", 
                params={"country": country, "year": year}
            )
            
            if response.status_code == 200:
                sessions_data = response.json()
                
                if sessions_data:
                    st.success(f"Found {len(sessions_data)} sessions for {country} ({year})!")
                    
                
               # pandas is imported to display the backend data in a table format.
                    import pandas as pd
                    
                    # Session data is a list instead of a dictionary
                    if isinstance(sessions_data, dict):
                        sessions_data = [sessions_data]
                        
                    df = pd.DataFrame(sessions_data)
                    
                    columns_to_show = {
                        "session_name": "Session Name",
                        "session_type": "Type",
                        "circuit_short_name": "Circuit",
                        "location": "Location",
                        "date_start": "Start Time (GMT)"
                    }
                    
                    available_cols = [col for col in columns_to_show.keys() if col in df.columns]
                    df_clean = df[available_cols].rename(columns={k: v for k, v in columns_to_show.items() if k in available_cols})
                    
                    if "Start Time (GMT)" in df_clean.columns:
                        df_clean["Start Time (GMT)"] = pd.to_datetime(df_clean["Start Time (GMT)"]).dt.strftime('%Y-%m-%d %H:%M')
                    
                    # Display System
                    st.subheader("🏁 Weekend Schedule & Track Info")
                    st.dataframe(df_clean, use_container_width=True, hide_index=True)
                else:
                    st.warning("⚠️ No sessions found matching those filters. Check your spelling or capitalization!")
            else:
                # If there is an error in the backend itself. This error handler will get triggered.
                st.error(f"❌ Backend returned an error status: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            # This error handler will get triggered when backend is not configured properly with the frontend.
            st.error(" ⚠️ Connection Refused! Is your FastAPI backend server running right now?")