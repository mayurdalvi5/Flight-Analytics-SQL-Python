# Flight Analytics Application ✈️

## Overview 🌍

The Flight Analytics Application is a powerful tool designed to seamlessly connect to a MySQL database and provide comprehensive flight information. Users can easily extract flight details such as date, departure time, duration, and prices based on specified source and destination filters. The application also offers insightful visualizations using Plotly charts, enabling users to make well-informed decisions in the dynamic realm of air travel.

## Features 🛫

- **Check Flights**: Search for available flights between specified source and destination cities.
- **Analytics**:
  - View airline frequency distribution.
  - Identify the busiest airports.
  - Analyze daily flight frequencies over time.

## Requirements 📋

- Python 3.x
- MySQL Server
- Python Libraries:
  - mysql-connector-python
  - streamlit
  - plotly

## Installation 💻

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repository/flight-analytics.git
cd flight-analytics
```

### Step 2: Install Python Packages
```
pip install -r requirements.txt
```

### Step 3: Set Up MySQL Database

* Ensure MySQL server is running.
* Create a database named flight.
* Import your flight data into a table named `flight` within the `flight` database.


### Step 4: Configure Database Connection
Update the database connection parameters (host, user, password) in the DB class in `dbhelper.py`.

## File Structure 📁
```
flight-analytics/
│
├── dbhelper.py         # Database helper class for interacting with MySQL
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
├── requirements.txt    # List of required Python packages
└── .gitignore          # Git ignore file
```

## Usage
### Run the Application
```
streamlit run app.py
```


### User Interface
####  Sidebar Menu:
* Select One: Default option providing project information.
* Check Flights: Allows users to search for flights between specified cities.
* Analytics: Provides various analytical visualizations of flight data.

#### Analytics
* Airline Frequency Distribution: Pie chart showing the distribution of flights by airline.
* Busiest Airports: Bar chart showing the busiest airports based on flight frequency.
* Daily Flight Frequency: Line chart showing the frequency of flights over time.

## Conclusion
This Flight Analytics Application provides an intuitive interface for exploring and analyzing flight data. By following the instructions in this README, you can set up and use the application efficiently. For further assistance, refer to the official documentation or contact the project maintainers.
