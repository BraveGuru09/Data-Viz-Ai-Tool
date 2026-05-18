import customtkinter as ctk
from src.ui.main_window import MainWindow

def main():
    """Main entry point for the Data Visualization & AI Analysis Tool"""
    app = ctk.CTk()
    app.geometry("1400x800")
    app.title("Data Visualization & AI Analysis Tool")
    app.resizable(True, True)
    
    # Set color theme
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    # Initialize main window
    main_window = MainWindow(app)
    app.mainloop()

if __name__ == "__main__":
    main()