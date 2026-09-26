import random
import tkinter as tk
from tkinter import font as tkfont


# Each entry: (label text, starting value, min, max) - purely for the fake
# data generator below. Replace the fake data with real CAN values later;
# see update_values() for exactly where that swap happens.
READOUTS = [
    ("Engine Temperature (F)", 180, 150, 230),
    ("Lambda", 1.0, 0.7, 1.3),
    ("TPS (%)", 0, 0, 100),
    ("Wheel Speed (RPM)", 0, 0, 1200),
    ("Engine RPM", 0, 0, 8000),
    ("Tire Temp (F)", 90, 70, 160),
    ("Battery Voltage", 13.2, 11.5, 14.5),
    ("MAP (PSI)", 14, 5, 30),
    ("Intake Air Temp (F)", 80, 60, 140),
]


class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DiagWindow")
        self.configure(bg="black")
        self.geometry("900x500")

        digit_font = tkfont.Font(family="Arial", size=32, weight="bold")
        label_font = tkfont.Font(family="Verdana", size=11)

        header = tk.Label(self, text="Engine Diagnostics", bg="black", fg="white",
                           font=("Segoe UI", 14), anchor="w")
        header.grid(row=0, column=0, columnspan=3, sticky="w", padx=15, pady=(15, 5))

        # value_labels keeps a handle to each number's Label widget so we
        # can update its text later without rebuilding the whole grid.
        self.value_labels = {}

        # --- Grid placement -----------------------------
        # We keep track of "where are we right now" with two plain
        # variables, and move them ourselves after placing each readout.
        # Row 0 is the header, so the first readout starts at row 1.
        current_row = 1
        current_col = 0
        columns_per_row = 3

        for readout in READOUTS:
            # Pull the four pieces out of this readout by name, one at a
            # time, instead of unpacking them all in the loop header.
            name = readout[0]
            start = readout[1]
            lo = readout[2]
            hi = readout[3]

            # The caption ("Engine RPM") goes on the row we're currently at.
            caption = tk.Label(self, text=name, bg="black", fg="white", font=label_font)
            caption.grid(row=current_row, column=current_col,
                         sticky="w", padx=15, pady=(10, 0))

            # The white value box goes one row directly below the caption.
            box = tk.Frame(self, bg="white", highlightbackground="#8fa8bf",
                            highlightthickness=1)
            box.grid(row=current_row + 1, column=current_col,
                      sticky="nsew", padx=15, pady=(0, 15))

            value = tk.Label(box, text=str(start), bg="white",
                              font=digit_font, fg="black")
            value.pack(padx=10, pady=8)

            self.value_labels[name] = (value, lo, hi)

            # Move to the next column for the next readout.
            current_col = current_col + 1

            # If we've just filled the last column in this row, wrap
            # around: go back to column 0, and drop down to the next
            # free row. Each readout uses 2 grid rows (caption + box),
            # so we skip down by 2, not 1.
            if current_col == columns_per_row:
                current_col = 0
                current_row = current_row + 2
        # --------------------------------------------------------------

        for c in range(columns_per_row):
            self.grid_columnconfigure(c, weight=1)

        # self.update_values()

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()