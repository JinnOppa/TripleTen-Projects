# Zuber Ride-Sharing Analysis

## Introduction

This project involves analyzing taxi trip data in Chicago, focusing on two main objectives: **Exploratory Data Analysis (EDA)** and **Hypothesis Testing**. The EDA phase utilizes two datasets: one containing the number of trips completed by various taxi companies, and another detailing the average trips ending at specific drop-off locations across the city. The aim is to explore these datasets, identify patterns, and create visualizations to highlight the top-performing taxi companies and the most popular drop-off locations, providing insights into Chicago's taxi trip dynamics.

In the **Hypothesis Testing** phase, the analysis focuses on a dataset containing trip details between the Loop and O’Hare International Airport. The objective is to determine whether the average trip duration changes on Saturdays when it rains. This involves formulating null and alternative hypotheses, selecting a significance level, applying statistical tests, and interpreting the results. The project demonstrates the application of data analysis techniques, generating meaningful insights and utilizing hypothesis testing to support data-driven conclusions.

### Aim:
The goal is to explore patterns in Chicago's ride-sharing data, including analyzing taxi company performance, popular drop-off locations, and trip duration variability based on weather conditions. Additionally, this project tests the hypothesis that average trip duration on Saturdays differs when it rains.

### Objectives:
1. **Exploratory Data Analysis (EDA)**:
   - Analyze the number of trips completed by various taxi companies in Chicago.
   - Explore the most popular drop-off locations across the city.
   - Investigate patterns related to trip durations and how they are affected by weather conditions.

2. **Hypothesis Testing**:
   - Hypothesis: **Does the average trip duration change on Saturdays when it rains?**
   - Test this hypothesis using statistical methods and interpret the results.


## Data Description

The analysis will be conducted using the following datasets:

- **`moved_project_sql_result_01.csv`**: Contains the number of trips completed by various taxi companies in Chicago.
- **`moved_project_sql_result_04.csv`**: Contains average trips ending at specific drop-off locations in Chicago.
- **`moved_project_sql_result_07.csv`**: Contains trip details between the Loop and O'Hare, including weather conditions and duration of trips.

### Dataset Breakdown

#### `moved_project_sql_result_01.csv`
Contains data on taxi companies and the number of trips completed by each company. The dataset includes:
- **`company_name`**: The name of the taxi company.
- **`trips_amount`**: The number of trips completed by the company.

#### `moved_project_sql_result_04.csv`
Contains data on drop-off locations and average trips for each location in Chicago. The dataset includes:
- **`dropoff_location_name`**: The name of the drop-off location.
- **`average_trips`**: The average number of trips ending at the drop-off location.

#### `moved_project_sql_result_07.csv`
Contains trip data for the Loop to O'Hare route. The dataset includes:
- **`start_ts`**: Timestamp when the trip started.
- **`weather_conditions`**: Weather conditions during the trip (Good or Bad).
- **`duration_seconds`**: Duration of the trip in seconds.

## Project Workflow

1. **Data Import and Initial Exploration**
   - Import the datasets and examine the structure, data types, and check for any missing values.

2. **Data Preprocessing**
   - Clean the data by handling missing values and ensuring proper data types.

3. **Exploratory Data Analysis (EDA)**
   - Analyze the number of trips completed by taxi companies.
   - Explore the most popular drop-off locations in Chicago.
   - Investigate patterns in trip durations and weather conditions.

4. **Hypothesis Testing**
   - Hypothesis: **Does the average trip duration change on Saturdays when it rains?**
     - Formulate null and alternative hypotheses.
     - Select significance level and apply statistical tests to the dataset.
     - Interpret the test results to support or reject the hypothesis.

5. **Visualization**
   - Create visualizations to present insights from the data analysis, including bar charts, line graphs, and box plots.

6. **Conclusion**
   - Summarize the findings and provide recommendations based on the analysis.

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, SciPy

## Usage

1. **Clone the repository** or download the project folder.
2. **Install the required libraries**:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```
3. **Run the Jupyter Notebook**:
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open the notebook and run the cells one by one to perform the analysis and generate insights.


## Conclusion

This project provides valuable insights into Chicago's ride-sharing data, including the performance of taxi companies, popular drop-off locations, and the impact of weather on trip durations. The results of the hypothesis testing will also shed light on whether rainy Saturdays affect ride duration.

## MIT License

MIT License

Copyright (c) 2025 Eugene Winata

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
