import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from import_func import *

def draw_graph():
    """ Import the dataset"""
    df = import_dataset()



    """ Set the style of the plot """
    sns.set_style("darkgrid")

    """ Set the order of platforms """
    platform_order = ['PS4', 'XOne', 'PC', 'WiiU']

    """ Draw the plot """
    plot = sns.catplot(
        data=df,
        x=df.platform,
        hue=df.genre,
        kind='count',
        order=platform_order,
        height=5,  # controls the height of the plot in inches
        aspect=16 / 10  # controls the width of the plot
    )

    """ save the plot """
    # plot.savefig('plot.png')
    return plot
