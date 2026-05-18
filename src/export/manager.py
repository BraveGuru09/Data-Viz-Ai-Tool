import pandas as pd
import os
from datetime import datetime
from tkinter import filedialog
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from typing import Optional

class ExportManager:
    """Manage data and chart exports in multiple formats"""
    
    def __init__(self):
        self.export_history = []
        self.timestamp_format = "%Y%m%d_%H%M%S"
    
    def get_timestamp_filename(self, extension: str) -> str:
        """Generate filename with timestamp"""
        timestamp = datetime.now().strftime(self.timestamp_format)
        return f"export_{timestamp}.{extension}"
    
    def export_to_excel(self, dataframe: pd.DataFrame, original_filename: str = "data") -> str:
        """
        Export DataFrame to Excel file
        
        Args:
            dataframe: DataFrame to export
            original_filename: Original file name for reference
            
        Returns:
            Path to exported file
        """
        try:
            filename = self.get_timestamp_filename("xlsx")
            
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                dataframe.to_excel(writer, sheet_name='Data', index=False)
                
                # Add summary sheet
                summary_data = {
                    'Metric': ['Total Rows', 'Total Columns', 'Export Date'],
                    'Value': [len(dataframe), len(dataframe.columns), datetime.now()]
                }
                summary_df = pd.DataFrame(summary_data)
                summary_df.to_excel(writer, sheet_name='Summary', index=False)
            
            self.export_history.append({
                'type': 'Excel',
                'filename': filename,
                'timestamp': datetime.now(),
                'rows': len(dataframe),
                'columns': len(dataframe.columns)
            })
            
            print(f"✅ Excel export: {filename}")
            return filename
        
        except Exception as e:
            print(f"❌ Excel export error: {str(e)}")
            raise
    
    def export_to_csv(self, dataframe: pd.DataFrame, original_filename: str = "data") -> str:
        """
        Export DataFrame to CSV file
        
        Args:
            dataframe: DataFrame to export
            original_filename: Original file name for reference
            
        Returns:
            Path to exported file
        """
        try:
            filename = self.get_timestamp_filename("csv")
            dataframe.to_csv(filename, index=False)
            
            self.export_history.append({
                'type': 'CSV',
                'filename': filename,
                'timestamp': datetime.now(),
                'rows': len(dataframe),
                'columns': len(dataframe.columns)
            })
            
            print(f"✅ CSV export: {filename}")
            return filename
        
        except Exception as e:
            print(f"❌ CSV export error: {str(e)}")
            raise
    
    def export_to_pdf(self, dataframe: pd.DataFrame, original_filename: str = "data") -> str:
        """
        Export DataFrame to PDF file with formatted table
        
        Args:
            dataframe: DataFrame to export
            original_filename: Original file name for reference
            
        Returns:
            Path to exported file
        """
        try:
            filename = self.get_timestamp_filename("pdf")
            
            # Create PDF
            doc = SimpleDocTemplate(filename, pagesize=letter)
            story = []
            styles = getSampleStyleSheet()
            
            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=16,
                textColor=colors.HexColor('#00d4ff'),
                spaceAfter=12,
                alignment=1  # Center
            )
            
            title = Paragraph(f"📊 Data Export Report", title_style)
            story.append(title)
            
            # Metadata
            metadata_style = ParagraphStyle(
                'Meta',
                parent=styles['Normal'],
                fontSize=10,
                textColor=colors.HexColor('#666666')
            )
            
            metadata = Paragraph(
                f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br/>" +
                f"File: {original_filename}<br/>" +
                f"Rows: {len(dataframe)} | Columns: {len(dataframe.columns)}",
                metadata_style
            )
            story.append(metadata)
            story.append(Spacer(1, 0.3*inch))
            
            # Table data (limit to first 50 rows for readability)
            max_rows = min(50, len(dataframe))
            table_data = [[str(col) for col in dataframe.columns]]
            
            for idx, row in dataframe.head(max_rows).iterrows():
                table_data.append([str(row[col])[:30] for col in dataframe.columns])
            
            # Create table
            table = Table(table_data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#505050')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#00d4ff')),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#2d2d2d')),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.white),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#404040')),
            ]))
            
            story.append(table)
            
            # Build PDF
            doc.build(story)
            
            self.export_history.append({
                'type': 'PDF',
                'filename': filename,
                'timestamp': datetime.now(),
                'rows': len(dataframe),
                'columns': len(dataframe.columns)
            })
            
            print(f"✅ PDF export: {filename}")
            return filename
        
        except Exception as e:
            print(f"❌ PDF export error: {str(e)}")
            raise
    
    def export_chart(self, figure, dpi: int = 300) -> str:
        """
        Export matplotlib figure to PNG image
        
        Args:
            figure: Matplotlib figure to export
            dpi: Resolution (default: 300 DPI - high quality)
            
        Returns:
            Path to exported file
        """
        try:
            filename = self.get_timestamp_filename("png")
            
            figure.savefig(filename, dpi=dpi, bbox_inches='tight', facecolor='#1e1e1e')
            
            self.export_history.append({
                'type': 'Chart (PNG)',
                'filename': filename,
                'timestamp': datetime.now(),
                'dpi': dpi
            })
            
            print(f"✅ Chart export: {filename}")
            return filename
        
        except Exception as e:
            print(f"❌ Chart export error: {str(e)}")
            raise
    
    def export_analytics_report(self, dataframe: pd.DataFrame, original_filename: str = "data") -> str:
        """
        Export analytics summary report as text file
        
        Args:
            dataframe: DataFrame to analyze
            original_filename: Original file name for reference
            
        Returns:
            Path to exported file
        """
        try:
            filename = self.get_timestamp_filename("txt")
            
            report = f"""
╔════════════════════════════════════════════════════════════════╗
║           📊 DATA ANALYSIS REPORT                              ║
╚════════════════════════════════════════════════════════════════╝

📁 FILE INFORMATION
{'-' * 65}
Filename: {original_filename}
Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Total Rows: {len(dataframe)}
Total Columns: {len(dataframe.columns)}

📋 COLUMNS
{'-' * 65}
"""
            
            for i, col in enumerate(dataframe.columns, 1):
                report += f"{i}. {col} ({dataframe[col].dtype})\n"
            
            report += f"""

📈 NUMERIC COLUMNS SUMMARY
{'-' * 65}
"""
            
            numeric_cols = dataframe.select_dtypes(include=['number']).columns
            
            if len(numeric_cols) == 0:
                report += "No numeric columns found\n"
            else:
                for col in numeric_cols:
                    report += f"""
{col}:
  • Mean:     {dataframe[col].mean():.2f}
  • Median:   {dataframe[col].median():.2f}
  • Std Dev:  {dataframe[col].std():.2f}
  • Min:      {dataframe[col].min():.2f}
  • Max:      {dataframe[col].max():.2f}
  • Missing:  {dataframe[col].isnull().sum()}
"""
            
            report += f"""
🤖 DATA QUALITY CHECK
{'-' * 65}
"""
            
            missing_pct = (dataframe.isnull().sum().sum() / (len(dataframe) * len(dataframe.columns))) * 100
            report += f"Missing Values: {missing_pct:.2f}%\n"
            report += f"Duplicate Rows: {dataframe.duplicated().sum()}\n"
            
            report += f"""

{'=' * 65}
Report generated by Data Visualization & AI Tool
{'=' * 65}
"""
            
            with open(filename, 'w') as f:
                f.write(report)
            
            self.export_history.append({
                'type': 'Analytics Report',
                'filename': filename,
                'timestamp': datetime.now()
            })
            
            print(f"✅ Analytics report: {filename}")
            return filename
        
        except Exception as e:
            print(f"❌ Analytics report error: {str(e)}")
            raise
    
    def get_export_history(self) -> list:
        """Get list of all exports"""
        return self.export_history
    
    def clear_export_history(self):
        """Clear export history"""
        self.export_history = []
