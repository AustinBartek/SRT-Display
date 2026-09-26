import tkinter as tk
from data.common import WIDTH, HEIGHT

# Every page will have a 3 columns, the first and last with 3 rows, and the middle with 2.
class PageFrame(tk.Frame):
    def __init__(self, parent, controller, index):
        super().__init__(parent)

        self.parent = parent
        self.controller = controller

        c=tk.Canvas(self, width=WIDTH, height=HEIGHT, highlightthickness=0)
        self.canvas = c
        c.pack()
            
        c.create_oval(WIDTH*4//5,-HEIGHT//2,WIDTH*3//2,HEIGHT//2)
