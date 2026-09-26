import tkinter as tk
import tkinter.font as tkfont
from ui import displayvariable
from ui.pageframe import PageFrame

#Main dashboard needs to display:
#RPM, Gear (top right), Lap times (last lap, delta, current lap), Engine temp, Coolant temp

print(displayvariable.RPM.get_value())

class RaceDash(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sooner Racing Dash")
        self.geometry(f"{800}x{480}")
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        
        self.frames=[] #A list of frames representing each individual page
        for i in range(0, 5):
            page_frame = PageFrame(container, self)
            self.frames.append(page_frame)
            page_frame.grid(row=0, column=0, sticky="nsew")

        #Initializing frame and looper
        self.set_frame(0)
        self.update_values()

    def set_frame(self, page_index):
        self.frames[page_index].tkraise()

    def update_values(self):
        print(67)
        self.after(100, self.update_values) 

if __name__ == "__main__":
    app = RaceDash()
    app.mainloop()