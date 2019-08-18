"""
Data visualization functions to simplify plots in Seaborn.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def _get_steps(df, ax, width):
    """Properly spaces values in x-axis."""
    steps = ( ( df[ax].max() - df[ax].min() ) / width / 10 )
    steps = max(int(round(steps)), 1)
    return steps


def get_scatterplot(df, x, y, height=5, width=5, hue=None):
    """Create a scatterplot using Seaborn. 
    """
    p = sns.catplot(
        x=x, 
        y=y, 
        hue=hue, 
        kind="swarm", 
        data=df,
        height=height,
        aspect=width/height,
        #palette="Set1",
        palette=sns.color_palette(['blue', 'grey'])
    )
    step = _get_steps(df, x, width)
    p.set_xticklabels(rotation=90, step=step)
    p.fig.suptitle("Scatterplot: {} vs {}".format(x, y))
    return p


def get_historgram(df, x, height=5, width=5, bins=20):
    """Create a histogram plot using Seaborn
    Docs: https://seaborn.pydata.org/tutorial/distributions.html
    """
    fig, ax = plt.subplots()
    fig.set_size_inches(width, height)
    p = sns.distplot(
        df[x], 
        bins=bins,
        kde=False,
        #hue=None,
        color='blue',
    )
    p.set(title = "Histogram: {}".format(x))
    return p


def get_boxplot(df, x, y, height=5, width=5):
    """Create a boxplot using Seaborn
    """
    fig, ax = plt.subplots()
    fig.set_size_inches(width, height)
    p = sns.boxplot(x=x, y=y, data=df)
    p.set(title = "Box Chart: {} vs {}".format(x, y))
    return p


def get_bar_chart(df, x, y, height=5, width=5):
    """Create a bar chart using Seaborn
    """
    p = sns.catplot(
        x=x, y=y, kind='bar',
        data=df,
        height=height,
        aspect=width/height,
    )
    p.set_xticklabels(rotation=90, step=1)
    p.fig.suptitle("Bar Chart: {} vs {}".format(x, y))
    return p


