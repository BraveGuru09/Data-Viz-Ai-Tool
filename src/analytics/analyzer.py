import pandas as pd
import numpy as np
from typing import Dict, List, Any

class DataAnalyzer:
    """Analyze data and generate insights"""
    
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
    
    def get_basic_stats(self) -> Dict[str, Any]:
        """
        Get basic statistics
        
        Returns:
            Dictionary of statistics
        """
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        stats = {
            "rows": len(self.df),
            "columns": len(self.df.columns),
            "numeric_summary": self.df[numeric_cols].describe().to_dict()
        }
        return stats
    
    def detect_outliers(self, column: str) -> List[int]:
        """
        Detect outliers using IQR method
        
        Args:
            column: Column to analyze
            
        Returns:
            List of outlier indices
        """
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        outliers = self.df[
            (self.df[column] < Q1 - 1.5 * IQR) | 
            (self.df[column] > Q3 + 1.5 * IQR)
        ].index.tolist()
        
        return outliers
    
    def calculate_trends(self, column: str) -> Dict[str, Any]:
        """
        Calculate trend information
        
        Args:
            column: Column to analyze
            
        Returns:
            Trend information
        """
        if len(self.df) < 2:
            return {"trend": "insufficient_data"}
        
        first_val = self.df[column].iloc[0]
        last_val = self.df[column].iloc[-1]
        change = last_val - first_val
        percent_change = (change / first_val * 100) if first_val != 0 else 0
        
        return {
            "start_value": first_val,
            "end_value": last_val,
            "change": change,
            "percent_change": percent_change,
            "trend": "up" if change > 0 else "down"
        }
    
    def get_column_insights(self, column: str) -> Dict[str, Any]:
        """
        Get insights about a specific column
        
        Args:
            column: Column to analyze
            
        Returns:
            Column insights
        """
        insights = {
            "column": column,
            "dtype": str(self.df[column].dtype),
            "unique_values": self.df[column].nunique(),
            "missing_values": self.df[column].isnull().sum()
        }
        
        if self.df[column].dtype in ['int64', 'float64']:
            insights["mean"] = self.df[column].mean()
            insights["median"] = self.df[column].median()
            insights["std"] = self.df[column].std()
        
        return insights