import customtkinter as ctk
from tkinter import ttk
import pandas as pd
from typing import Optional

class Dashboard:
    """Main dashboard display area with data table, charts, and insights"""
    
    def __init__(self, parent):
        self.parent = parent
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        
        # Main dashboard frame
        self.dashboard_frame = ctk.CTkFrame(parent, fg_color="#1e1e1e")
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")
        self.dashboard_frame.grid_rowconfigure(1, weight=1)
        self.dashboard_frame.grid_columnconfigure(0, weight=1)
        
        # Header
        header_frame = ctk.CTkFrame(self.dashboard_frame, fg_color="#1e1e1e", height=60)
        header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=(0, 10))
        header_frame.grid_propagate(False)
        
        title = ctk.CTkLabel(
            header_frame,
            text="📊 Dashboard",
            font=("Arial", 24, "bold"),
            text_color="#00d4ff"
        )
        title.pack(side="left", padx=15, pady=10)
        
        # Content area with tabs
        self.content_frame = ctk.CTkFrame(
            self.dashboard_frame,
            fg_color="#2d2d2d",
            corner_radius=15
        )
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)
        
        # Create tabview for different displays
        self.tabview = ctk.CTkTabview(
            self.content_frame,
            fg_color="#2d2d2d",
            segmented_button_fg_color="#404040",
            text_color="#00d4ff"
        )
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        # Tab 1: Data Preview
        self.data_tab = self.tabview.add("📋 Data Preview")
        self.data_tab.grid_rowconfigure(0, weight=1)
        self.data_tab.grid_columnconfigure(0, weight=1)
        
        # Tab 2: Charts
        self.chart_tab = self.tabview.add("📈 Charts")
        self.chart_tab.grid_rowconfigure(0, weight=1)
        self.chart_tab.grid_columnconfigure(0, weight=1)
        
        # Tab 3: Analytics
        self.analytics_tab = self.tabview.add("🔍 Analytics")
        self.analytics_tab.grid_rowconfigure(0, weight=1)
        self.analytics_tab.grid_columnconfigure(0, weight=1)
        
        # Tab 4: Export
        self.export_tab = self.tabview.add("📤 Export")
        self.export_tab.grid_rowconfigure(0, weight=1)
        self.export_tab.grid_columnconfigure(0, weight=1)
        
        # Tab 5: Debug
        self.debug_tab = self.tabview.add("🐛 Debug")
        self.debug_tab.grid_rowconfigure(0, weight=1)
        self.debug_tab.grid_columnconfigure(0, weight=1)
        
        # Initialize tabs
        self._setup_data_tab()
        self._setup_chart_tab()
        self._setup_analytics_tab()
        self._setup_export_tab()
        self._setup_debug_tab()
        
        # Store current data
        self.current_data = None
        self.current_file_name = None
        self.export_manager = None
    
    def set_export_manager(self, manager):
        """Set the export manager instance"""
        self.export_manager = manager
    
    def _setup_data_tab(self):
        """Setup data preview tab with table"""
        # Info frame
        info_frame = ctk.CTkFrame(self.data_tab, fg_color="#1e1e1e", height=50)
        info_frame.pack(fill="x", padx=10, pady=(10, 5))
        info_frame.pack_propagate(False)
        
        self.data_info_label = ctk.CTkLabel(
            info_frame,
            text="👈 Upload a CSV file to view data",
            font=("Arial", 12),
            text_color="#888888"
        )
        self.data_info_label.pack(side="left", padx=10, pady=10)
        
        # Table frame
        table_frame = ctk.CTkFrame(self.data_tab, fg_color="#2d2d2d")
        table_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # Treeview for data display
        self.data_tree = ttk.Treeview(
            table_frame,
            height=15,
            style="Treeview"
        )
        
        # Configure Treeview style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            'Treeview',
            background='#404040',
            foreground='#00d4ff',
            fieldbackground='#404040',
            borderwidth=0
        )
        style.configure(
            'Treeview.Heading',
            background='#505050',
            foreground='#00d4ff',
            borderwidth=1
        )
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.data_tree.yview
        )
        self.data_tree.configure(yscroll=scrollbar.set)
        
        self.data_tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
    
    def _setup_chart_tab(self):
        """Setup chart display tab"""
        # Chart controls frame
        controls_frame = ctk.CTkFrame(self.chart_tab, fg_color="#1e1e1e", height=80)
        controls_frame.pack(fill="x", padx=10, pady=(10, 5))
        controls_frame.pack_propagate(False)
        
        # First row of controls
        row1 = ctk.CTkFrame(controls_frame, fg_color="#1e1e1e")
        row1.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkLabel(
            row1,
            text="Chart Type:",
            font=("Arial", 11, "bold"),
            text_color="#00d4ff"
        ).pack(side="left", padx=5)
        
        # Chart type dropdown
        self.chart_type_var = ctk.StringVar(value="Bar Chart")
        self.chart_type_dropdown = ctk.CTkComboBox(
            row1,
            values=[
                "Bar Chart",
                "Line Chart",
                "Pie Chart",
                "Scatter Plot",
                "Histogram",
                "Box Plot"
            ],
            variable=self.chart_type_var,
            fg_color="#404040",
            button_color="#00d4ff",
            text_color="#00d4ff",
            width=120
        )
        self.chart_type_dropdown.pack(side="left", padx=5)
        
        # Second row of controls
        row2 = ctk.CTkFrame(controls_frame, fg_color="#1e1e1e")
        row2.pack(fill="x", padx=5, pady=5)
        
        # Column selection for X-axis
        ctk.CTkLabel(
            row2,
            text="X-Axis:",
            font=("Arial", 11),
            text_color="#888888"
        ).pack(side="left", padx=5)
        
        self.x_column_var = ctk.StringVar(value="Select Column")
        self.x_column_dropdown = ctk.CTkComboBox(
            row2,
            values=["Select Column"],
            variable=self.x_column_var,
            fg_color="#404040",
            button_color="#00d4ff",
            text_color="#00d4ff",
            width=120
        )
        self.x_column_dropdown.pack(side="left", padx=5)
        
        # Column selection for Y-axis
        ctk.CTkLabel(
            row2,
            text="Y-Axis:",
            font=("Arial", 11),
            text_color="#888888"
        ).pack(side="left", padx=(20, 5))
        
        self.y_column_var = ctk.StringVar(value="Select Column")
        self.y_column_dropdown = ctk.CTkComboBox(
            row2,
            values=["Select Column"],
            variable=self.y_column_var,
            fg_color="#404040",
            button_color="#00d4ff",
            text_color="#00d4ff",
            width=120
        )
        self.y_column_dropdown.pack(side="left", padx=5)
        
        # Create chart button
        create_chart_btn = ctk.CTkButton(
            row2,
            text="📊 Create Chart",
            fg_color="#00d4ff",
            text_color="#1e1e1e",
            font=("Arial", 10, "bold"),
            command=self.create_chart
        )
        create_chart_btn.pack(side="left", padx=15)
        
        # Chart display frame
        self.chart_display_frame = ctk.CTkFrame(self.chart_tab, fg_color="#2d2d2d")
        self.chart_display_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))
        
        self.chart_placeholder = ctk.CTkLabel(
            self.chart_display_frame,
            text="📈 Chart will appear here",
            font=("Arial", 14),
            text_color="#888888"
        )
        self.chart_placeholder.pack(expand=True)
    
    def _setup_analytics_tab(self):
        """Setup analytics display tab"""
        # Analytics info frame
        self.analytics_frame = ctk.CTkFrame(self.analytics_tab, fg_color="#2d2d2d")
        self.analytics_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Scrollable text area
        scrollable_frame = ctk.CTkScrollableFrame(
            self.analytics_frame,
            fg_color="#2d2d2d",
            label_text="Analytics & Insights"
        )
        scrollable_frame.pack(fill="both", expand=True)
        
        self.analytics_label = ctk.CTkLabel(
            scrollable_frame,
            text="📊 Upload data to see analytics",
            font=("Arial", 12),
            text_color="#888888",
            justify="left"
        )
        self.analytics_label.pack(anchor="nw", padx=10, pady=10)
    
    def _setup_export_tab(self):
        """Setup export tab with multiple export options"""
        # Export controls frame
        controls_frame = ctk.CTkFrame(self.export_tab, fg_color="#1e1e1e", height=150)
        controls_frame.pack(fill="x", padx=10, pady=(10, 5))
        controls_frame.pack_propagate(False)
        
        # Title
        ctk.CTkLabel(
            controls_frame,
            text="📤 Export Your Data",
            font=("Arial", 14, "bold"),
            text_color="#00d4ff"
        ).pack(pady=(10, 15))
        
        # Data export buttons
        data_label = ctk.CTkLabel(
            controls_frame,
            text="Export Data:",
            font=("Arial", 11, "bold"),
            text_color="#888888"
        )
        data_label.pack(anchor="w", padx=15, pady=(5, 10))
        
        data_buttons_frame = ctk.CTkFrame(controls_frame, fg_color="#1e1e1e")
        data_buttons_frame.pack(fill="x", padx=15, pady=5)
        
        self.export_excel_btn = ctk.CTkButton(
            data_buttons_frame,
            text="📄 Excel",
            fg_color="#00aa00",
            hover_color="#00cc00",
            text_color="#1e1e1e",
            command=self.export_to_excel
        )
        self.export_excel_btn.pack(side="left", padx=5)
        
        self.export_csv_btn = ctk.CTkButton(
            data_buttons_frame,
            text="📋 CSV",
            fg_color="#0077ff",
            hover_color="#0099ff",
            text_color="white",
            command=self.export_to_csv
        )
        self.export_csv_btn.pack(side="left", padx=5)
        
        self.export_pdf_btn = ctk.CTkButton(
            data_buttons_frame,
            text="📕 PDF",
            fg_color="#cc0000",
            hover_color="#ff0000",
            text_color="white",
            command=self.export_to_pdf
        )
        self.export_pdf_btn.pack(side="left", padx=5)
        
        # Chart export buttons
        chart_label = ctk.CTkLabel(
            controls_frame,
            text="Export Charts:",
            font=("Arial", 11, "bold"),
            text_color="#888888"
        )
        chart_label.pack(anchor="w", padx=15, pady=(10, 5))
        
        chart_buttons_frame = ctk.CTkFrame(controls_frame, fg_color="#1e1e1e")
        chart_buttons_frame.pack(fill="x", padx=15, pady=5)
        
        self.export_chart_btn = ctk.CTkButton(
            chart_buttons_frame,
            text="🖼️ Chart as PNG",
            fg_color="#ff7700",
            hover_color="#ff9900",
            text_color="white",
            command=self.export_chart_image
        )
        self.export_chart_btn.pack(side="left", padx=5)
        
        self.export_analytics_btn = ctk.CTkButton(
            chart_buttons_frame,
            text="📊 Analytics Report",
            fg_color="#9900ff",
            hover_color="#bb00ff",
            text_color="white",
            command=self.export_analytics_report
        )
        self.export_analytics_btn.pack(side="left", padx=5)
        
        # Status display
        self.export_status_frame = ctk.CTkFrame(self.export_tab, fg_color="#2d2d2d")
        self.export_status_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))
        
        self.export_status_label = ctk.CTkLabel(
            self.export_status_frame,
            text="✅ Export options ready\n\nSelect an export format above to get started!",
            font=("Arial", 12),
            text_color="#888888",
            justify="left"
        )
        self.export_status_label.pack(expand=True, padx=10, pady=10)
    
    def _setup_debug_tab(self):
        """Setup debug tab with logging and system info"""
        # Debug controls
        controls_frame = ctk.CTkFrame(self.debug_tab, fg_color="#1e1e1e", height=50)
        controls_frame.pack(fill="x", padx=10, pady=(10, 5))
        controls_frame.pack_propagate(False)
        
        clear_btn = ctk.CTkButton(
            controls_frame,
            text="🗑️ Clear Logs",
            fg_color="#404040",
            hover_color="#505050",
            command=self.clear_debug_logs
        )
        clear_btn.pack(side="left", padx=5, pady=5)
        
        export_btn = ctk.CTkButton(
            controls_frame,
            text="💾 Export Logs",
            fg_color="#404040",
            hover_color="#505050",
            command=self.export_debug_logs
        )
        export_btn.pack(side="left", padx=5, pady=5)
        
        # Debug log frame
        log_frame = ctk.CTkFrame(self.debug_tab, fg_color="#2d2d2d")
        log_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))
        log_frame.grid_rowconfigure(0, weight=1)
        log_frame.grid_columnconfigure(0, weight=1)
        
        # Debug text area
        self.debug_text = ctk.CTkTextbox(
            log_frame,
            fg_color="#1e1e1e",
            text_color="#00d4ff",
            border_width=1,
            border_color="#404040"
        )
        self.debug_text.grid(row=0, column=0, sticky="nsew")
        
        # Initial debug message
        self.debug_log("🟢 Debug Console Ready\n")
        self.debug_log(f"⏰ Timestamp: {pd.Timestamp.now()}\n")
        self.debug_log("=" * 60 + "\n")
    
    def display_data(self, dataframe: pd.DataFrame, file_name: str):
        """Display CSV data in the data preview table"""
        self.current_data = dataframe
        self.current_file_name = file_name
        
        # Debug log
        self.debug_log(f"✅ File Loaded: {file_name}")
        self.debug_log(f"📊 Rows: {len(dataframe)}, Columns: {len(dataframe.columns)}")
        self.debug_log(f"📝 Columns: {', '.join(dataframe.columns)}\n")
        
        # Update data info
        self.data_info_label.configure(
            text=f"📁 {file_name} | 📊 {len(dataframe)} rows × {len(dataframe.columns)} columns"
        )
        
        # Clear existing treeview
        for item in self.data_tree.get_children():
            self.data_tree.delete(item)
        
        # Set up columns
        self.data_tree['columns'] = list(dataframe.columns)
        self.data_tree.column('#0', width=0, stretch=False)
        
        for col in dataframe.columns:
            self.data_tree.column(col, anchor='center', width=100)
            self.data_tree.heading(col, text=col, anchor='center')
        
        # Insert data (limit to first 100 rows for performance)
        max_rows = min(100, len(dataframe))
        for idx, row in dataframe.head(max_rows).iterrows():
            values = [row[col] for col in dataframe.columns]
            self.data_tree.insert(parent='', index='end', iid=idx, values=values)
        
        # Update chart dropdowns
        numeric_cols = dataframe.select_dtypes(include=['number']).columns.tolist()
        all_cols = list(dataframe.columns)
        
        self.x_column_dropdown.configure(values=all_cols)
        self.y_column_dropdown.configure(values=numeric_cols if numeric_cols else all_cols)
        
        if all_cols:
            self.x_column_var.set(all_cols[0])
        if numeric_cols:
            self.y_column_var.set(numeric_cols[0])
        
        self.debug_log("✨ Data preview updated in table\n")
    
    def create_chart(self):
        """Create and display chart based on selected columns"""
        if self.current_data is None:
            self.debug_log("⚠️ Error: No data loaded\n")
            return
        
        x_col = self.x_column_var.get()
        y_col = self.y_column_var.get()
        chart_type = self.chart_type_var.get()
        
        if x_col == "Select Column" or y_col == "Select Column":
            self.debug_log("⚠️ Error: Please select columns\n")
            return
        
        try:
            self.debug_log(f"📊 Creating {chart_type}...")
            self.debug_log(f"   X-Axis: {x_col}")
            self.debug_log(f"   Y-Axis: {y_col}\n")
            
            from src.charts.chart_factory import ChartFactory
            import matplotlib.pyplot as plt
            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
            
            # Create chart
            factory = ChartFactory(self.current_data)
            
            if chart_type == "Bar Chart":
                fig = factory.create_bar_chart(x_col, y_col, f"Bar Chart: {x_col} vs {y_col}")
            elif chart_type == "Line Chart":
                fig = factory.create_line_chart(x_col, y_col, f"Line Chart: {x_col} vs {y_col}")
            elif chart_type == "Pie Chart":
                fig = factory.create_pie_chart(x_col, f"Pie Chart: {x_col}")
            elif chart_type == "Scatter Plot":
                fig = factory.create_scatter_plot(x_col, y_col, f"Scatter Plot: {x_col} vs {y_col}")
            elif chart_type == "Histogram":
                fig = factory.create_histogram(y_col, title=f"Histogram: {y_col}")
            elif chart_type == "Box Plot":
                fig = factory.create_box_plot(y_col, title=f"Box Plot: {y_col}")
            
            # Store current figure for export
            self.current_figure = fig
            
            # Clear previous chart
            for widget in self.chart_display_frame.winfo_children():
                widget.destroy()
            
            # Embed chart
            canvas = FigureCanvasTkAgg(fig, master=self.chart_display_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
            
            self.debug_log(f"✅ {chart_type} created successfully!\n")
            
        except Exception as e:
            error_msg = f"❌ Error creating chart: {str(e)}\n"
            self.debug_log(error_msg)
            self.chart_placeholder.configure(text=f"❌ Error: {str(e)}")
    
    def display_analytics(self, insights: list):
        """Display analytics insights"""
        try:
            self.debug_log("🔍 Generating analytics...")
            
            analytics_text = "📊 DATA ANALYTICS & INSIGHTS\n"
            analytics_text += "=" * 70 + "\n\n"
            
            if self.current_data is not None:
                analytics_text += f"📁 File: {self.current_file_name}\n"
                analytics_text += f"📊 Rows: {len(self.current_data)}\n"
                analytics_text += f"📝 Columns: {len(self.current_data.columns)}\n"
                analytics_text += f"📋 Column List: {', '.join(self.current_data.columns)}\n\n"
                
                analytics_text += "📈 NUMERIC SUMMARY:\n"
                analytics_text += "-" * 70 + "\n"
                numeric_cols = self.current_data.select_dtypes(include=['number']).columns
                
                if len(numeric_cols) == 0:
                    analytics_text += "No numeric columns found\n"
                else:
                    for col in numeric_cols:
                        analytics_text += f"\n{col}:\n"
                        analytics_text += f"  Mean: {self.current_data[col].mean():.2f}\n"
                        analytics_text += f"  Median: {self.current_data[col].median():.2f}\n"
                        analytics_text += f"  Std Dev: {self.current_data[col].std():.2f}\n"
                        analytics_text += f"  Min: {self.current_data[col].min():.2f}\n"
                        analytics_text += f"  Max: {self.current_data[col].max():.2f}\n"
                
                analytics_text += "\n\n🤖 AI INSIGHTS:\n"
                analytics_text += "-" * 70 + "\n"
                
                if insights:
                    for i, insight in enumerate(insights, 1):
                        analytics_text += f"{i}. {insight}\n"
                else:
                    analytics_text += "No insights generated yet\n"
            
            self.analytics_label.configure(text=analytics_text)
            self.debug_log("✅ Analytics displayed\n")
            
        except Exception as e:
            self.debug_log(f"❌ Error displaying analytics: {str(e)}\n")
    
    def export_to_excel(self):
        """Export data to Excel"""
        if self.current_data is None:
            self.export_status_label.configure(text="❌ No data to export. Please upload a CSV file first.")
            self.debug_log("❌ Error: No data to export\n")
            return
        
        try:
            self.export_status_label.configure(text="⏳ Exporting to Excel...")
            if self.export_manager:
                filepath = self.export_manager.export_to_excel(self.current_data, self.current_file_name)
                self.export_status_label.configure(text=f"✅ Exported to Excel:\n{filepath}")
                self.debug_log(f"✅ Data exported to Excel: {filepath}\n")
            else:
                self.export_status_label.configure(text="⚠️ Export manager not configured")
        except Exception as e:
            self.export_status_label.configure(text=f"❌ Export failed: {str(e)}")
            self.debug_log(f"❌ Excel export error: {str(e)}\n")
    
    def export_to_csv(self):
        """Export data to CSV"""
        if self.current_data is None:
            self.export_status_label.configure(text="❌ No data to export. Please upload a CSV file first.")
            self.debug_log("❌ Error: No data to export\n")
            return
        
        try:
            self.export_status_label.configure(text="⏳ Exporting to CSV...")
            if self.export_manager:
                filepath = self.export_manager.export_to_csv(self.current_data, self.current_file_name)
                self.export_status_label.configure(text=f"✅ Exported to CSV:\n{filepath}")
                self.debug_log(f"✅ Data exported to CSV: {filepath}\n")
            else:
                self.export_status_label.configure(text="⚠️ Export manager not configured")
        except Exception as e:
            self.export_status_label.configure(text=f"❌ Export failed: {str(e)}")
            self.debug_log(f"❌ CSV export error: {str(e)}\n")
    
    def export_to_pdf(self):
        """Export data to PDF"""
        if self.current_data is None:
            self.export_status_label.configure(text="❌ No data to export. Please upload a CSV file first.")
            self.debug_log("❌ Error: No data to export\n")
            return
        
        try:
            self.export_status_label.configure(text="⏳ Exporting to PDF...")
            if self.export_manager:
                filepath = self.export_manager.export_to_pdf(self.current_data, self.current_file_name)
                self.export_status_label.configure(text=f"✅ Exported to PDF:\n{filepath}")
                self.debug_log(f"✅ Data exported to PDF: {filepath}\n")
            else:
                self.export_status_label.configure(text="⚠️ Export manager not configured")
        except Exception as e:
            self.export_status_label.configure(text=f"❌ Export failed: {str(e)}")
            self.debug_log(f"❌ PDF export error: {str(e)}\n")
    
    def export_chart_image(self):
        """Export current chart as image"""
        if not hasattr(self, 'current_figure'):
            self.export_status_label.configure(text="❌ No chart created yet. Please create a chart first.")
            self.debug_log("❌ Error: No chart to export\n")
            return
        
        try:
            self.export_status_label.configure(text="⏳ Exporting chart...")
            if self.export_manager:
                filepath = self.export_manager.export_chart(self.current_figure)
                self.export_status_label.configure(text=f"✅ Chart exported as PNG:\n{filepath}")
                self.debug_log(f"✅ Chart exported to PNG: {filepath}\n")
            else:
                self.export_status_label.configure(text="⚠️ Export manager not configured")
        except Exception as e:
            self.export_status_label.configure(text=f"❌ Export failed: {str(e)}")
            self.debug_log(f"❌ Chart export error: {str(e)}\n")
    
    def export_analytics_report(self):
        """Export analytics as text report"""
        if self.current_data is None:
            self.export_status_label.configure(text="❌ No data to analyze. Please upload a CSV file first.")
            self.debug_log("❌ Error: No data to export\n")
            return
        
        try:
            self.export_status_label.configure(text="⏳ Generating report...")
            if self.export_manager:
                filepath = self.export_manager.export_analytics_report(self.current_data, self.current_file_name)
                self.export_status_label.configure(text=f"✅ Report exported as TXT:\n{filepath}")
                self.debug_log(f"✅ Analytics report exported: {filepath}\n")
            else:
                self.export_status_label.configure(text="⚠️ Export manager not configured")
        except Exception as e:
            self.export_status_label.configure(text=f"❌ Export failed: {str(e)}")
            self.debug_log(f"❌ Report export error: {str(e)}\n")
    
    def debug_log(self, message: str):
        """Add message to debug console"""
        self.debug_text.insert("end", message)
        self.debug_text.see("end")  # Auto-scroll to bottom
    
    def clear_debug_logs(self):
        """Clear debug logs"""
        self.debug_text.delete("1.0", "end")
        self.debug_log("🗑️ Logs cleared\n")
        self.debug_log("=" * 60 + "\n")
    
    def export_debug_logs(self):
        """Export debug logs to file"""
        try:
            log_content = self.debug_text.get("1.0", "end")
            
            # Save to file
            with open("debug_logs.txt", "w") as f:
                f.write(log_content)
            
            self.debug_log("💾 Logs exported to debug_logs.txt\n")
        except Exception as e:
            self.debug_log(f"❌ Error exporting logs: {str(e)}\n")