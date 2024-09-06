# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
import streamlit as st  # For creating web applications
import matplotlib.pyplot as plt  # For creating static, interactive, and animated visualizations

# Define column names for the DataFrame
col_names = ['column1', 'column2', 'column3']

# Create a DataFrame with random integers between 0 and 30, with 30 rows and 3 columns
data = pd.DataFrame(np.random.randint(30, size=(30, 3)), columns=col_names)

# Display a line graph of the DataFrame using Streamlit
'line graph:'
st.line_chart(data)

# Display a bar graph of the DataFrame using Streamlit
'bar graph:'
st.bar_chart(data)

# Define labels and values for the pie chart
animals = ['cat', 'cow', 'dog']  # Labels for the pie chart
heights = [30, 150, 80]  # Values corresponding to each label

# Create a pie chart using Matplotlib
'pie chart:'
fig, ax = plt.subplots()  # Create a figure and a set of subplots
ax.pie(heights, labels=animals)  # Plot the pie chart with the specified labels

# Display the pie chart using Streamlit
st.pyplot(fig)