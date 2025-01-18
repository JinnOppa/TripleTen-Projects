# Interconnect Client Churn Level Prediction

## Introduction

Client churn is a major concern for businesses, as it directly impacts revenue and long-term growth. Understanding the factors that contribute to churn and identifying at-risk clients can help organizations take proactive measures to retain valuable customers. The **Interconnect Client Churn Level Prediction** project aims to develop an accurate prediction system using machine learning models to identify churn levels based on historical client data.

This project integrates data from multiple sources, preprocesses it to ensure consistency and quality, and employs advanced machine learning techniques. By analyzing key features and their relationships with churn behavior, the project offers actionable insights to businesses for reducing churn rates and fostering client loyalty.

## Data Description

The project utilizes four datasets, each providing distinct information about the clients and their behavior. After preprocessing and integration, these datasets are combined into a single dataset for model training and analysis. The details of the imported datasets are as follows:

1. **`customer_data.csv`**
   - **`customerID`**: Unique identifier for each client.
   - **`gender`**: Gender of the client (`Male`, `Female`).
   - **`SeniorCitizen`**: Indicates whether the client is a senior citizen (0 = No, 1 = Yes).
   - **`Partner`**: Indicates whether the client has a partner (`Yes`, `No`).
   - **`Dependents`**: Indicates whether the client has dependents (`Yes`, `No`).

2. **`service_data.csv`**
   - **`customerID`**: Unique identifier for each client.
   - **`tenure`**: Number of months the client has been with the service.
   - **`PhoneService`**: Indicates whether the client has phone service (`Yes`, `No`).
   - **`InternetService`**: Type of internet service (`DSL`, `Fiber optic`, `No`).
   - **`MultipleLines`**: Indicates whether the client has multiple phone lines.

3. **`billing_data.csv`**
   - **`customerID`**: Unique identifier for each client.
   - **`MonthlyCharges`**: Monthly charges incurred by the client.
   - **`TotalCharges`**: Total charges incurred by the client over the subscription duration.
   - **`PaperlessBilling`**: Indicates whether the client is subscribed to paperless billing (`Yes`, `No`).

4. **`churn_data.csv`**
   - **`customerID`**: Unique identifier for each client.
   - **`Churn`**: Indicates whether the client has churned (`Yes`, `No`).
   - **`Contract`**: Type of contract (`Month-to-month`, `One year`, `Two year`).
   - **`PaymentMethod`**: Payment method used by the client.

## Project Workflow

### **Data Cleaning and Preprocessing**
- **Column Type Conversion**: Ensure columns are in appropriate data types.
- **Handle Missing Values**: Address missing data to avoid biases.
- **Categorical Feature Encoding**: Convert categorical features into numerical formats for machine learning models.

### **Data Integration**
- Integrate the four datasets based on `customerID` to create a single, unified dataset.
- Remove any duplicate entries to maintain data integrity.

### **Further Data Preprocessing**
- Perform feature engineering, including creating a **subscription duration** column from the `tenure` feature.
- Normalize numerical features and address data imbalances, if any.

### **Exploratory Data Analysis (EDA)**
- Analyze numerical and categorical feature distributions.
- Handle outliers in the integrated dataset.
- Visualize feature relationships to uncover insightful patterns.

### **Model Selection and Training**
- Split the integrated dataset into training and testing sets.
- Implement the following machine learning models:
  - **Logistic Regression** (Baseline Model)
  - **Random Forest**
  - **Gradient Boosting Machines (GBM)**
- Perform k-Fold Cross Validation to validate model performance and prevent overfitting.

### **Model Evaluation**
Evaluate the models using the following metrics:
- **Accuracy**
- **F1-Score**
- **AUC-ROC**
- **Confusion Matrix**

### **Hyperparameter Tuning**
Optimize the models using **GridSearchCV** or **RandomizedSearchCV** to identify the best parameters for maximum performance.

### **Final Report and Presentation**
- Develop a comprehensive Jupyter Notebook report that documents the entire workflow.
- Prepare a presentation summarizing findings, insights, and actionable recommendations.

## Tools and Technologies

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, XGBoost

## Usage

To execute the project, follow these steps:

1. **Clone the repository** or download the project files.
2. **Install dependencies**:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn xgboost
   ```
3. **Run the Jupyter Notebook**:
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open the notebook `telecom_client_churn.ipynb` and run the cells to train the model.


## Conclusion

The **Interconnect Client Churn Level Prediction** project leverages data integration, advanced preprocessing, and robust machine learning models to predict churn levels with high accuracy. This system provides actionable insights to reduce churn, enabling businesses to enhance customer retention and maintain long-term relationships effectively.

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