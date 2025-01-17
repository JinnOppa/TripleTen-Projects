# Automated Sentiment Analysis for IMDB Movie Reviews

## Introduction

With the growing reliance on online reviews for decision-making, businesses and consumers alike turn to platforms like IMDB for insights into movie sentiment. Understanding customer sentiment is critical in guiding marketing strategies, improving customer engagement, and gaining a competitive edge. This project aims to build an automated system to analyze the sentiment of movie reviews from IMDB, classifying them as positive or negative.

### Aim:
The primary goal of this project is to develop a machine learning model that can accurately classify IMDB movie reviews into positive or negative sentiments. This automated analysis will save time, reduce bias, and provide actionable insights for stakeholders.

### Objectives:
- **Data Preprocessing**: Clean and preprocess the text data to make it suitable for analysis.
- **Model Development**: Build a natural language processing (NLP) pipeline to classify reviews.
- **Performance Evaluation**: Evaluate the model using metrics like accuracy, precision, recall, and F1-score to ensure robustness.
- **Feature Engineering**: Leverage techniques such as word embeddings and Term Frequency-Inverse Document Frequency (TF-IDF) for better text representation.
- **Sentiment Prediction**: Use the best-performing model to predict sentiments on unseen data.

## Data Description

The dataset contains movie reviews from IMDB, stored in a **tab-separated values (.tsv)** file. Key columns in the dataset include:

- **`tconst`**: Unique identifier for the movie or title.
- **`title_type`**: Type of the title (e.g., movie, short, TV series).
- **`primary_title`**: The most commonly used title in English.
- **`original_title`**: The original title of the movie.
- **`start_year`**: Year the movie was released.
- **`end_year`**: Year the title ended (for series, otherwise null).
- **`runtime_minutes`**: Duration of the movie or title in minutes.
- **`is_adult`**: Whether the movie is marked as adult content (`1` for yes, `0` for no).
- **`genres`**: Genres associated with the title.
- **`average_rating`**: Average rating given to the movie.
- **`votes`**: Number of votes the movie received.
- **`review`**: The text of the movie review.
- **`rating`**: Reviewer rating of the movie.
- **`sp`**: Sentiment polarity (`pos` for positive, `neg` for negative).
- **`ds_part`**: Dataset split part (e.g., `train` or `test`).
- **`idx`**: Unique index for the dataset.

The dataset is stored in the `/imdb_reviews.tsv` file and consists of **50,000 rows** and **15 columns**.

## Project Workflow

### 1. Import Libraries and Load Data
- Import necessary libraries such as NLTK, Scikit-learn, Pandas, and TensorFlow/Keras.
- Load the dataset and explore its structure.

### 2. Data Preprocessing
- **Text Cleaning**: Remove HTML tags, punctuation, and special characters.
- **Tokenization**: Split text into words.
- **Stopwords Removal**: Remove commonly used words that do not contribute to sentiment analysis.
- **Stemming/Lemmatization**: Reduce words to their base forms.
- **Vectorization**: Convert text to numerical representations using techniques like TF-IDF or word embeddings (e.g., GloVe, Word2Vec).

### 3. Model Building
- **Train-Test Split**: Divide the dataset into training and testing subsets based on the `ds_part` column to ensure the separation aligns with predefined splits (`train` and `test`).
- **Model 0 - Constant**: 
    - Use a `DummyClassifier` as a baseline to predict the most frequent sentiment class (positive or negative).
    - This model serves as a benchmark for evaluating the performance of other models.
- **Model 1 - NLTK, TF-IDF, and Logistic Regression**:
    - **Text Preprocessing**: Use NLTK for tokenization and stopword removal.
    - **Feature Extraction**: Apply `TfidfVectorizer` to convert the reviews into numerical features.
    - **Classification**: Train a Logistic Regression model on the transformed data.
- **Model 3 - spaCy, TF-IDF, and Logistic Regression**:
    - **Text Preprocessing**: Use spaCy's `en_core_web_sm` model for tokenization and stopword removal.
    - **Feature Extraction**: Use `TfidfVectorizer` to extract features from the processed reviews.
    - **Classification**: Train a Logistic Regression model on the transformed features.
- **Model 4 - spaCy, TF-IDF, and LGBMClassifier**:
    - **Text Preprocessing**: Use spaCy for tokenization and stopword removal.
    - **Feature Extraction**: Apply `TfidfVectorizer` for feature representation.
    - **Classification**: Use the LightGBM classifier (`LGBMClassifier`) for sentiment classification.
    - **Hyperparameter Tuning**: Use `GridSearchCV` to fine-tune parameters such as:
        - `n_estimators`: Number of boosting rounds.
        - `learning_rate`: Shrinkage rate for feature contribution.
- **Model 9 - BERT**:
    - **Tokenization**: Use the BERT tokenizer (`BertTokenizer`) to prepare the text for the model.
    - **Pre-trained Model**: Leverage the pre-trained `BertModel` from the Transformers library for extracting contextual embeddings.
    - **Fine-Tuning**: Fine-tune the BERT model for sentiment classification. This involves adding a classification head (e.g., a fully connected layer) on top of BERT's output and training it on the labeled data.
- **Hyperparameter Tuning**: Use `GridSearchCV` or `RandomizedSearchCV` to optimize model parameters.

### 4. Model Evaluation
- Evaluate models using metrics such as:
  - **Accuracy**
  - **Precision**
  - **Recall**
  - **F1-Score**
- Compare the models to determine the best-performing one based on the evaluation metrics.

### 5. Conclusion
- Summarize the findings, including the best model and its evaluation metrics.
- Provide insights into how the sentiment analysis can be applied to improve decision-making.

## Tools and Technologies

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, NLTK, Scikit-learn, TensorFlow, Keras, Matplotlib, Seaborn

## Usage

To run the project, follow these steps:

1. **Clone the repository** or download the project folder.
2. **Install required libraries**:
   - Open a terminal and install the necessary Python libraries:
     ```bash
     pip install pandas numpy nltk scikit-learn tensorflow keras matplotlib seaborn
     ```
3. **Run the Jupyter Notebook**:
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open the notebook `imdb_movie_review.ipynb` and run the cells to preprocess data, train models, and evaluate their performance.

## Conclusion

This project provides a sentiment analysis system for IMDB movie reviews, enabling quick and reliable sentiment classification. The model serves as a valuable tool for businesses, researchers, and consumers to analyze opinions and trends efficiently.


## MIT License

MIT License

Copyright (c) 2025 Eugene Winata

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.