import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class ChartEmbedder:
    """Embed Matplotlib charts in CustomTkinter"""
    
    @staticmethod
    def embed_chart(parent_frame: ctk.CTkFrame, figure: Figure) -> ctk.CTkFrame:
        """
        Embed a Matplotlib figure in a CustomTkinter frame
        
        Args:
            parent_frame: Parent CustomTkinter frame
            figure: Matplotlib figure to embed
            
        Returns:
            Frame containing the embedded chart
        """
        # Create canvas
        canvas = FigureCanvasTkAgg(figure, master=parent_frame)
        canvas.draw()
        
        # Get canvas widget
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill='both', expand=True, padx=10, pady=10)
        
        return parent_frame
    
    @staticmethod
    def create_chart_frame(parent: ctk.CTkFrame) -> ctk.CTkFrame:
        """
        Create a frame for chart display
        
        Args:
            parent: Parent CustomTkinter frame
            
        Returns:
            New chart frame
        """
        chart_frame = ctk.CTkFrame(
            parent,
            fg_color="#2d2d2d",
            corner_radius=10
        )
        chart_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        return chart_frame