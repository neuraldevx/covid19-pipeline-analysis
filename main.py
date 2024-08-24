import pandas as pd
import requests
from sqlalchemy import create_engine
from datetime import datetime
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Extract
def extract_data(url):
    response = requests.get(url)
    data = pd.read_csv(url)
    return data

# Transform
def transform_data(df):
    # Melt the dataframe to convert dates from columns to rows
    melted_df = df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
                        var_name='Date', value_name='Confirmed')
    
    # Convert date strings to datetime objects
    melted_df['Date'] = pd.to_datetime(melted_df['Date'], format='%m/%d/%y')
    
    # Group by country and date, summing the confirmed cases
    grouped_df = melted_df.groupby(['Country/Region', 'Date'])['Confirmed'].sum().reset_index()
    
    # Calculate new cases
    grouped_df['NewCases'] = grouped_df.groupby('Country/Region')['Confirmed'].diff().fillna(0)
    
    return grouped_df

# Load
def load_data(df, table_name, engine):
    df.to_sql(table_name, engine, if_exists='replace', index=False)

# Main ETL process
def etl_process():
    # Connection string for PostgreSQL
    db_connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    
    # URL for COVID-19 confirmed cases data
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    
    try:
        # Extract
        raw_data = extract_data(url)
        
        # Transform
        transformed_data = transform_data(raw_data)
        
        # Load
        engine = create_engine(db_connection_string)
        load_data(transformed_data, 'covid19_confirmed_cases', engine)

        print("ETL process completed successfully!")
    except Exception as e:
        print(f"An error occurred during the ETL process: {e}")
        sys.exit(1)

if __name__ == "__main__":
    etl_process()