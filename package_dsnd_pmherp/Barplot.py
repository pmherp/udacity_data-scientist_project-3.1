#import the relevant libraries
from IPython import get_ipython
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set()

class Barplot():
    """
    The Bar class sets the ground for bar objects derived from it. With it, plotting nice bar charts becomes very easy!
    
    ATTRIBUTES:
        - x_values (list): list of all values plottet on x-axis
        - y_values (list): list of all values plottet on y-axis
        - x_label (string): name of x-axis
        - chart_title (string): title of bar chart
        - fig_width (int): width of figure
        - fig_height (int): height of figure
    """
    
    #define the __init__ of Bar
    def __init__(self, x_values, y_values, x_label, chart_title, fig_width=10, fig_height=6):
        self.x_values = x_values
        self.y_values = y_values
        self.x_label = x_label
        self.chart_title = chart_title
        self.fig_width = fig_width
        self.fig_height = fig_height
    
    
    #read in data file
    def read_data_file(self, file_name):
        """
        Function to read in data from a csv file and make it a pandas dataframe
        
        ARGS:
            - file_name (string): name of a file to read in
        OUTPUTS:
            - NONE
        """
        df = pd.read_csv(file_name)