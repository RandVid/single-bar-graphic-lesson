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
    platform_order = []

    """ Draw the plot """
    plot = sns.catplot(
        data=df,
        x=,
        hue=,
        kind='count',
        order=,
        height=,  # controls the height of the plot in inches
        aspect=  # controls the width of the plot
    )

    """ save the plot """
    plot.
    return plot
