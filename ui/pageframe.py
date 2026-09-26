import tkinter as tk

class PageFrame(tk.Frame):
    # Create a canvas to draw on
            c=tk.Canvas(self, width=WIDTH, height=HEIGHT, bg=BG, highlightthickness=0)
            self.canvas = c
            c.pack()
            
            c.create_oval(WIDTH*4//5,-HEIGHT//2,WIDTH*3//2,HEIGHT//2)
            #self.canvas.create_rectangle(WIDTH//2 - 100, 10, WIDTH//2 + 100, 200, outline="White", width=5)
            #self.canvas.create_text(WIDTH//2, 250, text="Gear", fill="White", font=("Arial", 24))