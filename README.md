# Data-Visualizations-
Learned how to use Seaborn and Matplotlib to create insightful data visualizations.

# Loan and Iris Data Visualizations Using Matplotlib

## Overview
This project explores data visualization techniques using Python's Seaborn and Matplotlib libraries. Two datasets are analyzed: a loan dataset containing financial information related to loans and an Iris dataset containing flower measurements. Various visualizations are created to identify trends and insights in both datasets.

## Purpose
The purpose of this project is to enhance data analysis skills by creating meaningful visualizations. By applying different types of charts, such as bar plots, box plots, histograms, and scatter plots, we aim to uncover patterns in loan interest rates, loan default rates, and relationships among Iris flower species characteristics.

## Files
- **loan_data_visualizations.py**: Python code for visualizing loan data

- **iris_visualizations.py**: Python code for visualizing Iris dataset
- **Copilotchat**: Copiolt help

## Datasets
The Loan Dataset is used from Kaggle 
https://www.kaggle.com/datasets/prakashraushan/loan-dataset
- **Features**: Loan amount, interest rate, loan grade, home ownership, loan intent, and loan default status

Iris Dataset
- **Features**: Sepal length, sepal width, petal length, petal width, and species classification


## Libraries Used
- Pandas as pd
- Seaborn as sns
- Matplotlib.pyplot as plt
- Sklearn. datasets 
- Os 

## Visualizations
Loan Data
- **Bar Plot (Loan Intent Distribution)**: Displays the distribution of loan purposes
- **Box Plot (Interest Rates by Loan Grade)**: Shows interest rate differences across loan grades
- **Stacked Bar Chart (Loan Default by Home Ownership)**: Analyzes default rates among homeowners and renters

Iris Data
- **Bar Plot (Average Sepal & Petal Width by Species)**: Compares sepal and petal width across species
- **Histogram (Petal Length Distribution by Species)**: Displays the spread of petal lengths among species
- **Scatter Plot (Sepal Length vs Sepal Width)**: Visualizes relationships between sepal dimensions with regression lines

## Project Structure
- **Data Preparation**:
- The loan dataset is loaded and cleaned to ensure numerical consistency
- The Iris dataset is loaded directly using Scikit-learn

- **Visualization and Analysis**:
- Each dataset is explored using appropriate visualization techniques
- Charts are analyzed to identify key trends and insights

- **Insights**
- Loan intent varies significantly, with education being the most common reason for borrowing
- Interest rates tend to be higher for lower loan grades, highlighting financial risk
- Homeowners are more likely to default on loans compared to renters
- The Iris dataset shows distinct patterns among species, with significant differences in petal and sepal measurements

## Limitations
- The loan dataset may not be representative of all lending institutions
- Class imbalance in the loan dataset may misrepresent real trends
- The Iris dataset is well-balanced, but findings are limited to these specific species
