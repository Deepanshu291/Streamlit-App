import streamlit as st
import pandas as pd
import numpy  as np

st.write("""
# welcome to Streamlit App
Here is *data!*
This is My First App
""")

dt = pd.read_csv("./sample.csv")
# st.altair_chart(dt)
st.line_chart(dt)
st.date_input("Pick a *Date*")