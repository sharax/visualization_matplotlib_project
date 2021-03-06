# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    x=ipl_df.groupby('batsman')['runs'].sum()
    y=ipl_df.groupby('batsman')['delivery'].count()
    plt.scatter(y,x)
    plt.show()
#plot_runs_by_balls()
