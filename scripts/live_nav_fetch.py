import requests
import pandas as pd
import os

# Output folder
OUTPUT_PATH = "data/raw"

# AMFI Scheme Codes
scheme_codes = {
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Create folder if not exists
os.makedirs(OUTPUT_PATH, exist_ok=True)

# Fetch NAV data
for scheme_name, scheme_code in scheme_codes.items():

    print("\n" + "=" * 60)
    print(f"Fetching: {scheme_name}")
    print("=" * 60)

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            # Scheme details
            print("\nSCHEME DETAILS:")
            print(data.get("meta", {}))

            # NAV history
            nav_df = pd.DataFrame(data["data"])

            # Save CSV
            file_name = f"{scheme_name}_nav.csv"

            save_path = os.path.join(OUTPUT_PATH, file_name)

            nav_df.to_csv(save_path, index=False)

            print(f"\nSaved File: {file_name}")

            print("\nFIRST 5 ROWS:")
            print(nav_df.head())

        else:
            print(f"Failed with status code: {response.status_code}")

    except Exception as e:
        print(f"Error fetching {scheme_name}: {e}")