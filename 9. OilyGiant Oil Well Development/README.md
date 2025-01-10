# OilyGiant Oil Well Development Project

## Introduction

OilyGiant, a leading mining company, aims to expand its oil well development in three regions. The goal of this project is to predict the oil reserves in new wells, assess profitability, and evaluate the risk of each region to recommend the most viable area for new oil well developments. By leveraging predictive modeling and risk assessment, the company seeks to optimize investment in oil exploration.

### Aim:
The main objective of this project is to predict the oil reserves in newly proposed wells using geological data and identify the best regions for development based on predicted reserves, profitability, and risk.

### Objectives:
- **Build a Predictive Regression Model**: Develop a linear regression model to predict the oil reserves (`product`) based on geological features (`f0`, `f1`, `f2`) of the regions.
  
- **Profitability Analysis**: Calculate the profitability of new wells by predicting oil volumes and assessing the total potential profit for the 200 wells in each region.

- **Risk Assessment**: Use bootstrapping to assess the uncertainty and risk associated with the predicted reserves and potential profits, estimating the likelihood of financial loss.

- **Evaluate Model Performance**: Measure model performance through RMSE and use it to guide decisions about which regions to prioritize for well development.

- **Recommend Optimal Region**: Provide a recommendation on the best region for development based on predicted profit and associated risk.

The project enables OilyGiant to make data-driven decisions on where to focus its oil exploration and maximize financial returns.

## Data Description

The analysis uses three datasets for three regions, each containing geological data and reserve estimates for oil wells.

### Datasets:
1. **`geo_data_0.csv`**: Data for Region 0
2. **`geo_data_1.csv`**: Data for Region 1
3. **`geo_data_2.csv`**: Data for Region 2

### Features:
- **`id`**: Unique identifier for the well.
- **`f0`, `f1`, `f2`**: Geological features related to each well's environment.
- **`product`**: Volume of predicted reserves (target variable).

The data contains information for multiple wells across three regions, with **geological features** and **reserve volumes** as key components for predicting profitability.

## Project Workflow

### 1. Import Libraries and Dataset
- Import necessary libraries: Pandas, NumPy, Scikit-learn, Matplotlib, etc.
- Load the `geo_data_0.csv`, `geo_data_1.csv`, and `geo_data_2.csv` datasets.
- Perform basic data exploration and clean-up (checking for missing values and data types).

### 2. Data Preprocessing and Exploration
- Clean the data by handling missing values and encoding categorical features (if any).
- Perform exploratory data analysis (EDA) to understand the relationships between geological features (`f0`, `f1`, `f2`) and reserve volumes (`product`).
- Visualize the distribution of `product` to detect any patterns or anomalies.

### 3. Model Building
- **Data Splitting**: Split the data into training and testing sets (75% training, 25% testing).
- **Train Regression Model**: Use a linear regression model to predict the oil reserves (`product`).
- **Hyperparameter Tuning**: Apply grid search or cross-validation to find the best model parameters.
- **Model Evaluation**: Evaluate the model’s performance on the test set using RMSE to ensure accurate predictions.

### 4. Profit Calculation and Risk Analysis
- **Profit Estimation**: Estimate the total profit for the 200 most profitable wells in each region using predicted reserves.
- **Bootstrapping for Risk**: Implement bootstrapping (1,000 iterations) to assess the variability of the predicted profits and determine the risk of financial loss.
- **Confidence Intervals**: Calculate 95% confidence intervals for profit distributions and assess the likelihood of losses.

### 5. Conclusion and Recommendations
- **Best Region for Development**: Based on profitability and risk analysis, recommend the region with the highest predicted profit and lowest financial risk.
- **Summary of Findings**: Present key findings, including the total profit and risk levels for each region.

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

## Usage

To run the project, follow these steps:

1. **Clone the repository** or download the project folder.
2. **Install required libraries**:
   - Open a terminal and install the necessary Python libraries:
     ```bash
     pip install pandas numpy scikit-learn matplotlib seaborn
     ```
3. **Run the Jupyter Notebook**:
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open the notebook `oil_well_development.ipynb` and run the cells to train the model and analyze the results.

## Conclusion

The project successfully developed a predictive model for estimating the oil reserves in new wells and assessing the risk associated with each region. By leveraging predictive modeling and bootstrapping techniques, OilyGiant can make informed decisions on where to focus its resources for new oil well development, maximizing profit while minimizing financial risk.

## Future Improvements

- **Model Enhancement**: Explore more advanced models (e.g., Random Forest, Gradient Boosting) to improve prediction accuracy.
- **Feature Engineering**: Investigate additional features (e.g., environmental data, drilling history) to improve model performance.
- **Alternative Risk Assessment**: Test other risk assessment methods like Monte Carlo simulations for more complex scenarios.

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
