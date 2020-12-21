#import the relevant libraries
from IPython import get_ipython
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set()

#import Class Barplot
from .Barplot import Barplot

#make a horizontal barplot class which inherits from Barplot
class Horizontalbar(Barplot):
    """
    Horizontal bar chart class for plotting horizontal bar charts that look nice
    """
    
    #define the __init__
    def __init__(self):
        Barplot.__init__(self, x_values, y_values, x_label, chart_title, fig_width=10, fig_height=6)
    
    
    #creating a horizontal barchart
    def plot_bar_h(self):
        """
        Function for creating nice looking bar charts with horizontal figs. 
        To be stored in three variables barplot, fix, ax
    
        ARGS:
            - x_values: column in dataframe to be plotted on x-axis
            - y_values: column in dataframe to be plotted on y-axis
            - x_label: Label for x-axis
            - chart_title: title for whole bar chart
            - figwidth: width of each figure in the bar chart
            - figheight: height of each figure in the bar chart
    
        OUTPUTS:
            - barplot: type of chart is bar chart
            - fig: the figure in the chart
            - ax: axis-element, which is necessary for running the autolabel-function
        """
        fig, ax = plt.subplots(figsize=(fig_width,fig_height))
    
        #src: http://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
        plt.style.use('fivethirtyeight')
    
        # set labels
        ax.set_xlabel(x_label, fontsize=15, fontweight='black', color='#333F4B')
    
        # set axis
        ax.tick_params(axis='both', which='major', labelsize=12)
    
        #plot the bar
        barplot=ax.barh(x_values, y_values)
    
        #set bar chart title
        ax.set_title(chart_title,fontsize=15, fontweight='black', color = '#333F4B')
    
        return barplot, fig, ax
    
    
    #This example shows a how to create a grouped bar chart and how to annotate bars with labels automatically
    #https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html
    def autolabel(self, rects, ax):
        """
        Attach a text label above each bar in *rects*, displaying its height.
        
        ARGS:
            - rects: barplot that was made with plot_bar_h()
            - ax: that was made with plot_bar_h()
        """
    
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(round(height,2)), fontsize=12,
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')