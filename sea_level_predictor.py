import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    lineal_reg = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = lineal_reg.slope*x_pred + lineal_reg.intercept
    
    plt.plot(x_pred, y_pred, 'green')

    # Create second line of best fit
    df_fit = df.loc[df["Year"] >= 2000]
    
    lineal_reg_fit = linregress(df_fit["Year"], df_fit["CSIRO Adjusted Sea Level"])
    x_pred_fit = pd.Series([i for i in range(2000, 2051)])
    y_pred_fit = lineal_reg_fit.slope*x_pred_fit + lineal_reg_fit.intercept
    
    plt.plot(x_pred_fit, y_pred_fit, 'blue')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()