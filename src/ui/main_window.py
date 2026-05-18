import customtkinter as ctk
from src.ui.sidebar import Sidebar
from src.ui.dashboard import Dashboard
from src.export.manager import ExportManager

class MainWindow:
    """Main application window container"""
    
    def __init__(self, root):
        self.root = root
        self.root.configure(fg_color="#1e1e1e")
        
        # Configure grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
        # Initialize export manager
        self.export_manager = ExportManager()
        
        # Create sidebar
        self.sidebar = Sidebar(root, self.on_action)
        
        # Create main content frame
        main_frame = ctk.CTkFrame(root, fg_color="#1e1e1e")
        main_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Create dashboard
        self.dashboard = Dashboard(main_frame)
        self.dashboard.set_export_manager(self.export_manager)
        
        # Store data state
        self.loaded_files = []
        self.current_data = None
    
    def on_action(self, action):
        """Handle actions from sidebar"""
        print(f"Action triggered: {action}")
        
        # Handle specific actions
        if "Upload" in action:
            self.handle_file_upload(action)
        elif "Chart" in action:
            self.handle_chart_request(action)
        elif "Compare" in action:
            self.dashboard.debug_log("📊 Compare Files feature - Coming soon!\n")
        elif "AI" in action:
            self.dashboard.debug_log("🤖 AI Insights feature - Coming soon!\n")
        elif "Clear" in action:
            self.dashboard.debug_log("🗑️ Clearing all data...\n")
            self.current_data = None
            self.loaded_files = []
    
    def handle_file_upload(self, action):
        """Handle CSV file upload"""
        try:
            file_path = action.split(": ")[1]
            
            # Load the file
            from src.data.loader import DataLoader
            loader = DataLoader()
            df = loader.load_csv(file_path)
            
            if df is not None:
                self.current_data = df
                self.loaded_files.append(file_path)
                
                # Display data
                import os
                file_name = os.path.basename(file_path)
                self.dashboard.display_data(df, file_name)
                
                # Generate AI insights
                from src.ai.insights import InsightGenerator
                generator = InsightGenerator()
                generator.analyze(df)
                insights = generator.get_insights_list()
                
                # Display analytics
                self.dashboard.display_analytics(insights)
                
                self.dashboard.debug_log(f"✅ Successfully loaded: {file_name}\n")
            else:
                self.dashboard.debug_log(f"❌ Failed to load file\n")
        
        except IndexError:
            self.dashboard.debug_log("⚠️ Invalid file upload action\n")
        except Exception as e:
            self.dashboard.debug_log(f"❌ Error loading file: {str(e)}\n")
    
    def handle_chart_request(self, chart_type):
        """Handle chart creation request"""
        if self.current_data is None:
            self.dashboard.debug_log("⚠️ Please upload a CSV file first\n")
        else:
            self.dashboard.debug_log(f"📈 Ready to create {chart_type}\n")
