import streamlit as st
import pandas as pd

st.write('# This is my first Python web app')

st.write("## Hi, this is Pablo and I trying to create my first web application using Python!!! :sunglasses:")

sample_df = pd.DataFrame({'col1':[1,2], 'col2':[3,4]})

st.write(sample_df)

input_value = st.text_input("Enter Message")


if st.button("Display Text Message"):
    st.write(input_value)



library = st.sidebar.selectbox(
    "What is your favorite Python library?",
    ("Pandas","NumPy","Streamlit")
)

if st.sidebar.button("Display Sidebar Message"):
    st.sidebar.write(library)