# Enhancing Insurance Operations with Machine Learning

## Project Introduction

Sure Tomorrow, an insurance company, is exploring how machine learning can be applied to optimize its operations. The company faces various challenges, including the need to improve client targeting, accurately predict insurance claims, estimate the size of potential claims, and protect sensitive client data. By leveraging machine learning, Sure Tomorrow aims to enhance its marketing strategies, make more informed predictions, and ensure data privacy without compromising model performance.

In this project, the task was to develop machine learning models and algorithms that address these challenges. The objectives include identifying clients with similar attributes to a given set of criteria for targeted marketing, predicting the likelihood of new clients making an insurance claim, estimating the potential size of claims using regression techniques, and implementing data obfuscation methods to protect sensitive client information. The goal is to demonstrate how machine learning can drive efficiency and improve decision-making while ensuring robust data security.


## Objectives
The project is divided into four main tasks:

1. **Client Similarity Identification**  
   Develop a model to identify clients with similar attributes to a given set of criteria. This enables targeted marketing strategies.
   
2. **Insurance Claim Prediction**  
   Predict whether a new client is likely to make an insurance claim and compare the performance against a dummy model.
   
3. **Claim Size Estimation**  
   Estimate the potential size of insurance claims using a linear regression model.
   
4. **Data Privacy Protection**  
   Implement a data transformation algorithm to protect sensitive client information through data obfuscation while maintaining model accuracy.

## Dataset Description
The dataset is located at `/insurance_us.csv`. It contains the following features:

- `gender`: Gender of the client (binary).
- `age`: Age of the client (in years).
- `salary`: Annual salary of the client (in USD).
- `family_members`: Number of family members insured under the policy.
- `insurance_benefits`: Amount of insurance claims received by the client over the past five years.

### Data Summary
- **Rows**: 5000  
- **Columns**: 5  
- **Data Types**:  
  - `int64`: 3 columns  
  - `float64`: 2 columns  


## Project Workflow
The project workflow is structured into the following steps:

1. **Data Preprocessing**
   - Check for missing values, outliers, and inconsistencies.
   - Standardize and scale numerical features as needed.

2. **Model Development**
   - Task 1. Similar Clients: Implement K-Nearest Neighbors (KNN) for client similarity identification.
   - Task 2. Is the client likely to receive an insurance claim: Train logistic regression and evaluate claim prediction accuracy.
   - Task 3. Regression (with Linear Regression): Develop a linear regression model to estimate claim sizes.
   - Task 4. Data Obfuscation: Apply data obfuscation techniques to protect client data.

3. **Evaluation**
   - Use appropriate metrics such as accuracy, confusion matrix, mean squared error (MSE), and R² for model evaluation.
   - Compare model predictions with dummy models to establish baseline performance.

4. **Conclusion**
   - Summarize findings for each task.
   - Provide recommendations based on the insights generated.

## Tools and Libraries
The following tools and libraries were used for this project:

- **Programming Language**: Python
- **Libraries**: 
  - `pandas` for data manipulation
  - `numpy` for numerical operations
  - `matplotlib` and `seaborn` for visualization
  - `scikit-learn` for machine learning models and metrics

## Usage

To run the project, follow these steps:

1. **Clone the repository** or download the project folder.
2. **Install required libraries**:
   - Open a terminal and install the necessary Python libraries:
     ```bash
     pip install pandas numpy scikit-learn matplotlib seaborn
     pip install scikit-learn --upgrade
     ```
3. **Run the Jupyter Notebook**:
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open the notebook `insurance_company.ipynb` and run the cells to train the model and analyze the results.

## Key Results
- **Task 1. Similar Clients**: Successfully identified clients similar to specified criteria, aiding targeted marketing efforts.
- **Task 2. Is the client likely to receive an insurance claim**: Logistic regression outperformed the dummy model in predicting insurance claims.
- **Task 3. Regression (with Linear Regression)**: Linear regression provided a reliable estimate of claim sizes with minimal error.
- **Task 4. Data Obfuscation**: Data obfuscation was implemented effectively without compromising model accuracy.

## Conclusion
This project demonstrates the potential of machine learning in enhancing various aspects of insurance operations. From targeted marketing to accurate predictions and secure data handling, the solutions developed here offer a foundation for implementing machine learning in the insurance industry.

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

