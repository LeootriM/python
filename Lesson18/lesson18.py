import streamlit as st
import pandas as pd
import plotly.express as px

from Lesson3.lesson3 import color

st.header("Displaying dataframes")

df = pd.DataFrame({
    'Name' : ['Alice' , 'Michael' , 'Tony'],
    'Age' : [24 , 156 ,8],
    "City" : ["Prishtina" , "New york" , "Paris"]
})

st.dataframe(data)


books_df = pd.read_csv('Lesson18/test.csv')

st.title('Bestselling book analysis')
st.write('This app analyzes the Amazon top selling books')

st.subheader('Summary')
total_books = books_df.shape[0]
unique_titles = books.df['Name'].nunique()
average_rating = books_df['User rating'].mean()
average_price = books_df['Price'].mean()


col1 , col2, col3 , col4 = st.columns(4)

col1.metric("Total books" , total_books)
col2.metric("Unique titles" , unique_titles)
col3.metric("Average rating" , f"{average_rating:.2f}")
col4.metric("Average price" , f"{average_price:.2f}")


st.subheader("Preview")
st.write(books_df.head())


col1,col2 = st.columns(2)
with col1:
    st.subheader("Top 10 book titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart( top_authors)

st.subheader("Genre Distribution")
fig = px.pie(books_df, name='Genre' , title= 'Most liked Genre (2009-2022)' , color='Genre' , color_discrete_sequence=px.colors.sequential.Plasma)

st.plotly_chart(fig)