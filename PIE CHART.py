# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 23:51:34 2023

@author: Dhairya Shah
"""

"""
  Create a pie chart of renewable energy consumption for different countries from 1994 to 2019.
  Parameters:
  data_path (str): The file path of the CSV file containing the data.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("D:\Dhairyakumar\Renewable energy Pie.csv")

# Group data by category and sum values from 1994 to 2019

grouped_data = data.groupby('Country Name')['2019'].sum()

# Set labels for pie chart
labels = grouped_data.index

# Set values for pie chart
values = grouped_data.values

# Set explode values for each slice
explode = [0.022] * len(labels) # explode each slice by 0.

# Set colors for each slice
colors = ['silver','yellowgreen','gold','green',"red","grey","orange"]

# Plot the pie chart
plt.pie(values, labels=labels, explode=explode, colors=colors,
        autopct='%1.1f%%', startangle=90)

# Add title to the chart
plt.title('Renewable energy consumption 1994 to 2019',fontweight ='bold', color="purple")

# Show the chart
plt.show()