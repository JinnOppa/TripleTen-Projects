# Customer Churn Prediction for Bank Beta

## Introduction

Bank Beta, a leading financial institution, is facing a critical challenge of retaining customers who are at risk of leaving. To tackle this, the bank seeks to predict customer churn and develop targeted retention strategies. The project aims to build a predictive model that can identify high-risk customers, allowing the bank to take proactive actions to reduce churn.

### Aim:
The main goal of this project is to develop a machine learning model capable of predicting whether a customer will leave Bank Beta based on historical data and various customer attributes. The model will help in creating retention campaigns, thereby improving customer retention and reducing the overall churn rate.

### Objectives:
- **Build a Predictive Classification Model**: Develop a machine learning model that predicts whether a customer will churn (Exited = 1) or stay (Exited = 0) based on customer demographics and account activity.
  
- **Achieve High Predictive Accuracy**: The target for model performance is to achieve an F1 score of at least 0.59 on the test dataset, ensuring reliable predictions.

- **Handle Class Imbalance**: Address the class imbalance between customers who stay and customers who churn using techniques like oversampling, undersampling, or synthetic data generation (e.g., SMOTE).

- **Evaluate Model Performance**: Evaluate the performance using metrics such as F1 score, ROC-AUC, and classification reports to assess how well the model identifies potential churners.

- **Optimize Model Performance**: Use hyperparameter tuning techniques to ensure the model performs optimally with balanced recall, precision, and accuracy.

The project aims to develop a system that enables Bank Beta to predict churn effectively and implement customer retention strategies tailored to high-risk individuals.

## Data Description

The analysis uses the `Churn.csv` dataset, which contains the following features:

- **`RowNumber`**: Index of the row.
- **`CustomerId`**: Unique identifier for the customer.
- **`Surname`**: Customer's surname.
- **`CreditScore`**: Credit score of the customer.
- **`Geography`**: Customer's country of residence.
- **`Gender`**: Gender of the customer.
- **`Age`**: Age of the customer.
- **`Tenure`**: Number of years the customer has been with the bank.
- **`Balance`**: Account balance of the customer.
- **`NumOfProducts`**: Number of products the customer uses.
- **`HasCrCard`**: Whether the customer has a credit card (1 = Yes, 0 = No).
- **`IsActiveMember`**: Whether the customer is an active member (1 = Yes, 0 = No).
- **`EstimatedSalary`**: Estimated salary of the customer.
- **`Exited`**: Target variable indicating whether the customer churned (1 = Churned, 0 = Stayed).

This dataset contains **10,000 entries** and **14 columns**, with `Exited` as the target variable.

## Project Workflow

### 1. Import Libraries and Dataset
- Import necessary libraries: Pandas, NumPy, Scikit-learn, Matplotlib, etc.
- Load the `Churn.csv` dataset and perform basic data exploration (e.g., check for missing values and data types).

### 2. Data Preprocessing and Analysis
- Clean the data by handling missing values, encoding categorical variables, and normalizing numerical features.
- Perform exploratory data analysis (EDA) to understand the relationships between features, and visualize data distributions.

### 3. Model Building
- **Split Dataset**: Divide the dataset into training and testing sets.
- **Handle Class Imbalance**: Apply techniques such as SMOTE to address the class imbalance between churned and non-churned customers.
- **Train Model**: Train machine learning models, such as Random Forest, Logistic Regression, and XGBoost.
- **Hyperparameter Tuning**: Use grid search or random search to find the best parameters for the model.

### 4. Model Evaluation
- Evaluate the model performance using:
  - **F1 score**: Focus on balancing precision and recall.
  - **ROC-AUC**: Assess the model's ability to discriminate between churned and non-churned customers.
  - **Confusion Matrix**: Examine the true positives, false positives, true negatives, and false negatives.

### 5. Conclusion
- Summarize the findings, including the F1 score and AUC-ROC of the best model.
- Provide recommendations for the bank based on model predictions, including retention strategies for high-risk customers.

## Tools and Technologies

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, imbalanced-learn

## Usage

To run the project, follow these steps:

1. **Clone the repository** or download the project folder.
2. **Install required libraries**:
   - Open a terminal and install the necessary Python libraries:
     ```bash
     pip install pandas numpy scikit-learn matplotlib seaborn imbalanced-learn
     ```
3. **Run the Jupyter Notebook**:
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open the notebook `bank_client_behavior.ipynb` and run the cells to train the model.

## Conclusion

The project successfully developed a predictive model for customer churn at Bank Beta. Through the application of machine learning techniques and careful handling of class imbalance, the final model demonstrated reliable performance. This model can help Bank Beta improve its retention strategies by identifying customers at risk of leaving and allowing for targeted intervention.

## Future Improvements

- **Ensemble Methods**: Explore the use of ensemble methods such as Random Forest and Gradient Boosting for further improving model performance.
- **Deep Learning**: Investigate neural networks or deep learning models for even more accurate predictions.
- **Additional Features**: Incorporate more customer data, such as transaction history and interactions with customer service, to further improve predictions.

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
