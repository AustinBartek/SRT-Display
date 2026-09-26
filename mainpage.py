import tkinter as tk
import tkinter.font as tkfont
WIDTH, HEIGHT = 800, 480
BG = "black"

class RaceDash(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Race Dash")
        self.geometry(f"{800}x{480}")
        self.configure(bg=BG)
        self.resizable(False, False)

        # Create a canvas to draw on
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg=BG, highlightthickness=0)
        self.canvas.pack()
        #da middle ones
        self.canvas.create_rectangle(WIDTH//2 - 100, 10, WIDTH//2 + 100, 200, outline="White", width=5)
        self.canvas.create_rectangle(WIDTH//2 - 100, 210, WIDTH//2 + 100, HEIGHT - 10, outline="White", width=5)
        #3 left side rectangles
        self.canvas.create_rectangle(10, 10, 290, 150, outline="White", width=5)
        self.canvas.create_rectangle(10, 160, 290, 300, outline="White", width=5)
        self.canvas.create_rectangle(10, 310, 290, 470, outline="White", width=5)
        #3 right side rectangles
        self.canvas.create_rectangle(WIDTH - 290, 10, WIDTH - 10, 150, outline="White", width=5)
        self.canvas.create_rectangle(WIDTH - 290, 160, WIDTH - 10, 300, outline="White", width=5)
        self.canvas.create_rectangle(WIDTH - 290, 310, WIDTH - 10, 470, outline="White", width=5)
        self.canvas.create_text(WIDTH//2, 250, text="Gear", fill="White", font=("Arial", 24))

if __name__ == "__main__":
    app = RaceDash()
    app.mainloop()