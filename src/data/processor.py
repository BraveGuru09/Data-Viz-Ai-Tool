import pandas as pd
from typing import List, Optional

class DataProcessor:
    """Handle data processing and cleaning"""
    
    @staticmethod
    def clean_data(df: pd.DataFrame) -> pd.DataFrame:
        """
        Basic data cleaning
        
        Args:
            df: Input DataFrame
            
        Returns:
            Cleaned DataFrame
        """
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Handle missing values
        df = df.dropna()
        
        return df
    
    @staticmethod
    def merge_files(dataframes: List[pd.DataFrame], method: str = "concat") -> Optional[pd.DataFrame]:
        """
        Merge multiple DataFrames
        
        Args:
            dataframes: List of DataFrames to merge
            method: "concat" or "merge"
            
        Returns:
            Merged DataFrame
        """
        try:
            if method == "concat":
                return pd.concat(dataframes, ignore_index=True)
            elif method == "merge":
                result = dataframes[0]
                for df in dataframes[1:]:
                    result = pd.merge(result, df, how="inner")
                return result
        except Exception as e:
            print(f"Error merging files: {str(e)}")
            return None
    
    @staticmethod
    def get_statistics(df: pd.DataFrame) -> dict:
        """
        Get basic statistics
        
        Args:
            df: Input DataFrame
            
        Returns:
            Dictionary of statistics
        """
        stats = {
            "count": len(df),
            "numeric_columns": df.select_dtypes(include=['number']).columns.tolist(),
            "text_columns": df.select_dtypes(include=['object']).columns.tolist(),
            "missing_values": df.isnull().sum().to_dict(),
            "summary": df.describe().to_dict()
        }
        return stats
    
    @staticmethod
    def filter_data(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
        """
        Filter DataFrame by column value
        
        Args:
            df: Input DataFrame
            column: Column to filter by
            value: Value to filter
            
        Returns:
            Filtered DataFrame
        """
        return df[df[column] == value]
    
    @staticmethod
    def sort_data(df: pd.DataFrame, column: str, ascending: bool = True) -> pd.DataFrame:
        """
        Sort DataFrame
        
        Args:
            df: Input DataFrame
            column: Column to sort by
            ascending: Sort order
            
        Returns:
            Sorted DataFrame
        """
        return df.sort_values(by=column, ascending=ascending)