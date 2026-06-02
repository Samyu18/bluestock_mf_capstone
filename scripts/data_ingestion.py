import os
import pandas as pd

# -----------------------------------------
# PATH TO RAW DATA
# -----------------------------------------

RAW_DATA_PATH = "data/raw"

# -----------------------------------------
# GET ALL CSV FILES
# -----------------------------------------

csv_files = [f for f in os.listdir(RAW_DATA_PATH) if f.endswith(".csv")]

print("\n" + "=" * 70)
print(f"TOTAL CSV FILES FOUND: {len(csv_files)}")
print("=" * 70)

# Dictionary to store datasets
datasets = {}

# -----------------------------------------
# LOAD ALL CSV FILES
# -----------------------------------------

for file in csv_files:

    file_path = os.path.join(RAW_DATA_PATH, file)

    try:

        df = pd.read_csv(file_path)

        datasets[file] = df

        print("\n" + "=" * 70)
        print(f"DATASET: {file}")
        print("=" * 70)

        # SHAPE
        print("\nSHAPE:")
        print(df.shape)

        # DATA TYPES
        print("\nDATA TYPES:")
        print(df.dtypes)

        # FIRST 5 ROWS
        print("\nFIRST 5 ROWS:")
        print(df.head())

        # MISSING VALUES
        print("\nMISSING VALUES:")
        print(df.isnull().sum())

        # DUPLICATES
        print("\nDUPLICATE ROWS:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"\nERROR READING {file}: {e}")

# -----------------------------------------
# FUND MASTER EXPLORATION
# -----------------------------------------

fund_master_file = "01_fund_master.csv"

if fund_master_file in datasets:

    fund_master = datasets[fund_master_file]

    print("\n" + "=" * 70)
    print("FUND MASTER EXPLORATION")
    print("=" * 70)

    # PRINT COLUMN NAMES
    print("\nCOLUMNS:")
    print(fund_master.columns)

    # CHECK POSSIBLE COLUMNS
    possible_columns = [
        "fund_house",
        "category",
        "subcategory",
        "sub_category",
        "risk_grade",
        "risk"
    ]

    for col in possible_columns:

        if col in fund_master.columns:

            print("\n" + "-" * 50)
            print(f"UNIQUE VALUES IN: {col.upper()}")
            print("-" * 50)

            print(fund_master[col].unique())


# -----------------------------------------
# AMFI CODE VALIDATION
# -----------------------------------------

nav_history_file = "02_nav_history.csv"

if fund_master_file in datasets and nav_history_file in datasets:

    fund_master = datasets[fund_master_file]
    nav_history = datasets[nav_history_file]

    # Your datasets use 'amfi_code'
    master_codes = set(
        fund_master["amfi_code"].dropna()
    )

    nav_codes = set(
        nav_history["amfi_code"].dropna()
    )

    missing_codes = master_codes - nav_codes

    print("\n" + "=" * 70)
    print("AMFI CODE VALIDATION")
    print("=" * 70)

    print(f"\nTOTAL FUND MASTER CODES: {len(master_codes)}")
    print(f"TOTAL NAV HISTORY CODES: {len(nav_codes)}")
    print(f"MISSING CODES: {len(missing_codes)}")

    if len(missing_codes) > 0:

        print("\nSAMPLE MISSING CODES:")
        print(list(missing_codes)[:20])

    else:

        print("\nSUCCESS: ALL AMFI CODES MATCH!")

