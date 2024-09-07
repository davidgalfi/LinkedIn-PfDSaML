# Import necessary libraries
import streamlit as st  # For creating web applications
import pandas as pd  # For data manipulation
import matplotlib.pyplot as plt  # For creating visualizations
import seaborn as sns  # For statistical data visualization
from sklearn.datasets import load_iris  # For loading the Iris dataset

# Load the Iris dataset
iris_data = load_iris()

# Create a DataFrame from the dataset
data = pd.DataFrame(iris_data['data'], columns=iris_data['feature_names'])

# Create a histogram of the Iris dataset using seaborn
fig = plt.figure(figsize=(10, 7))  # Define the figure size
sns.histplot(data=data, bins=20)  # Plot the histogram with 20 bins
st.pyplot(fig)  # Display the plot using Streamlit

# Create a box plot of the Iris dataset using seaborn
fig = plt.figure(figsize=(10, 7))  # Define the figure size
sns.boxplot(data=data)  # Plot the box plot
st.pyplot(fig)  # Display the plot using Streamlit

# Create a scatter plot of the Iris dataset using seaborn
fig = plt.figure(figsize=(10, 7))  # Define the figure size
sns.scatterplot(data=data)  # Plot the scatter plot
st.pyplot(fig)  # Display the plot using Streamlit