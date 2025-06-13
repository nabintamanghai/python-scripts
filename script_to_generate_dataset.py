import pandas as pd             
import random                   
from faker import Faker       
import numpy as np

# Initialize Faker instance
fake = Faker()

# Define lists of possible values for campaigns
channels = ['Facebook', 'Google Ads', 'Instagram', 'LinkedIn', 'Twitter']          # Marketing platforms
regions = ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia']  # Geographical regions
campaign_names = ['Summer Sale', 'Winter Blast', 'Spring Promo', 'Autumn Deals', 'Mega Campaign']  # Campaign titles

# Initialize an empty list to store generated data
data = []

# Loop to generate 5000 records
for i in range(1, 5001):
    campaign_id = i  # Unique campaign ID
    campaign_name = random.choice(campaign_names)  # Random campaign name
    channel = random.choice(channels)              # Random marketing channel
    region = random.choice(regions)                # Random region
    impressions = random.randint(1000, 500000)     # Number of times the ad was shown
    clicks = random.randint(50, min(5000, impressions))  # Number of clicks, must be <= impressions
    conversions = random.randint(5, min(500, clicks))    # Number of successful outcomes, <= clicks
    cost = round(random.uniform(100, 5000), 2)           # Cost of campaign
    revenue = round(cost + random.uniform(50, 10000), 2) # Revenue earned
    start_date = fake.date_between(start_date='-1y', end_date='-1m')  # Campaign start date
    end_date = start_date + pd.Timedelta(days=random.randint(3, 15))  # Campaign end date (3–15 days later)
    
    # Append the generated row of data
    data.append([
        campaign_id, campaign_name, channel, region, impressions, clicks,
        conversions, cost, revenue, start_date, end_date
    ])

# Define column names for the dataset
columns = ['campaign_id', 'campaign_name', 'channel', 'region', 'impressions', 'clicks', 'conversions', 'cost', 'revenue', 'start_date', 'end_date']

# Create a pandas DataFrame from the list of data
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame as a CSV file
file_path = "C:\\Users\\aakash\\OneDrive\\Desktop\\Data analysis\\marketing_campaign_data.csv"
df.to_csv(file_path, index=False)  # Export the dataset without row indices
