
import pandas as pd
import os

# ---------------------------------------------------
# PATHS
# ---------------------------------------------------

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

# ---------------------------------------------------
# 1. CLEAN NAV HISTORY
# ---------------------------------------------------

nav = pd.read_csv(f"{RAW_PATH}/02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort values
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Forward fill NAV
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Validate NAV > 0
nav = nav[nav["nav"] > 0]

# Save cleaned file
nav.to_csv(f"{PROCESSED_PATH}/cleaned_nav_history.csv", index=False)

print("Cleaned nav_history.csv")

# ---------------------------------------------------
# 2. CLEAN INVESTOR TRANSACTIONS
# ---------------------------------------------------

txn = pd.read_csv(f"{RAW_PATH}/08_investor_transactions.csv")

# Convert date
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

# Standardize transaction types
txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.upper()
)

# Replace variations
txn["transaction_type"] = txn["transaction_type"].replace({
    "SIP": "SIP",
    "LUMPSUM": "LUMPSUM",
    "REDEMPTION": "REDEMPTION"
})

# Validate amount
txn = txn[txn["amount_inr"] > 0]

# Standardize KYC status
txn["kyc_status"] = txn["kyc_status"].str.title()

valid_kyc = ["Verified", "Pending"]

txn = txn[txn["kyc_status"].isin(valid_kyc)]

# Save cleaned file
txn.to_csv(
    f"{PROCESSED_PATH}/cleaned_investor_transactions.csv",
    index=False
)

print("Cleaned investor_transactions.csv")

# ---------------------------------------------------
# 3. CLEAN SCHEME PERFORMANCE
# ---------------------------------------------------

perf = pd.read_csv(f"{RAW_PATH}/07_scheme_performance.csv")

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

# Ensure numeric
for col in return_columns:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

# Remove invalid expense ratios
perf = perf[
    (perf["expense_ratio_pct"] >= 0.1) &
    (perf["expense_ratio_pct"] <= 2.5)
]

# Save anomalies separately
anomalies = perf[
    (perf["return_1yr_pct"] < -100) |
    (perf["return_1yr_pct"] > 200)
]

anomalies.to_csv(
    f"{PROCESSED_PATH}/performance_anomalies.csv",
    index=False
)

# Save cleaned performance file
perf.to_csv(
    f"{PROCESSED_PATH}/cleaned_scheme_performance.csv",
    index=False
)

print("Cleaned scheme_performance.csv")

# ---------------------------------------------------
# 4. COPY OTHER FILES TO PROCESSED
# ---------------------------------------------------

other_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in other_files:

    df = pd.read_csv(f"{RAW_PATH}/{file}")

    output_name = f"cleaned_{file}"

    df.to_csv(
        f"{PROCESSED_PATH}/{output_name}",
        index=False
    )

print("Other datasets copied successfully")

print("\nALL CLEANING COMPLETED")