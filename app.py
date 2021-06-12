import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
from streamlit.proto.DataFrame_pb2 import DataFrame

from streamlit.proto.Progress_pb2 import Progress


st.sidebar.title("CovidApp")

nav = st.sidebar.radio("Navigation", ["Home", "Analysis"])
# file = st.sidebar.file_uploader("Upload file")
df = pd.read_csv('./sample.csv')


class Nav():
    df = pd.DataFrame()
    print(df)

    def loader():
       bar = st.progress(0)
       for i in range(100):
        time.sleep(0.01)
        bar.progress(i+1)
        
    def Analysis():
        Nav.loader()
        st.sidebar.subheader("Data ")
        ftype = st.sidebar.selectbox('Pick File Type', ('DataFrame', 'Graphs', 'Pie Chart'))
        st.sidebar.write(f"### {ftype}")
        if ftype == 'DataFrame':
            st.title(f"{ftype}")
            st.dataframe(df, height=500, width=2000)
        elif ftype=='Graphs':
            st.title(f"{ftype}")
            st.line_chart(df,height=500, width=500)
        elif "Pie" in ftype:
            st.title(f"{ftype}") 

    def tables():
        st.subheader("Table:")
        st.table(data=df)   

btn = False
# df = pd.read_csv('./sample.csv')

if nav == 'Home':
    df = pd.read_csv('./sample.csv')
    Nav.df = df
    st.header("Welcome world!")
    file = st.file_uploader('Pick a File')
    st.title('First App ')
    n  = st.slider('Pick A number', 0, 100)
    st.write(f'## {n}')
    date = st.date_input('Pick a Date')
    st.write(date)
    btn = st.button('Submit')
    if btn == True:
       Nav.tables()

elif nav == 'Analysis' or btn == True:
    # df = pd.read_csv('./sample.csv')
    Nav.Analysis()
    

# st.table(df)
    



