import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Investor Analytics")

txn = pd.read_csv(
    "data/processed/cleaned_investor_transactions.csv"
)

state_data = (
    txn.groupby("state")["amount_inr"]
    .sum()
    .reset_index()
)

fig = px.bar(
    state_data,
    x="state",
    y="amount_inr",
    title="Transaction Amount by State"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.pie(
    txn,
    names="transaction_type",
    title="Transaction Split"
)

st.plotly_chart(fig2, use_container_width=True)

age_data = (
    txn.groupby("age_group")["amount_inr"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    age_data,
    x="age_group",
    y="amount_inr",
    title="Average Investment by Age Group"
)

st.plotly_chart(fig3, use_container_width=True)