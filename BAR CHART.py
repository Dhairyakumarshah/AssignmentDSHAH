import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_data(file_path):
    """
    To read data from a CSV file and return to a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The data from the CSV file.
    """
    data = pd.read_csv(file_path)
    return data


def create_bar_chart(data, x_label, y_label, title, legend_labels):
    """
    This function creates a bar chart using the given data and displays it.

    Args:
        data (pd.DataFrame): The data to use for the chart.
        x_label (str): The label for the x-axis.
        y_label (str): The label for the y-axis.
        title (str): The title of the chart.
        legend_labels (list[str]): The labels for the legend.

    Returns:
        None
    """
    #plot parameters
    plt.figure(figsize=(15, 8))
    num_years = data.shape[0]
    ind = np.arange(num_years)
    width = 0.25

    # Extract data for every country
    india_data = data["India"]
    uk_data = data["United Kingdom"]
    us_data = data["United States"]

    # to Create bar chart for contries
    india_bars = plt.bar(ind, india_data, width, color='y')
    uk_bars = plt.bar(ind+width, uk_data, width, color='g')
    us_bars = plt.bar(ind+width*2, us_data, width, color='b')

    #labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Set x-axis tick labels
    plt.xticks(ind, data["Time"])

    # Add legend to the chart
    plt.legend((india_bars, uk_bars, us_bars), legend_labels)

    # Display the chart
    plt.show()


# Example usage
if __name__ == "__main__":
    data = read_data("D:\Dhairyakumar\Data for bar.csv")
    create_bar_chart(data, "Year", "Ratio in percentage(%)", "Armed forces personnel (% of total labor force)",
                     ['India', 'United Kingdom', 'United States'])
