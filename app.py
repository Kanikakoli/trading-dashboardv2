import streamlit as st

st.set_page_config(page_title="Trading Dashboard V2", layout="wide")

st.title("Trading Dashboard V2")
st.write("New project started successfully.")

module = st.radio(
    "Select Module",
    ["Dashboard", "F&O", "Scalping", "Intraday", "BTST", "Hero Zero"],
    horizontal=True
)

if module == "Dashboard":
    st.subheader("Dashboard")
    st.metric("Market Bias", "Neutral")
elif module == "F&O":
    st.subheader("F&O")
elif module == "Scalping":
    st.subheader("Scalping")
elif module == "Intraday":
    st.subheader("Intraday")
elif module == "BTST":
    st.subheader("BTST")
elif module == "Hero Zero":
    st.subheader("Hero Zero")
    st.warning("High-risk module. Use strict risk controls.")
