
# Optimizing Gold Ore Extraction Efficiency in Heavy Industries: A Machine Learning Approach

## Introduction

Gold ore extraction in heavy industries involves complex processes that require constant optimization for cost-effectiveness and productivity. The project focuses on predicting and optimizing gold ore extraction efficiency using machine learning techniques. By developing accurate models for predicting extraction efficiency, this project aims to help industries reduce waste, increase productivity, and improve decision-making processes.

### Aim:
The primary goal of this project is to develop machine learning models that predict the efficiency of gold ore extraction based on historical and sensor data from industrial operations. The models will help optimize extraction strategies, reducing costs and maximizing output.

### Objectives:
- **Build Predictive Models**: Develop machine learning models to predict extraction efficiency using different regression algorithms.
- **Improve Prediction Accuracy**: Use various regression models to determine the most effective predictors for optimizing gold ore extraction.
- **Feature Engineering**: Explore relevant features that impact the extraction process and improve model performance.
- **Model Comparison**: Compare the performance of various models to identify the best one based on accuracy, speed, and interpretability.

The project will focus on using machine learning techniques to create systems that improve the efficiency and cost-effectiveness of gold ore extraction in the mining industry.

## Data Description

The project uses the following dataset:
- **`gold_recovery.csv`**: This dataset contains various features, including concentrations of gold (Au), silver (Ag), lead (Pb), and other materials at different stages of the extraction process, along with the target variable, `rougher.output.recovery`, which represents the recovery rate of gold.

The dataset has the following key columns:
- **`date`**: Date of the sample collection.
- **`Au`, `Ag`, `Pb`**: Concentration of gold, silver, and lead at different stages of the process.
- **`rougher.output.recovery`**: Target variable (gold recovery rate).
- **Other process parameters**: Various features related to flotation, concentration, and refining steps.


## Project Workflow

### 1. Data Exploration and Preprocessing
- **Data Cleaning**: Handle missing values and outliers in the dataset.
- **Feature Engineering**: Create new features based on existing ones and ensure consistency across the dataset.
- **Scaling**: Normalize numerical features for consistency during model training.
- **Recovery Calculation**: Ensure that the target variable `rougher.output.recovery` is correctly calculated and clean.

### 2. Data Analysis
- **Concentration Analysis**: Explore metal concentrations (e.g., gold, silver) at different stages and their relationship to recovery.
- **Distribution Analysis**: Analyze the distribution of the feed size and its impact on the recovery process.
- **Correlation Analysis**: Investigate the correlation between features like metal concentration and recovery.

### 3. Model Building
- **Train-Test Split**: Divide the data into training and testing sets.
- **Model Selection**: Train multiple models, including:
  - Linear Regression
  - Decision Tree Regressor
  - Support Vector Regressor (SVR)
  - Random Forest Regressor
  - Gradient Boosting Regressor
- **Model Tuning**: Use techniques like grid search or random search for hyperparameter optimization.

### 4. Model Evaluation
- **Train Models**: We train various machine learning models and evaluate them using cross-validation to ensure a reliable estimate of model performance.

- **sMAPE Calculation**: To evaluate the models, we use the Symmetric Mean Absolute Percentage Error (sMAPE) metric, which is commonly used in regression tasks. The formula for sMAPE is as follows:

   $\text{sMAPE} = \frac{1}{n} \sum_{i=1}^{n} \frac{|y_i - \hat{y}_i|}{(y_i + \hat{y}_i)/2} \times 100$

   Where:
   - $ y_i$ is the true value,
   - $\hat{y}_i$ is the predicted value,
   - $n$ is the number of samples.

    and 
    $$sMAPE_{\text{akhir}} = 25\% \times sMAPE_{\text{rougher}} + 75\% \times sMAPE_{\text{final}}$$

- **Cross-Validation and Model Comparison**: The models are evaluated using k-fold cross-validation, and the average sMAPE score across all folds is computed for each model.

- **Test Sample Evaluation**: After identifying the best-performing model, we test it on a separate test dataset to evaluate its final performance and generalization capability.

### 5. Conclusion
- Summarize the key findings, including which models performed the best and their evaluation scores.
- Discuss the implications of the results for optimizing the gold extraction process.

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
   - Open the notebook `gold_mining.ipynb` and run the cells to train and evaluate the models.

## Conclusion

The project successfully developed machine learning models to predict gold ore extraction efficiency. By testing multiple regression algorithms and fine-tuning their parameters, we identified the most accurate and reliable model for the given dataset. The final model can assist industries in optimizing their extraction processes and improving productivity.

## Future Improvements

- **Ensemble Methods**: Explore the use of ensemble methods like Stacking and Bagging to further improve model performance.
- **Deep Learning**: Investigate neural networks or deep learning models for more complex data patterns.
- **Additional Data**: Incorporate more process data, such as operational factors and equipment conditions, to improve predictions.

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
