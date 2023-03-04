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
    Returns:
        pandas.DataFrame: The filtered data.
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
    
    # show legend and display the plot
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
    
    # show legend and display the plot
    plt.legend()
    plt.show()
    

def create_boxplot(df, group_var, value_var):
    """
    Create a box plot of value_var variable grouped by group_var variable.

    Args:
        df(pd.DataFrame): The input DataFrame.
        group_var(str): The name of the variable to group by on the x-axis.
        value_var(str): The name of the variable to plot on the y-axis.
    """

    # create a new DataFrame with only the two variables of interest
    data = df[[group_var, value_var]]

    # create a list of the unique group values
    group_values = data[group_var].unique()

    # create a list of boxplot data, one for each group
    boxplot_data = [data[data[group_var] == group][value_var] 
                    for group in group_values]

    # create a boxplot using Matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Adding colors to boxplot
    bp = dict(linestyle='-', linewidth=2.5, color='red')
    wp = dict(linestyle='--', linewidth=1.5, color='black')
    cp = dict(linestyle='-', linewidth=1.5, color='black')
    mp = dict(linestyle='-', linewidth=2.5, color='green')
    fp = dict(marker='o', markerfacecolor='blue', markersize=8, alpha=0.5)
    
    # Plot the boxplot according to above details
    ax.boxplot(boxplot_data, boxprops=bp, whiskerprops=wp, capprops=cp, 
               medianprops=mp, flierprops=fp)

    # set the x-axis tick labels to be the group values
    ax.set_xticklabels(group_values)
    
    # set x-axis and y-axis labels
    ax.set_xlabel("Index of accessibility to radial highways")
    ax.set_ylabel("Median value of owner-occupied homes in $1000s")

    # add a title to the plot
    ax.set_title(f'Boxplot of {value_var} grouped by {group_var}')

    # display the plot
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


# PLOT-3 (BOXPLOT)-------------------------------------------------------


# Load the dataset from the URL into dataframe
df_data_bp = pd.read_csv(url)

# Call the create_boxplot function for 'rad', 'medv' variable in dataset
create_boxplot(df_data_bp, 'rad', 'medv')



