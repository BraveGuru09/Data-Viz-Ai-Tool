import pandas as pd
import numpy as np
from typing import List, Dict, Any
from sklearn.preprocessing import StandardScaler

class InsightGenerator:
    """Generate AI insights from data (free, rule-based)"""
    
    def __init__(self):
        self.insights = []
    
    def analyze(self, dataframe: pd.DataFrame) -> 'InsightGenerator':
        """
        Analyze DataFrame and generate insights
        
        Args:
            dataframe: DataFrame to analyze
            
        Returns:
            Self for method chaining
        """
        self.df = dataframe
        self.insights = []
        
        self._analyze_numeric_data()
        self._detect_anomalies()
        self._analyze_trends()
        
        return self
    
    def _analyze_numeric_data(self):
        """Analyze numeric columns"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            mean = self.df[col].mean()
            std = self.df[col].std()
            
            if mean < 100:
                self.insights.append(f"📊 {col}: Average value is {mean:.2f} (below typical range)")
            elif mean > 1000:
                self.insights.append(f"📊 {col}: Average value is {mean:.2f} (high values detected)")
    
    def _detect_anomalies(self):
        """Detect anomalies in data"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            outliers = len(self.df[
                (self.df[col] < Q1 - 1.5 * IQR) | 
                (self.df[col] > Q3 + 1.5 * IQR)
            ])
            
            if outliers > 0:
                self.insights.append(f"⚠️ {col}: {outliers} anomalies detected")
    
    def _analyze_trends(self):
        """Analyze trends in data"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            if len(self.df) > 1:
                first = self.df[col].iloc[0]
                last = self.df[col].iloc[-1]
                change_pct = ((last - first) / first * 100) if first != 0 else 0
                
                if change_pct > 10:
                    self.insights.append(f"📈 {col}: Growing trend detected (+{change_pct:.1f}%)")
                elif change_pct < -10:
                    self.insights.append(f"📉 {col}: Declining trend detected ({change_pct:.1f}%)")
    
    def get_summary(self) -> str:
        """
        Get summary of insights
        
        Returns:
            Summary string
        """
        if not self.insights:
            return "No significant insights detected."
        
        return "\n".join(self.insights)
    
    def get_insights_list(self) -> List[str]:
        """
        Get insights as list
        
        Returns:
            List of insights
        """
        return self.insights