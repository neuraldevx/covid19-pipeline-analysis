import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connect to the database
engine = create_engine("postgresql://jakechris:Badgerboy511@localhost:5432/covid19_data")

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

print("Analysis complete. Check the generated PNG files for visualizations.")