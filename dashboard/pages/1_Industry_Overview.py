import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Industry Overview")

aum = pd.read_csv(
    "data/processed/cleaned_03_aum_by_fund_house.csv"
)

sip = pd.read_csv(
    "data/processed/cleaned_04_monthly_sip_inflows.csv"
)

folios = pd.read_csv(
    "data/processed/cleaned_06_industry_folio_count.csv"
)

fund_master = pd.read_csv(
    "data/processed/cleaned_01_fund_master.csv"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total AUM", "₹81 L Cr")
col2.metric("SIP Inflows", "₹31K Cr")
col3.metric("Folios", "26.12 Cr")
col4.metric("Schemes", len(fund_master))

fig = px.line(
    aum,
    x="date",
    y="aum_lakh_crore",
    color="fund_house",
    title="Industry AUM Trend"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(
    aum,
    x="fund_house",
    y="aum_lakh_crore",
    title="AUM by AMC"
)

st.plotly_chart(fig2, use_container_width=True)