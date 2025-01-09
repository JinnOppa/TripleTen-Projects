# Key Factors Influencing Used Vehicle Prices

## Introduction

In this project, I was tasked with analyzing data for Crankshaft List to uncover key factors influencing used vehicle prices. By studying data from hundreds of vehicle ads displayed daily, this project aims to provide valuable insights into the used vehicle market. The focus is on parameters such as vehicle age, annual mileage, number of cylinders, condition, and the ad's validity period to determine their impact on vehicle pricing. This analysis will guide smarter decision-making in vehicle transactions and help the company better understand market dynamics.

## Goals

The project seeks to answer the following questions:
1. How do vehicle age and mileage influence the price of used vehicles?
2. What is the impact of the number of cylinders and condition on pricing?
3. Does the ad's validity period affect vehicle prices?
4. What are the average price trends across different vehicle types (e.g., SUV, Sedan)?

## Data Description

The dataset used in this project includes the following attributes:

- **`price`:** Vehicle price in USD.
- **`model_year`:** Year the vehicle model was manufactured.
- **`model`:** Vehicle model name.
- **`condition`:** Vehicle condition (e.g., excellent, good, fair).
- **`cylinders`:** Number of cylinders in the vehicle engine.
- **`fuel`:** Type of fuel used by the vehicle (e.g., gas, diesel).
- **`odometer`:** Vehicle mileage when the ad was shown.
- **`transmission`:** Type of transmission (e.g., automatic, manual).
- **`paint_color`:** Color of the vehicle.
- **`is_4wd`:** Whether the vehicle has 4-wheel drive (Boolean type).
- **`date_posted`:** Date when the ad was posted.
- **`days_listed`:** Number of days the ad was shown until it was removed.

## Project Workflow

1. **Data Import and Initial Exploration**  
   - Import the dataset and libraries.  
   - Explore the data structure, types, and missing values.  

2. **Data Preprocessing**  
   - Handle missing values and inconsistencies.  
   - Correct data types and improve quality.  

3. **Core Parameter Analysis**  
   - Analyze key factors like price, age, mileage, cylinders, and condition.  
   - Handle outliers to refine data accuracy.  

4. **Ad Validity Period Analysis**  
   - Explore the relationship between ad validity and pricing.  

5. **Price Factor Analysis**  
   - Determine average price trends for different vehicle types (e.g., SUVs, sedans).  

6. **Conclusion**  
   - Summarize insights and provide actionable recommendations.  

## Tools and Technologies

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, SciPy  

## Usage

1. Clone the repository.  
2. Ensure the dataset is in the same folder as the project file.  
3. Open the `.ipynb` file and execute the cells in a Jupyter Notebook environment.  

## Conclusion

This project aims to provide Crankshaft List with actionable insights into the used vehicle market, helping them make data-driven decisions to optimize pricing strategies and improve customer engagement.

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

