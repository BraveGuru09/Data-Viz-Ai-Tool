import pandas as pd
import os
from typing import Optional

class DataLoader:
    """Handle CSV and data file loading"""
    
    def __init__(self):
        self.loaded_files = {}
    
    def load_csv(self, file_path: str) -> Optional[pd.DataFrame]:
        """
        Load a CSV file into a pandas DataFrame
        
        Args:
            file_path: Path to CSV file
            
        Returns:
            pd.DataFrame or None if failed
        """
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            
            df = pd.read_csv(file_path)
            file_name = os.path.basename(file_path)
            self.loaded_files[file_name] = df
            
            print(f"✓ Loaded: {file_name} ({len(df)} rows, {len(df.columns)} columns)")
            return df
        
        except Exception as e:
            print(f"✗ Error loading {file_path}: {str(e)}")
            return None
    
    def load_excel(self, file_path: str, sheet_name: str = 0) -> Optional[pd.DataFrame]:
        """
        Load an Excel file
        
        Args:
            file_path: Path to Excel file
            sheet_name: Sheet to load (default: 0)
            
        Returns:
            pd.DataFrame or None if failed
        """
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            file_name = os.path.basename(file_path)
            self.loaded_files[file_name] = df
            
            print(f"✓ Loaded: {file_name} ({len(df)} rows, {len(df.columns)} columns)")
            return df
        
        except Exception as e:
            print(f"✗ Error loading {file_path}: {str(e)}")
            return None
    
    def get_file_info(self, file_name: str) -> dict:
        """Get information about loaded file"""
        if file_name in self.loaded_files:
            df = self.loaded_files[file_name]
            return {
                "name": file_name,
                "rows": len(df),
                "columns": len(df.columns),
                "column_names": list(df.columns),
                "dtypes": df.dtypes.to_dict()
            }
        return None
    
    def list_loaded_files(self) -> list:
        """Get list of all loaded files"""
        return list(self.loaded_files.keys())