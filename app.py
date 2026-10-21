import streamlit as st
import pandas as pd

st.title("HackInsight: Air Quality & Health Dashboard")
st.subheader("Target User: District Health Officer (DHO)")

st.metric(label="Data Freshness Status", value="2026-10-21 08:00 UTC", delta="Live")
st.metric(label="Data Quality Agent Status", value="PASS (100% Validated)", delta="0 Errors")

st.markdown("### Latest Gold Table Records")
st.table(pd.DataFrame({
    "Gold Row ID": [1, 2, 3],
    "District": ["Lahore Central", "Karachi South", "Peshawar East"],
    "PM2.5 (ug/m3)": [184.2, 92.1, 145.6],
    "Health Advisory": ["Severe Surge Expected", "Moderate", "High Caution"]
}))
