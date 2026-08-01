import streamlit as st

st.title("F&O")
st.write("Futures & Options tools go here.")
# placeholder control
ticker = st.text_input("Ticker", "NIFTY")
st.write("Selected:", ticker)
