import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional

class ChartFactory:
    """Create various chart types from data"""
    
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
        plt.style.use('dark_background')
    
    def create_bar_chart(self, x_column: str, y_column: str, title: str = "Bar Chart"):
        """
        Create a bar chart
        
        Args:
            x_column: Column for X-axis
            y_column: Column for Y-axis
            title: Chart title
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        self.df.plot(x=x_column, y=y_column, kind='bar', ax=ax, color='#00d4ff')
        ax.set_title(title, fontsize=14, color='#00d4ff', fontweight='bold')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        return fig
    
    def create_line_chart(self, x_column: str, y_column: str, title: str = "Line Chart"):
        """
        Create a line chart
        
        Args:
            x_column: Column for X-axis
            y_column: Column for Y-axis
            title: Chart title
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        self.df.plot(x=x_column, y=y_column, kind='line', ax=ax, color='#00d4ff')
        ax.set_title(title, fontsize=14, color='#00d4ff', fontweight='bold')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        return fig
    
    def create_pie_chart(self, column: str, title: str = "Pie Chart"):
        """
        Create a pie chart
        
        Args:
            column: Column to visualize
            title: Chart title
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        self.df[column].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
        ax.set_title(title, fontsize=14, color='#00d4ff', fontweight='bold')
        ax.set_ylabel('')
        return fig
    
    def create_scatter_plot(self, x_column: str, y_column: str, title: str = "Scatter Plot"):
        """
        Create a scatter plot
        
        Args:
            x_column: Column for X-axis
            y_column: Column for Y-axis
            title: Chart title
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        self.df.plot(x=x_column, y=y_column, kind='scatter', ax=ax, color='#00d4ff')
        ax.set_title(title, fontsize=14, color='#00d4ff', fontweight='bold')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        return fig
    
    def create_histogram(self, column: str, bins: int = 30, title: str = "Histogram"):
        """
        Create a histogram
        
        Args:
            column: Column to visualize
            bins: Number of bins
            title: Chart title
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        self.df[column].hist(bins=bins, ax=ax, color='#00d4ff', edgecolor='black')
        ax.set_title(title, fontsize=14, color='#00d4ff', fontweight='bold')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        return fig
    
    def create_box_plot(self, column: str, title: str = "Box Plot"):
        """
        Create a box plot
        
        Args:
            column: Column to visualize
            title: Chart title
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        self.df.boxplot(column=column, ax=ax)
        ax.set_title(title, fontsize=14, color='#00d4ff', fontweight='bold')
        ax.set_ylabel(column)
        return fig