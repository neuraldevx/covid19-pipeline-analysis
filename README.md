# COVID-19 ETL Data Pipeline and Analysis

This project implements an ETL (Extract, Transform, Load) pipeline for COVID-19 data and performs various analyses on the processed data. It uses PostgreSQL as the database for storing the processed data.

## Project Structure

- `main.py`: Handles the ETL process
- `analysis.py`: Performs data analysis and generates visualizations
- `requirements.txt`: Lists project dependencies
- `.env`: Contains environment variables (not tracked by git)
- `.env.example`: Example environment variable file

## Project Samples
![image](https://github.com/user-attachments/assets/2bf9ecfe-e336-427f-84a3-a9384a16f54e)
![image](https://github.com/user-attachments/assets/afa21a39-9e0e-48a2-89bd-0c80c6e2b879)

## Prerequisites

- Python 3.7+
- PostgreSQL 12+

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/neuraldevx/covid19-etl-data-pipeline.git
   cd covid19-etl-data-pipeline
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv covid_env
   source covid_env/bin/activate  # On Windows, use `covid_env\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL:
   - Install PostgreSQL if you haven't already
   - Create a new database for this project:
     ```
     createdb covid19_data
     ```

5. Set up your environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your database credentials and other configuration in `.env`:
     ```
     DB_USER=your_username
     DB_PASSWORD=your_password
     DB_HOST=localhost
     DB_PORT=5432
     DB_NAME=covid19_data
     ```

## Usage

1. Run the ETL process to extract data and load it into PostgreSQL:
   ```
   python main.py
   ```

2. Run the analysis to generate visualizations from the data in PostgreSQL:
   ```
   python analysis.py
   ```

## Database Schema

The project uses the following main table in PostgreSQL:

- `covid19_confirmed_cases`:
  - `Date`: Date of the record
  - `Country/Region`: Country or region name
  - `Confirmed`: Total confirmed cases
  - `NewCases`: New cases on that date

Additional tables may be created for deaths and recovered cases data.

## Analysis Outputs

The analysis script generates several visualizations using data from the PostgreSQL database:

- Global daily new COVID-19 cases
- Top 10 countries by total COVID-19 cases
- Daily new cases for the United States
- 7-day rolling average of new cases in the US
- Case fatality rate in the US

## Data Source

This project uses data from the [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19).


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
