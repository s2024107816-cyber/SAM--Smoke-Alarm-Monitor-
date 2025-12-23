import streamlit as st
import pandas as pd
import time
import requests # Used to send notifications

# --- SETTINGS ---
# Replace with a real data source (e.g., a Google Sheet or Database API)
# For now, it simulates the Arduino data
THRESHOLD = 400 

st.set_page_config(page_title="SAM the Smoke and Alarm Monitor", page_icon="🔥")

# Custom CSS to make it feel like a native app
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🏠 SAM Monitoring")

# UI Layout
smoke_val = st.number_input("Current Sensor Data (Simulation)", value=350)
st.metric(label="Smoke Concentration", value=f"{smoke_val} ppm", delta=f"{smoke_val - 300}")

if smoke_val > THRESHOLD:
    st.error("🚨 ALERT: SMOKE DETECTED IN KITCHEN!")
    # Optional: Send a real push notification to your phone using ntfy.sh
    # requests.post("https://ntfy.sh/YourUniqueTopic", data="Fire Alert! Check your home immediately.")
else:
    st.success("✅ Air Quality: Clear")

st.subheader("Historical Trends")
# Logic to display a chart of recent data
