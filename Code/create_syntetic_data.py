from faker import Faker
import random
import pandas as pd
from datetime import timedelta

fake = Faker()

categories = ["Billing", "Technical", "General Inquiry"]
severities = ["Low", "Medium", "High"]
statuses = ["Resolved", "Pending", "Escalated"]
channels = ["Email", "Chat", "Phone"]
activities = ["Ticket Opened", "Investigating", "Resolved"]

cases = []
events = []

for i in range(1, 201):
    issue_category = random.choice(categories)
    issue_severity = random.choice(severities)
    resolution_status = random.choice(statuses)
    satisfaction_score = random.randint(1, 10)
    
    cases.append({
        "case_id": i,
        "customer_id": random.randint(1000, 2000),
        "issue_category": issue_category,
        "issue_severity": issue_severity,
        "resolution_status": resolution_status,
        "customer_feedback": fake.sentence(),
        "satisfaction_score": satisfaction_score
    })
    
    base_time = fake.date_time_this_year()
    for j in range(random.randint(2, 4)):
        activity = random.choice(activities)
        sentiment = round(random.uniform(-1, 1), 2)
        events.append({
            "case_id": i,
            "activity": activity,
            "timestamp": base_time + timedelta(minutes=15*j),
            "actor": fake.name(),
            "channel": random.choice(channels),
            "sentiment_score": sentiment,
            "resolution_time": random.randint(5, 180)
        })

pd.DataFrame(cases).to_csv("customer_satisfaction_cases.csv", index=False)
pd.DataFrame(events).to_csv("customer_satisfaction_events.csv", index=False)
