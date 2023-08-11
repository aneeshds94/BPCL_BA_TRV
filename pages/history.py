import pandas as pd
import streamlit as st

df = pd.read_csv("./history.csv")

st.subheader("Indian Oil Corporation Ltd. Trivandrum AFS")
st.subheader("List of personnel selected for BA test")
st.dataframe(df, hide_index=True, width=None)
