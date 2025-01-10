# Customer Subscription Plan Recommendation System for Megaline Mobile Operator

## Introduction

Megaline, a mobile network operator, is confronted with a notable retention challenge, as a considerable portion of its clientele persists with legacy subscription plans. To address this, the company is developing a predictive model capable of analyzing customer behavior and recommending one of its latest subscription plans: Smart or Ultra.

With access to historical customer behavior data, specifically for customers who have transitioned to the newer plans, the primary objective is to build a classification model that can accurately predict the most appropriate subscription plan for prospective customers. The target is to achieve a predictive accuracy greater than 0.75.

### Aim:
The primary aim of this project is to develop a machine learning model that can predict the most suitable subscription plan for a customer based on their historical usage patterns. The recommendation system will help Megaline enhance its customer retention efforts by suggesting tailored subscription plans (either Smart or Ultra) based on individual customer behavior, ultimately improving user satisfaction and reducing churn.

### Objectives:
- **Build a Predictive Classification Model**: The goal is to create a machine learning model capable of predicting whether a customer would be better suited to the Smart or Ultra plan based on their monthly usage data (calls, minutes, messages, data usage).
  
- **Achieve High Predictive Accuracy**: The target accuracy for the model is set to exceed 0.75, ensuring reliable recommendations. This will be assessed by comparing predicted subscription plans against actual customer preferences in the test data.

- **Handle Data Preprocessing**: The project will involve cleaning the dataset by addressing missing values, outliers, and ensuring the dataset is balanced, especially considering potential class imbalances between Smart and Ultra plan users.

- **Evaluate Model Performance**: After training the model, it will be evaluated using various metrics such as accuracy, precision, recall, and the confusion matrix to assess its reliability and precision in providing correct recommendations.

- **Optimize Model Performance**: Hyperparameter tuning will be performed to ensure the model reaches its optimal performance using grid search techniques and cross-validation.

This project aims to not only predict the best plan for users but also to improve Megaline's customer retention strategies by providing personalized recommendations that better match the needs of each individual based on their actual usage.

## Data Description

The analysis will use the following dataset:

- **`customer_subscription_data.csv`:** Contains customer subscription data with the following features:
    - **`calls`**: Total number of calls made by the customer.
    - **`minutes`**: Total number of minutes the customer has used.
    - **`messages`**: Total number of text messages sent by the customer.
    - **`mb_used`**: Total data usage in MB.
    - **`is_ultra`**: Target variable indicating the subscription plan:
      - 1 for the "Ultra" plan
      - 0 for the "Smart" plan

This dataset contains **3,214 entries** and **5 columns**:
- **`calls`**: Total number of calls made.
- **`minutes`**: Total number of minutes used.
- **`messages`**: Total number of messages sent.
- **`mb_used`**: Total data usage (in MB).
- **`is_ultra`**: Target variable (1 for Ultra, 0 for Smart).


## Project Workflow

### 1. Import Libraries and Dataset
- Import necessary libraries: Pandas, NumPy, Scikit-learn, etc.
- Load the dataset and perform basic data exploration (e.g., view data types, check for missing values).

### 2. Data Preparation and Analysis
- Clean the data by handling missing values and outliers.
- Perform exploratory analysis to understand key customer behaviors (calls, data usage, etc.).

### 3. Machine Learning Model
- **Split Dataset**: Divide data into training and testing sets.
- **Baseline Model**: Train an initial model and evaluate performance.
- **Hyperparameter Tuning**: Optimize model parameters using grid search.
- **Final Model**: Train the model with the best parameters and evaluate it on the test set.

### 4. Model Evaluation
- Assess model performance with metrics like accuracy, precision, recall, and confusion matrix.

### 5. Conclusion
- Summarize the findings and performance of the model.
- Provide recommendations for customer subscription plan allocation based on predictions.


## Tools and Technologies

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

## Usage

To run the `.ipynb` file, follow these steps:

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
