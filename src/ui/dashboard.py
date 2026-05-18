import customtkinter as ctk

class Dashboard:
    """Main dashboard display area"""
    
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
        
        # Content area
        self.content_frame = ctk.CTkFrame(
            self.dashboard_frame,
            fg_color="#2d2d2d",
            corner_radius=15
        )
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)
        
        # Placeholder content
        placeholder_frame = ctk.CTkFrame(self.content_frame, fg_color="#2d2d2d")
        placeholder_frame.grid(row=0, column=0, sticky="nsew")
        placeholder_frame.grid_rowconfigure(0, weight=1)
        placeholder_frame.grid_columnconfigure(0, weight=1)
        
        placeholder = ctk.CTkLabel(
            placeholder_frame,
            text="👈 Select an option from the sidebar to begin",
            font=("Arial", 16),
            text_color="#888888"
        )
        placeholder.grid(row=0, column=0)
        
        self.current_content = placeholder_frame
    
    def update_display(self, content):
        """Update dashboard content"""
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Create new content frame
        new_frame = ctk.CTkFrame(self.content_frame, fg_color="#2d2d2d")
        new_frame.grid(row=0, column=0, sticky="nsew")
        new_frame.grid_rowconfigure(0, weight=1)
        new_frame.grid_columnconfigure(0, weight=1)
        
        # Add content
        label = ctk.CTkLabel(
            new_frame,
            text=f"📌 {content}",
            font=("Arial", 14),
            text_color="#00d4ff"
        )
        label.grid(row=0, column=0)
        
        self.current_content = new_frame
    
    def show_error(self, message):
        """Display error message"""
        self.update_display(f"❌ Error: {message}")
    
    def show_compare_interface(self):
        """Show file comparison interface"""
        self.update_display("📊 Compare Files - Select up to 3 files")
    
    def show_ai_insights(self):
        """Show AI insights interface"""
        self.update_display("🤖 AI Insights - Analyzing your data...")