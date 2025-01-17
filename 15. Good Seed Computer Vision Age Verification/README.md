# Good Seed Age Verification System

## Introduction

Ensuring compliance with age restrictions is critical for businesses in industries such as alcohol sales, gambling, and content distribution. The **Good Seed Age Verification System** is designed to automate and simplify the process of verifying the age of individuals using advanced image processing and machine learning techniques. This project provides a secure and efficient solution to help businesses maintain regulatory compliance and prevent underage access to restricted goods or services.

### Aim:
The primary goal of this project is to develop an automated age verification system capable of accurately determining whether an individual meets the required age threshold based on image data.

### Objectives:
- **Data Collection**: Gather a diverse dataset of images representing various age groups.
- **Data Preprocessing**: Prepare the data for training, including face detection, alignment, and normalization.
- **Model Development**: Build and train a deep learning model to predict the age of individuals.
- **Performance Evaluation**: Assess model performance using accuracy, precision, recall, and other relevant metrics.
- **Deployment**: Create a user-friendly interface for real-time age verification.

## Data Description

The dataset used for this project consists of labeled images, each representing a person's age. Key components of the dataset include:

- **`image_id`**: Unique identifier for the image file.
- **`age`**: The actual age of the person in the image.
- **`gender`**: The gender of the individual (`Male`, `Female`).
- **`dataset_split`**: Indicates whether the image belongs to the training, validation, or testing set.
- **`image_file_path`**: Path to the image file.

The dataset contains images stored in a structured directory format, with separate folders for training, validation, and testing. It is preprocessed to ensure consistency in image size and quality.

## Project Workflow

### 1. Import Libraries and Load Data
- Import essential libraries such as TensorFlow/Keras, OpenCV, Pandas, and NumPy.
- Load the dataset and inspect its structure.

### 2. Data Preprocessing
- **Face Detection**: Use a pre-trained face detection model (e.g., Haar cascades, MTCNN) to detect and crop faces from images.
- **Image Resizing**: Resize images to a consistent dimension for model input.
- **Data Augmentation**: Apply transformations like rotation, flipping, and brightness adjustment to increase dataset diversity.
- **Normalization**: Normalize pixel values to improve model training efficiency.

### 3. Model Building
- **Model 0 - Baseline**:
    - Use a simple convolutional neural network (CNN) for initial age prediction.
- **Model 1 - Transfer Learning with VGG16**:
    - Fine-tune the VGG16 model pre-trained on ImageNet for age prediction.
- **Model 2 - Transfer Learning with ResNet50**:
    - Utilize ResNet50 for its deeper architecture and feature extraction capabilities.
    - Train the model on the preprocessed dataset and evaluate performance.
- **Model 3 - Custom CNN Architecture**:
    - Design and train a custom CNN tailored to the dataset characteristics.
- **Hyperparameter Tuning**: Optimize parameters such as learning rate, batch size, and number of layers using tools like GridSearchCV or Optuna.

### 4. Model Evaluation
- Evaluate the models using metrics such as:
  - **Mean Absolute Error (MAE)**
  - **Accuracy within a tolerance range**
  - **Precision and Recall**
- Compare the performance of models to identify the best architecture.

### 5. Deployment
- Develop a real-time age verification system using a Streamlit-based web application.
- Features include:
  - Uploading images for verification.
  - Displaying predicted age and decision (e.g., "Approved" or "Not Approved").
  - Logging verified entries for auditing purposes.

## Tools and Technologies

- **Programming Language:** Python  
- **Libraries:** TensorFlow, Keras, OpenCV, NumPy, Pandas, Matplotlib, Seaborn, Streamlit

## Usage

To run the project, follow these steps:

1. **Clone the repository** or download the project folder.
2. **Install required libraries**:
   - Open a terminal and install the necessary Python libraries:
     ```bash
     pip install tensorflow keras opencv-python-headless pandas numpy matplotlib seaborn streamlit
     ```
3. **Train the Model**:
   - Run the training script to train and save the model:
     ```bash
     python run_model_on_gpu.py
     ```
4. **Run the Jupyter Notebook**:
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open the notebook `age_detection.ipynb` and run the cells to preprocess data, train models, and evaluate their performance.

## Conclusion

The **Good Seed Age Verification System** demonstrates how image processing and machine learning can automate age verification, providing businesses with a reliable and efficient tool for regulatory compliance. By combining advanced deep learning models with a user-friendly interface, the system is well-suited for real-world applications.

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
