# ```python
import pandas as pd

scorecard = pd.read_csv(
    "reports/fund_scorecard.csv"
)

fund_master = pd.read_csv(
    "data/processed/cleaned_01_fund_master.csv"
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

df = scorecard.merge(
    fund_master[
        ["amfi_code",
         "scheme_name",
         "risk_category"]
    ],
    on="amfi_code"
)

recommendations = (
    df[
        df["risk_category"]
        .str.lower()
        ==
        risk.lower()
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(
    recommendations[
        [
            "scheme_name",
            "risk_category",
            "sharpe_ratio"
        ]
    ]
)

