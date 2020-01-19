
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FILL_COLOR = '#ff975790'
LINE_COLOR = '#e34234'

QUANTILES = 20


def plot_performance_df(df, label='Performance', ax1=None, ax2=None):
    '''Plots the ability of the classifier to predict good/bad children'''
    
    # define name of index column for convenience
    index = 'FunctionEvaluation'

    # sort by function evaluation
    df = df.sort_values(index)

    # create 10 bins
    df['quantile'] = pd.qcut(df[index], q=QUANTILES)

    # group by the bins
    grouped = df.groupby('quantile')

    # find the mean of each bin
    means = grouped.mean()

    # find the standard deviation of each bin
    stds = grouped.std()

    # convenience for accessing columns
    good_perc = 'GoodPredictorPercentage'
    bad_perc = 'BadPredictorPercentage'

    # Upper/lower ounds of good predictor percentages
    good_upper = means[good_perc] + stds[good_perc]
    good_lower = means[good_perc] - stds[good_perc]

    # switch axis based on input value
    if ax1 is None:
        ax1 = plt
        ax1_arg = None
    else:
        ax1_arg = ax1

    # good predictor figure
    ax1.fill_between(means[index], good_upper, good_lower, color=FILL_COLOR)
    means.plot(x=index, y='GoodPredictorPercentage', c=LINE_COLOR, ax=ax1_arg)

    # axis settings
    ax1.set_ylim(0,1)
    ax1.set_title('Classifier Accuracy of Predicting Good Children')
    ax1.set_xlabel('Function Evaluation')
    ax1.set_ylabel('Percentage')

    # Upper/lower ounds of bad predictor percentages
    bad_upper = means[bad_perc] + stds[bad_perc]
    bad_lower = means[bad_perc] - stds[bad_perc]

    # switch axis based on input value
    if ax2 is None:
        ax2 = plt
        ax2_arg = None
    else:
        ax2_arg = ax2

    # bad predictor figure
    ax2.fill_between(means[index], bad_upper, bad_lower, color=FILL_COLOR)
    means.plot(x=index, y='BadPredictorPercentage', c=LINE_COLOR, ax=ax2_arg)

    # axis settings
    ax2.set_ylim(0,1)
    ax2.set_title('Classifier Accuracy of Predicting Bad Children')
    ax2.set_xlabel('Function Evaluation')
    ax2.set_ylabel('Percentage')
    
    
