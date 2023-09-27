import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv('Fish.csv')

st.markdown("### Fish Data Graphs")

Fig1 = px.bar(df, x= 'Species', y = 'Weight', title = 'Bar plot depicting weights of different fish species')
Fig2 = px.scatter(df, color="Width", x= 'Species', y = 'Width', title = 'Scatter plot depicting Widths of different fish species')

st.plotly_chart(Fig1)
st.plotly_chart(Fig2)

st.markdown("### Detailed Data View")
st.dataframe(df)
