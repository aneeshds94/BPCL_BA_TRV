import streamlit as st
import functions as func

names = func.get_names()
st.subheader("Indian Oil Corporation Ltd. Trivandrum AFS")
st.subheader("BA Random Generator Tool")
st.text("Select Shift: ")
for shift in ['A', 'B', 'C']:
    st.checkbox(shift)

st.text("Select employees available in shift from list below: ")
for name in names:
    checkbox = st.checkbox(name)

st.button("Generate")