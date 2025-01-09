# Which Prepaid Plan is Better?

## Introduction

In the world of telecommunications, which prepaid plan is more profitable can often be a key question for companies. As an analyst at Megaline, a telecommunications operator company, I have been tasked with providing an answer to this question using data. The company offers two prepaid plans: **Surf** and **Ultimate**. The advertising department needs to know which plan generates more revenue so they can create an efficient advertising budget.

In this project, I will analyze a sample dataset of 500 Megaline clients. The dataset contains information such as: who the clients are, where they come from, what type of package they use, and the number of calls and messages they sent in 2018. The goal is to analyze the behavior of users and determine which prepaid plan—**Surf** or **Ultimate**—is more profitable for the company.


## Data Description

The analysis will be conducted using five key datasets:

- **`megaline_calls.csv`:** Contains data on the number and duration of calls made by users.
- **`megaline_internet.csv`:** Includes information about users' internet usage, such as data consumption.
- **`megaline_messages.csv`:** Tracks the number of text messages sent by users.
- **`megaline_plans.csv`:** Provides details about the prepaid plans offered to users (e.g., Surf or Ultimate).
- **`megaline_users.csv`:** Contains demographic and profile information about the users, such as their location and user ID.

These datasets will be used to explore and analyze user behavior, helping to determine which prepaid plan is more profitable.

## Project Workflow

1. **Data Import and Initial Exploration**
   - Import the dataset and explore the data structure, types, and missing values.

2. **Data Preprocessing**
   - Handle missing values and clean the data.
   - Correct data types and improve data quality.

3. **Package Comparison**
   - Compare the **Surf** and **Ultimate** prepaid plans based on revenue, usage behavior, and customer segmentation.

4. **Statistical Hypothesis Testing**
   - Test hypotheses related to revenue generation from different packages and regions.

5. **User Behavior Analysis**
   - Analyze user behavior in terms of call usage, text messages, and internet data consumption for both plans.

6. **Conclusion**
   - Summarize findings and provide insights into which prepaid plan is more profitable.

## Tools and Technologies

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, SciPy  

## Usage

1. Clone the repository.
2. Ensure the dataset is in the same folder as the project file.
3. Open the `.ipynb` file and execute the cells in a Jupyter Notebook environment.

## Conclusion

This project will provide insights into which prepaid plan, **Surf** or **Ultimate**, generates more revenue for Megaline. This analysis will aid in making data-driven decisions regarding marketing and resource allocation.

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

