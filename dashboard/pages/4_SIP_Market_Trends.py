import streamlit as st
import pandas as pd
import plotly.express as px

st.title("SIP & Market Trends")

sip = pd.read_csv(
    "data/processed/cleaned_04_monthly_sip_inflows.csv"
)

fig = px.line(
    sip,
    x="month",
    y="sip_inflow_crore",
    title="SIP Inflows"
)

st.plotly_chart(fig, use_container_width=True)

category = pd.read_csv(
    "data/processed/cleaned_05_category_inflows.csv"
)

top5 = (
    category.groupby("category")
    ["net_inflow_crore"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

fig2 = px.bar(
    top5,
    x="category",
    y="net_inflow_crore",
    title="Top 5 Categories"
)

st.plotly_chart(fig2, use_container_width=True)