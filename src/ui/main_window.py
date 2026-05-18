import customtkinter as ctk
from src.ui.sidebar import Sidebar
from src.ui.dashboard import Dashboard

class MainWindow:
    """Main application window container"""
    
    def __init__(self, root):
        self.root = root
        self.root.configure(fg_color="#1e1e1e")
        
        # Configure grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
        # Create sidebar
        self.sidebar = Sidebar(root, self.on_action)
        
        # Create main content frame
        main_frame = ctk.CTkFrame(root, fg_color="#1e1e1e")
        main_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Create dashboard
        self.dashboard = Dashboard(main_frame)
        
        # Store data state
        self.loaded_files = []
        self.current_data = None
    
    def on_action(self, action):
        """Handle actions from sidebar"""
        print(f"Action triggered: {action}")
        self.dashboard.update_display(action)
        
        # Handle specific actions
        if "Upload" in action:
            self.handle_file_upload(action)
        elif "Chart" in action:
            self.handle_chart_request(action)
        elif "Compare" in action:
            self.dashboard.show_compare_interface()
        elif "AI" in action:
            self.dashboard.show_ai_insights()
    
    def handle_file_upload(self, action):
        """Handle CSV file upload"""
        # Extract file path from action string
        try:
            file_path = action.split(": ")[1]
            print(f"Loading file: {file_path}")
            self.loaded_files.append(file_path)
        except IndexError:
            print("Invalid file action")
    
    def handle_chart_request(self, chart_type):
        """Handle chart creation request"""
        if self.current_data is None:
            self.dashboard.show_error("Please upload a CSV file first")
        else:
            print(f"Creating {chart_type}")