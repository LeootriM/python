import streamlit as st
import pandas as pd

st.header("Displaying dataframes")

df = pd.DataFrame({
    'Name' : ['Alice' , 'Michael' , 'Tony'],
    'Age' : [24 , 156 ,8],
    "City" : ["Prishtina" , "New york" , "Paris"]
})

df