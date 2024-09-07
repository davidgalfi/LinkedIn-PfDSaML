# Import necessary libraries
import time  # For adding delays in the loop
import pandas as pd  # For data manipulation (not used directly here but imported for potential future use)
import numpy as np  # For numerical operations
import streamlit as st  # For creating web applications
import matplotlib.pyplot as plt  # For creating static, interactive, and animated visualizations

# Initialize a DataFrame with a single random value
rows = np.random.randn(1,1)

# Display a dynamic line chart using Streamlit
'Growing Line Chart:'
chart = st.line_chart(rows)  # Create an initial line chart with the first random value

# Update the line chart with new random values in a loop
for i in range(1, 100):
    new_rows = rows[0] + np.random.randn(1,1)  # Generate a new random value based on the previous value
    chart.add_rows(new_rows)  # Add the new value to the line chart
    rows = new_rows  # Update the current value
    time.sleep(0.05)  # Pause for 0.05 seconds before the next iteration

# Generate random values for a static line chart
values = np.random.randn(10)

# Display a static line chart using Matplotlib
'Matplotlib Line Chart:'
fig, ax = plt.subplots()  # Create a figure and a set of subplots
ax.plot(values)  # Plot the random values on the line chart
st.pyplot(fig)  # Display the Matplotlib chart using Streamlit