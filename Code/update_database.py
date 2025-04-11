from supabase import create_client
import pandas as pd
import os
from dotenv import load_dotenv

# Config
url = "https://gpoalwnhuvofvjtphlof.supabase.co"
load_dotenv()
key = os.getenv("anon_id")
supabase = create_client(url, key)

# Load and upload
cases_df = pd.read_csv("customer_satisfaction_cases.csv")
events_df = pd.read_csv("customer_satisfaction_events.csv")

# Upload to Supabase
for _, row in cases_df.iterrows():
    result = supabase.table("Customer_Satisfaction_Cases").insert(row.to_dict()).execute()
    print("Data:", result.data)
    print("Error:", result.error)

for _, row in events_df.iterrows():
    result = supabase.table("Customer_Satisfaction_Events").insert(row.to_dict()).execute()
    print("Data:", result.data)
    print("Error:", result.error)
