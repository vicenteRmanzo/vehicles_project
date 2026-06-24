import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.header("Dashboard de Vehículos")

hist_button = st.button("Construir histograma")

if hist_button:
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)

scatter_button = st.button("Construir dispersión")

if scatter_button:
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig)
