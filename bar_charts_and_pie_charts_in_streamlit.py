# Import necessary libraries
import pandas as pd  # For data manipulation (not used directly here but imported for potential future use)
import numpy as np  # For numerical operations
import streamlit as st  # For creating web applications
import matplotlib.pyplot as plt  # For creating static, interactive, and animated visualizations

# Define data for animals, their heights, and weights
animals = ['cat', 'cow', 'dog', 'goat']  # Labels for the charts
heights = [30, 150, 80, 60]  # Heights corresponding to each animal
weights = [5, 400, 40, 50]  # Weights corresponding to each animal

# Create a figure and a set of subplots for the bar chart
fig, ax = plt.subplots()

# Define positions for the bars
x = np.arange(len(heights))  # Create an array with the positions for each bar
width = 0.40  # Define the width of the bars

# Plot the bars for heights and weights
ax.bar(x-0.2, heights, width, color="red")  # Plot heights with red bars
ax.bar(x+0.2, weights, width, color="orange")  # Plot weights with orange bars

# Add a legend to the bar chart
ax.legend(["Height", "Weight"])

# Set the x-ticks and their labels
ax.set_xticks(x)
ax.set_xticklabels(animals)

# Display the bar chart using Streamlit
st.pyplot(fig)

# Define explode values for the pie chart of heights
explode = [0.1, 0.05, 0.1, 0.1]

# Create a figure and a set of subplots for the pie chart of heights
plot_pie, ax = plt.subplots()
ax.pie(heights, labels=animals, explode=explode, autopct='%1.1f%%', shadow=True)  # Plot the pie chart with specified explode values and percentage display
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Display the pie chart for heights using Streamlit
st.pyplot(plot_pie)

# Define explode values for the pie chart of weights
explode = [0.4, 0.3, 0.2, 0.2]

# Create a figure and a set of subplots for the pie chart of weights
plot_pie, ax = plt.subplots()
ax.pie(weights, labels=animals, explode=explode, autopct='%1.1f%%', shadow=True)  # Plot the pie chart with specified explode values and percentage display
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Display the pie chart for weights using Streamlit
st.pyplot(plot_pie)