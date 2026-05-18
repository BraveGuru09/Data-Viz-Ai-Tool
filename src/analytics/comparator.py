import pandas as pd
from typing import List, Dict, Any

class FileComparator:
    """Compare multiple data files"""
    
    def __init__(self):
        self.files = {}
    
    def add_file(self, name: str, dataframe: pd.DataFrame):
        """
        Add a file for comparison
        
        Args:
            name: File name/identifier
            dataframe: DataFrame to compare
        """
        self.files[name] = dataframe
    
    def compare_structure(self) -> Dict[str, Any]:
        """
        Compare file structures
        
        Returns:
            Structure comparison
        """
        comparison = {}
        for name, df in self.files.items():
            comparison[name] = {
                "rows": len(df),
                "columns": len(df.columns),
                "column_names": list(df.columns)
            }
        return comparison
    
    def compare_numeric_columns(self) -> Dict[str, Any]:
        """
        Compare numeric columns across files
        
        Returns:
            Numeric comparison
        """
        comparison = {}
        for name, df in self.files.items():
            numeric_cols = df.select_dtypes(include=['number']).columns
            comparison[name] = df[numeric_cols].describe().to_dict()
        return comparison
    
    def get_growth_metrics(self) -> Dict[str, Any]:
        """
        Calculate growth metrics between files
        
        Returns:
            Growth metrics
        """
        if len(self.files) < 2:
            return {"error": "At least 2 files required"}
        
        file_list = list(self.files.items())
        metrics = {}
        
        for i in range(len(file_list) - 1):
            name1, df1 = file_list[i]
            name2, df2 = file_list[i + 1]
            
            numeric_cols = df1.select_dtypes(include=['number']).columns
            
            growth = {}
            for col in numeric_cols:
                try:
                    growth[col] = {
                        name1: df1[col].sum(),
                        name2: df2[col].sum(),
                        "growth": ((df2[col].sum() - df1[col].sum()) / df1[col].sum() * 100)
                    }
                except:
                    pass
            
            metrics[f"{name1}_to_{name2}"] = growth
        
        return metrics