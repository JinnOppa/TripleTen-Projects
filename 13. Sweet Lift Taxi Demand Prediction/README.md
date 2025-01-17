# Sweet Lift Taxi Demand Prediction

## Introduction

Sweet Lift is a taxi company that specializes in providing reliable transportation services to and from airports. However, the company faces a recurring challenge of driver shortages during peak hours, leading to unmet customer demand and operational inefficiencies. To address this issue, Sweet Lift is investing in a machine learning solution to predict the number of taxi orders expected in the next hour, enabling better resource planning and driver allocation.

### Aim:
The main goal of this project is to develop a machine learning model capable of predicting taxi demand for the next hour based on historical data. This will help Sweet Lift optimize driver availability, minimize customer wait times, and improve operational efficiency.

### Objectives:
- **Develop a Predictive Model**: Create a model that can predict the number of taxi orders for the next hour based on historical data.
- **Model Evaluation**: Assess the performance of the model using Root Mean Squared Error (RMSE), with the goal of achieving an RMSE value of 48 or lower on the test set.
- **Data Preprocessing and Resampling**: Resample the data to create a structured hourly dataset for model training.
- **Hyperparameter Tuning**: Train multiple models with varying hyperparameters and evaluate their performance.
- **Robust Testing**: Use a test sample representing 10% of the original dataset for performance validation.

## Data Description

The dataset contains historical records of taxi orders at an airport. The key features in the dataset are:

- **`datetime`**: The timestamp of the taxi order.
- **`num_orders`**: The number of taxi orders made at that specific time.

The dataset is stored in the `/taxi.csv` file and consists of **26,496 rows** and **2 columns**.

## Project Workflow

### 1. Import Libraries and Load Data
- Import necessary libraries like Pandas, NumPy, Scikit-learn, and others.
- Load the dataset and explore the structure of the data.

### 2. Data Preprocessing and Resampling
- **Resampling**: Convert the `datetime` column to a datetime object and resample the data to a one-hour frequency to align with the prediction task.
- **Missing Values**: Handle any missing data if necessary (though the dataset doesn't seem to have missing values).
- **Feature Engineering**: Extract useful time-related features like hour, day, and month to help the model understand seasonal and time-based trends.

### 3. Model Building
- **Train-Test Split**: Split the dataset into training and test sets, with the test set representing 10% of the original dataset.
- **Model Selection**: Train multiple regression models with the following hyperparameters:
  
  - **Random Forest Regressor**:
    - `n_estimators`: [50, 100, 150]
    - `max_depth`: [None, 10, 20]
  
  - **Gradient Boosting Regressor**:
    - `n_estimators`: [50, 100, 150]
    - `learning_rate`: [0.01, 0.1, 0.5]
    - `max_depth`: [3, 5, 7]
  
  - **Linear Regression**: No hyperparameters to tune.

### 4. Hyperparameter Tuning
- **Grid Search**: Use `GridSearchCV` to tune hyperparameters and find the best model configuration.
- **Cross-Validation**: Use 5-fold cross-validation to ensure robust model evaluation.

### 5. Model Evaluation
- Evaluate model performance using RMSE (Root Mean Squared Error) to assess the accuracy of the taxi demand predictions.
- Ensure the RMSE value on the test set does not exceed the target threshold of 48.

### 6. Conclusion
- Summarize the findings and discuss which model performed best.
- Provide actionable insights that can help Sweet Lift optimize taxi demand forecasting and resource allocation.

## Tools and Technologies

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn, LightGBM, Statsmodels

## Usage

To run the project, follow these steps:

1. **Clone the repository** or download the project folder.
2. **Install required libraries**:
   - Open a terminal and install the necessary Python libraries:
     ```bash
     pip install pandas numpy scikit-learn matplotlib lightgbm statsmodels
     ```
3. **Run the Jupyter Notebook**:
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open the notebook `taxi_order.ipynb` and run the cells to train the model.

## Conclusion

This project provides a predictive model for taxi demand at Sweet Lift, enabling better driver allocation and improved service. By forecasting taxi orders in the next hour, the model helps optimize resource management and minimize customer waiting times.

## Future Improvements

- **Additional Features**: Incorporate external data, such as weather conditions, traffic data, and special events, to improve the accuracy of predictions.
- **Ensemble Methods**: Explore ensemble methods like stacking to combine the predictions of multiple models for better performance.
- **Real-Time Forecasting**: Implement a real-time prediction system for dynamic driver allocation and better responsiveness to demand fluctuations.

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
