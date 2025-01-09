# Analyzing Borrower Default Risk in Credit Scoring

## Introduction

In this project, I was tasked with analyzing borrower default risk to support the bank's credit division in developing more accurate credit scoring methodologies. In the competitive landscape of banking and finance, accurate credit assessment is crucial for mitigating risks associated with borrower defaults. This project investigates the relationship between borrowers' marital status, the number of children they have, and the probability of defaulting on loans. By analyzing existing credit eligibility data, the project aims to provide insights that can improve decision-making processes within the credit division.

## Goals

The project seeks to achieve the following research objectives:

1. **Hypothesis 1:** Investigate whether there is a correlation between having children and the probability of defaulting on a loan.  
2. **Hypothesis 2:** Explore the correlation between family status and the probability of defaulting on a loan.  
3. **Hypothesis 3:** Analyze the relationship between income level and the probability of defaulting on a loan.  
4. **Hypothesis 4:** Examine how different credit goals influence the default percentage.  

## Data Description

The dataset used for the analysis includes the following attributes:

- **`children`:** Number of children in the family.  
- **`days_employed`:** Customer work experience in days.  
- **`dob_years`:** Customer age in years.  
- **`education`:** Customer's education level.  
- **`education_id`:** Identifier for the customer's education level.  
- **`family_status`:** Marital status of the customer.  
- **`family_status_id`:** Identifier for the customer's marital status.  
- **`gender`:** Customer gender.  
- **`income_type`:** Job type of the customer.  
- **`debt`:** Whether the customer has ever defaulted on a loan.  
- **`total_income`:** Monthly income of the customer.  
- **`purpose`:** The purpose of obtaining a loan.  

## Project Structure

The analysis involves the following key steps:

1. **Data Preprocessing:**  
   - Identify and address missing values.  
   - Correct data types where necessary.  
   - Eliminate duplicates and ensure data integrity.  

2. **Exploratory Data Analysis (EDA):**  
   - Explore relationships between borrower characteristics (e.g., family status, income level, loan purpose) and default probabilities.  

3. **Hypothesis Testing:**  
   - Test the established hypotheses to identify significant factors influencing borrower default risk.  

4. **Reporting:**  
   - Synthesize findings into a comprehensive report to inform credit evaluation policies.

## Tools and Technologies

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, SciPy (for statistical tests)

## Usage

1. Clone the repository.  
2. Ensure the dataset is in the same folder as the project file.  
3. Open the `.ipynb` file and execute the cells in a Jupyter Notebook environment.  

## Conclusion

This project aims to enhance financial stability by identifying key factors affecting borrower default risk. The insights derived will help refine credit policies and improve risk mitigation strategies, benefiting both the bank and its clients.

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
