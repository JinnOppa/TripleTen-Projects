# Entertainment Software Rating Board 2016 Analysis

## Introduction

In preparation for the 2017 marketing campaign, the online store **Ice** is analyzing video game sales data from 2016. The dataset provides insights into user and expert reviews, genre information, platform details, and sales figures across various regions. A key component of the dataset is the **ESRB (Entertainment Software Rating Board)** abbreviation, which provides age ratings for games.

### Aim:
To explore sales trends, identify factors contributing to the success of video games, and predict market trends. The analysis will help **Ice** in shaping their 2017 marketing strategy and optimizing the customer shopping experience.

### Objectives:
1. **Sales Trend Analysis**: Identify patterns in game sales across different regions (North America, Europe, Japan, and others).
2. **Genre and Platform Analysis**: Examine the relationship between game genres, platforms, and their success in terms of sales.
3. **Ratings and User Sentiment**: Explore the correlation between critic and user scores and how they impact game sales.
4. **ESRB Rating Impact**: Investigate how ESRB ratings influence game sales and reception.


## Data Description

The analysis will be conducted using the following dataset:

- **`games.csv`:** Contains sales and rating information for video games, including details on platform, genre, year of release, and sales by region (North America, Europe, Japan, and other regions). It also includes user and critic scores, as well as ESRB ratings for each game.

The dataset consists of **16,715 entries** and **11 columns**:

- **`Name`**: Name of the game.
- **`Platform`**: Platform on which the game was released (e.g., PlayStation, Xbox, PC).
- **`Year_of_Release`**: The year when the game was released.
- **`Genre`**: The genre of the game (e.g., Action, Adventure, Strategy).
- **`NA_sales`**: Sales in North America (in millions).
- **`EU_sales`**: Sales in Europe (in millions).
- **`JP_sales`**: Sales in Japan (in millions).
- **`Other_sales`**: Sales in other regions (in millions).
- **`Critic_Score`**: Critic review score (some games may be missing this).
- **`User_Score`**: User review score (some games may be missing this).
- **`Rating`**: ESRB rating (e.g., E, M, T).

This dataset will be used to identify patterns in gaming sales and help understand the factors that influence the success of video games.

## Project Workflow

1. **Data Import and Initial Exploration**
   - Import the dataset and examine the structure, data types, and any missing values.

2. **Data Preprocessing**
   - Handle missing values and clean the data.
   - Convert data types where necessary and prepare the dataset for analysis.

3. **Sales Trend Analysis**
   - Analyze sales data by region (North America, Europe, Japan, and others) to identify patterns and trends in gaming preferences.

4. **Genre and Platform Analysis**
   - Investigate the relationship between genres, platforms, and game sales. Identify which genres and platforms are more successful.

5. **Ratings and User Sentiment**
   - Compare critic and user scores, and analyze their correlation with game sales.

6. **ESRB Rating Impact**
   - Explore how the ESRB rating (age rating) impacts sales and user reception.

7. **Conclusion**
   - Summarize findings and provide recommendations for future marketing efforts based on data analysis.

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

This project will provide valuable insights into the sales trends of video games in 2016, including the impact of genres, platforms, and ESRB ratings. The analysis will help **Ice** determine which games to focus on in the 2017 marketing campaign.

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

---
