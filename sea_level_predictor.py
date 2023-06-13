import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
  # Read data from file

  df = pd.read_csv('epa-sea-level.csv')
  # Create scatter plot
  fig, ax = plt.subplots(1, 1)
  scat = plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level', s=3)

  # Create first line of best fit
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']
  m = linregress(x, y)
  x_fit = np.arange(min(df['Year']), 2051)
  y_fit = x_fit * m[0] + m[1]
  ax.plot(x_fit, y_fit)

  # Create second line of best fit
  x1 = df[df['Year'] >= 2000]['Year']
  y1 = [df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']]
  m1 = linregress(x1, y1)
  x1_fit = np.arange(2000, 2051)
  y1_fit = x1_fit * m1[0] + m1[1]
  ax.plot(x1_fit, y1_fit, 'g')

  # Add labels and title
  ax.set(xlabel='Year', ylabel='Sea Level (inches)', title='Rise in Sea Level')

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
