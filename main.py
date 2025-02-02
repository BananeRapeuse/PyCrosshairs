import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Configuration initiale
CROSSHAIR_PATH = "crosshairs/"
COLORS = {
    "Noir": "black.png",
    "Bleu": "blue.png",
    "Vert": "green.png",
    "Rouge": "red.png",
    "Blanc": "white.png"
}
SIZES = {
    "Small": (50, 50),
    "Medium": (100, 100),
    "High": (150, 150)
}

class CrosshairApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PyCrosshair")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        # Variables
        self.selected_color = tk.StringVar(value="Noir")
        self.selected_size = tk.StringVar(value="Medium")
        
        # Création des widgets
        ttk.Label(root, text="Choisir la couleur:").pack(pady=5)
        self.color_menu = ttk.Combobox(root, values=list(COLORS.keys()), textvariable=self.selected_color)
        self.color_menu.pack()
        
        ttk.Label(root, text="Choisir la taille:").pack(pady=5)
        self.size_menu = ttk.Combobox(root, values=list(SIZES.keys()), textvariable=self.selected_size)
        self.size_menu.pack()
        
        self.apply_button = ttk.Button(root, text="Appliquer", command=self.apply_settings)
        self.apply_button.pack(pady=10)
        
        self.crosshair_window = None
        self.apply_settings()
    
    def apply_settings(self):
        color = self.selected_color.get()
        size = self.selected_size.get()
        image_path = os.path.join(CROSSHAIR_PATH, COLORS[color])
        img = Image.open(image_path).resize(SIZES[size], Image.ANTIALIAS)
        self.display_crosshair(img)
    
    def display_crosshair(self, img):
        if self.crosshair_window:
            self.crosshair_window.destroy()
        
        self.crosshair_window = tk.Toplevel(self.root)
        self.crosshair_window.overrideredirect(True)
        self.crosshair_window.attributes("-topmost", True)
        self.crosshair_window.attributes("-transparentcolor", "black")
        
        screen_width = self.crosshair_window.winfo_screenwidth()
        screen_height = self.crosshair_window.winfo_screenheight()
        img_width, img_height = img.size
        x = (screen_width // 2) - (img_width // 2)
        y = (screen_height // 2) - (img_height // 2)
        self.crosshair_window.geometry(f"{img_width}x{img_height}+{x}+{y}")
        
        self.tk_image = ImageTk.PhotoImage(img)
        label = tk.Label(self.crosshair_window, image=self.tk_image, bg="black")
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CrosshairApp(root)
    root.mainloop()
