"""
Master Pipeline Runner
Bluestock MF Capstone
"""

import os

print("Running Data Ingestion...")
os.system("python scripts/data_ingestion.py")

print("Running Live NAV Fetch...")
os.system("python scripts/live_nav_fetch.py")

print("Pipeline Completed Successfully")