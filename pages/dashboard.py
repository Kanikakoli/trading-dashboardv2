import streamlit as st

st.title("Dashboard")
st.markdown("Welcome to the Dashboard page.")
st.metric("Market Bias", "Neutral")

# Example small visualization
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "time": ["09:15","10:00","11:00","12:00"],
    "price": [100, 102, 101, 103]
})
fig = px.line(df, x="time", y="price", title="Sample Price")
st.plotly_chart(fig, use_container_width=True)
