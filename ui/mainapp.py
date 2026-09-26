import tkinter as tk
import tkinter.font as tkfont

#Main dashboard needs to display:
#RPM, Gear (top right), Lap times (last lap, delta, current lap), Engine temp, Coolant temp

class RaceDash(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Race Dash")
        self.geometry(f"{800}x{480}")
        self.resizable(False, False)

        self.container = tk.Frame(self)

        self.update_values()
    
    def update_values(self):
        print(67)
        self.after(100, self.update_values)
        

if __name__ == "__main__":
    app = RaceDash()
    app.mainloop()