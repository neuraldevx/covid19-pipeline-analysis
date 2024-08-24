import os
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

# Connect to the database
engine = create_engine(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

# Load data into a pandas DataFrame
df = pd.read_sql_table('covid19_confirmed_cases', engine)

# Convert 'Date' to datetime if it's not already
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the index
df.set_index('Date', inplace=True)

# Analysis 1: Global trend of new cases
global_new_cases = df.groupby('Date')['NewCases'].sum()
plt.figure(figsize=(12, 6))
global_new_cases.plot(title='Global Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.savefig('global_new_cases.png')
plt.close()

# Analysis 2: Top 10 countries by total cases
top_countries = df.groupby('Country/Region')['Confirmed'].max().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_countries.plot(kind='bar', title='Top 10 Countries by Total COVID-19 Cases')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_10_countries.png')
plt.close()

# Analysis 3: Daily new cases for a specific country (e.g., United States)
us_data = df[df['Country/Region'] == 'US']['NewCases']
plt.figure(figsize=(12, 6))
us_data.plot(title='Daily New COVID-19 Cases in the United States')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.savefig('us_new_cases.png')
plt.close()

# Analysis 4: Rolling average of new cases
df['7_day_avg'] = df.groupby('Country/Region')['NewCases'].rolling(window=7).mean().reset_index(0, drop=True)

plt.figure(figsize=(12, 6))
df[df['Country/Region'] == 'US']['7_day_avg'].plot(title='7-Day Rolling Average of New COVID-19 Cases in the US')
plt.xlabel('Date')
plt.ylabel('7-Day Average of New Cases')
plt.savefig('us_7day_avg.png')
plt.close()

# Analysis 5: Case fatality rate (requires death data)
death_df = pd.read_sql_table('covid19_deaths', engine)  # Assuming you have a deaths table
merged_df = pd.merge(df, death_df, on=['Date', 'Country/Region'])
merged_df['CFR'] = merged_df['Deaths'] / merged_df['Confirmed'] * 100

plt.figure(figsize=(12, 6))
merged_df[merged_df['Country/Region'] == 'US']['CFR'].plot(title='Case Fatality Rate in the US')
plt.xlabel('Date')
plt.ylabel('Case Fatality Rate (%)')
plt.savefig('us_cfr.png')
plt.close()

# Analysis 6: Correlation between population density and case rate
# This would require additional data on population and country area

print("Analysis complete. Check the generated PNG files for visualizations.")