# ```python
import pandas as pd
import os
from sqlalchemy import create_engine

# ---------------------------------------------------
# DATABASE CONNECTION
# ---------------------------------------------------

engine = create_engine("sqlite:///bluestock_mf.db")

PROCESSED_PATH = "data/processed"

# ---------------------------------------------------
# LOAD ALL CLEANED FILES
# ---------------------------------------------------

files = os.listdir(PROCESSED_PATH)

for file in files:

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "")

        path = os.path.join(PROCESSED_PATH, file)

        df = pd.read_csv(path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded {file} -> {table_name}")

        print(f"Rows: {len(df)}")

print("\nALL DATA LOADED TO SQLITE")
# ```
