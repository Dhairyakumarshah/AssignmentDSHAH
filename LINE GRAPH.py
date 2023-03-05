# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 23:31:21 2023

@author: Dhairya Shah
"""

import matplotlib.pyplot as plt
import pandas as pd

"""
 Creates a line plot from a CSV file.
 
 Args:
     csv_file_path (str): The path to the CSV file.
     x_column_name (str): The name of the column to use for the x-axis.
     y_column_name (str): The name of the column to use for the y-axis.
     
 """
 
def line(df, a, b, c, d, e):
    """
    Parameters
    ----------
    df : dataframe which read data from selected file.
    [ a , b , c , d , e ] is represents each country and help for labeling


    Returns
    -------
    None.

    """
    # Create a line chart
    plt.plot(df['Years'], df[a], label=a)
    plt.plot(df['Years'], df[b], label=b)
    plt.plot(df['Years'], df[c], label=c)
    plt.plot(df['Years'], df[d], label=d)
    plt.plot(df['Years'], df[e], label=e)


    # Add a legend
    plt.legend(loc='upper left')

    # Add labels and title with fontsize
    plt.xlabel('Time',fontweight ='bold')
    plt.ylabel('Total Numbers of People',fontweight ='bold',)
    plt.title('Secure internet server in 5 Countries', fontweight ='bold')
    plt.legend(facecolor='green', framealpha=0.4,
    fontsize='small')
    
    # Show the plot
    plt.show()



# Load the data from a CSV file
df = pd.read_csv("D:\Dhairyakumar\Ssl usage.csv")
line(df, "United States", "United Kingdom","Japan","India","Germany")