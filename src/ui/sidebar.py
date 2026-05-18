import customtkinter as ctk
from tkinter import filedialog

class Sidebar:
    """Sidebar navigation component"""
    
    def __init__(self, root, callback):
        self.callback = callback
        self.sidebar_frame = ctk.CTkFrame(root, fg_color="#2d2d2d", width=250)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.sidebar_frame.grid_propagate(False)
        
        # Title
        title = ctk.CTkLabel(
            self.sidebar_frame,
            text="📊 Data Viz AI",
            font=("Arial", 18, "bold"),
            text_color="#00d4ff"
        )
        title.pack(pady=15)
        
        # Upload Button
        upload_btn = ctk.CTkButton(
            self.sidebar_frame,
            text="📤 Upload CSV",
            command=self.upload_file,
            fg_color="#00d4ff",
            text_color="#1e1e1e",
            font=("Arial", 11, "bold")
        )
        upload_btn.pack(pady=5, padx=10, fill="x")
        
        # Divider
        divider1 = ctk.CTkLabel(self.sidebar_frame, text="━" * 20, text_color="#404040")
        divider1.pack(pady=10)
        
        # Chart Types Section
        charts_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="📈 Chart Types",
            font=("Arial", 12, "bold"),
            text_color="#00d4ff"
        )
        charts_label.pack(pady=(10, 5), padx=10)
        
        charts = [
            "📊 Bar Chart",
            "📈 Line Chart",
            "🥧 Pie Chart",
            "🔵 Scatter Plot",
            "📊 Histogram",
            "📦 Box Plot"
        ]
        for chart in charts:
            btn = ctk.CTkButton(
                self.sidebar_frame,
                text=chart,
                command=lambda c=chart: self.callback(c),
                fg_color="#404040",
                hover_color="#505050",
                font=("Arial", 10)
            )
            btn.pack(pady=2, padx=10, fill="x")
        
        # Divider
        divider2 = ctk.CTkLabel(self.sidebar_frame, text="━" * 20, text_color="#404040")
        divider2.pack(pady=10)
        
        # Analysis Section
        analysis_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="🔍 Analysis",
            font=("Arial", 12, "bold"),
            text_color="#00d4ff"
        )
        analysis_label.pack(pady=(10, 5), padx=10)
        
        compare_btn = ctk.CTkButton(
            self.sidebar_frame,
            text="📊 Compare Files",
            command=lambda: self.callback("Compare Files"),
            fg_color="#404040",
            hover_color="#505050",
            font=("Arial", 10)
        )
        compare_btn.pack(pady=2, padx=10, fill="x")
        
        ai_btn = ctk.CTkButton(
            self.sidebar_frame,
            text="🤖 AI Insights",
            command=lambda: self.callback("AI Insights"),
            fg_color="#404040",
            hover_color="#505050",
            font=("Arial", 10)
        )
        ai_btn.pack(pady=2, padx=10, fill="x")
        
        # Divider
        divider3 = ctk.CTkLabel(self.sidebar_frame, text="━" * 20, text_color="#404040")
        divider3.pack(pady=10)
        
        # Settings
        clear_btn = ctk.CTkButton(
            self.sidebar_frame,
            text="⚙️ Clear All",
            command=lambda: self.callback("Clear All"),
            fg_color="#404040",
            hover_color="#505050",
            font=("Arial", 10)
        )
        clear_btn.pack(pady=5, padx=10, fill="x")
    
    def upload_file(self):
        """Handle CSV file upload dialog"""
        file_path = filedialog.askopenfilename(
            title="Select a CSV file",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if file_path:
            self.callback(f"Upload: {file_path}")