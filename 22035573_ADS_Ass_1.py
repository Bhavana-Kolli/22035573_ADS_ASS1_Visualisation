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
    filtered_data = filtered_data.groupby('year').agg({'home_score': 
                                                       'sum'}).reset_index()
    return filtered_data


def create_line_plot(data, countries):
    """
    Create a line plot of the number of goals scored 
    by each country over the years.

    Args:
        data(pandas.DataFrame): The input data.
        countries(list of str): The names of countries to include in plot.
    """
    # Plot the line plot for countries in the string
    plt.figure()
    for country in countries:
        filtered_data = filter_data(data, country)
        plt.plot(filtered_data['year'], filtered_data['home_score'], 
                 label=country)
    
    # set the upper and lower limits of x
    plt.xlim(1900, 2020)
    # Set labels, title to the plot.
    plt.xlabel('Years')
    plt.ylabel('Goals Scored')
    plt.title('Number of Goals Scored by Countries Over the Years')
    # show legend
    plt.legend()
    plt.show()


def plot_histogram(data, variable):
    """
    Create a histogram of a given variable in a DataFrame.
    
    Args:
        data(pandas.DataFrame): The input data.
        variable (str): The name of the variable to create a histogram for.
    """
    
    # Plot the distribution as a histogram with 30 bins
    plt.figure(figsize=(8,6))
    plt.hist(data[variable], bins=30, label="medv", density=True, 
             alpha=0.7, color='orange')
    # Set labels, title to the plot.
    plt.title("Distribution of Median Home Values in Boston")
    plt.xlabel("Median value of owner-occupied homes in $1000s")
    plt.ylabel("Frequency")
    # show legend
    plt.legend()
    plt.show()
    

# Main Program


# PLOT-1 (LINE PLOT)-------------------------------------------------------


# read CSV file into dataframe and print
df_data_lp = pd.read_csv("results.csv")
print(df_data_lp)

# Countries for which we have plot lineplot
countries = ['Brazil', 'England', 'Spain']

# Call the create_line_plot function for the data
create_line_plot(df_data_lp, countries)


# PLOT-2 (HISTOGRAM)-------------------------------------------------------


# Load the dataset from the URL into dataframe
url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'
df_data_hp = pd.read_csv(url)

# Print the dataframe
print(df_data_hp)

# Extract 'medv' variable and print it
df_medv = df_data_hp['medv']
print("Median value of owner-occupied homes in $1000s in Boston")
print(df_medv)

# Call the plot_histogram function for 'medv' variable in dataset
plot_histogram(df_data_hp, 'medv')

