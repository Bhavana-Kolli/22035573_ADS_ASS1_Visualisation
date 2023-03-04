#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
7PAM2000 Applied Data Science 1
Assignment 1: Visualisation

@author: Bhavana Kolli - 22035573
"""

# Here modules are imported

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Here functions for all plots are defined

def filter_data(data, country):
    """
    Filter the data to only include matches where the specified country 
    played as the home team.

    Args:
        data(pandas.DataFrame): The input data.
        country(str): The name of the country to filter the data by.
    """
    
    # Filters the data of the country.
    filtered_data = data.loc[data['home_team'] == country]
    # Extract year from date and create new column.
    filtered_data['year'] = pd.to_datetime(filtered_data['date']).dt.year
    # Aggregates the goals scored by year
    filtered_data = filtered_data.groupby('year').agg({'home_score': 'sum'}).reset_index()
    return filtered_data


def create_line_plot(data, countries):
    """
    Create a line plot of the number of goals scored by each country over the years.

    Args:
        data(pandas.DataFrame): The input data.
        countries (list of str): The names of the countries to include in the plot.
    """
    # Plot the line plot for countries in the string
    for country in countries:
        filtered_data = filter_data(data, country)
        plt.plot(filtered_data['year'], filtered_data['home_score'], label=country)
    
    # set the upper and lower limits of x
    plt.xlim(1900, 2020)
    
    # Set labels, title to the plot.
    plt.xlabel('Years')
    plt.ylabel('Goals Scored')
    plt.title('Number of Goals Scored by Countries Over the Years')
    # show legend
    plt.legend()
    plt.show()


# Main Program

# read CSV file into dataframe and print
data = pd.read_csv("results.csv")
print(data)
# Countries for which we have plot lineplot
countries = ['Brazil', 'England', 'Spain']
# Call the above function for plotting
create_line_plot(data, countries)

