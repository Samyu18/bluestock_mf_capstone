import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Fund Performance")

performance = pd.read_csv(
    "reports/fund_scorecard.csv"
)

fig = px.scatter(
    performance,
    x="return_3yr_pct",
    y="sharpe_ratio",
    size="score",
    hover_data=["amfi_code"],
    title="Return vs Risk"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Fund Scorecard")

st.dataframe(
    performance.sort_values(
        "score",
        ascending=False
    )
)