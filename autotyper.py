import tkinter as tk
from tkinter import messagebox
import threading
import time
import pyautogui

class AutoTyperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Typer")

        # Create a frame to contain the widgets for rows 0, 1, and 2
        self.frame = tk.Frame(root, bd=5, relief=tk.GROOVE)
        self.frame.grid(row=0, column=0, rowspan=3, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Title
        self.title_label = tk.Label(self.frame, text="Auto-key-typer", font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Row 0: Text Entry
        self.text_label = tk.Label(self.frame, text="Enter Text:")
        self.text_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.text_entry = tk.Entry(self.frame, width=30)
        self.text_entry.grid(row=1, column=1, padx=5, pady=5)

        # Row 1: Duration Entry
        self.duration_label = tk.Label(self.frame, text="Duration (seconds):")
        self.duration_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.duration_entry = tk.Entry(self.frame, width=10)
        self.duration_entry.grid(row=2, column=1, padx=5, pady=5)

        # Row 3: Start Button and Additional Input with Watermark
        self.start_stop_button = tk.Button(self.frame, text="Start", command=self.start_stop)
        self.start_stop_button.grid(row=3, column=0, padx=5, pady=5)

        self.additional_entry_var = tk.StringVar()
        self.additional_entry = tk.Entry(self.frame, width=30, textvariable=self.additional_entry_var, fg="grey")
        self.additional_entry.grid(row=3, column=1, padx=5, pady=5)
        self.additional_entry_var.set("Printed Text")  # Set watermark text
        self.additional_entry.bind('<FocusIn>', self.on_entry_focus_in)
        self.additional_entry.bind('<FocusOut>', self.on_entry_focus_out)

        self.running = False
        self.thread = None

    def start_stop(self):
        if self.running:
            self.running = False
            self.start_stop_button.config(text="Start")
        else:
            text = self.text_entry.get()
            duration = self.duration_entry.get()
            additional_input = self.additional_entry.get()
            if not text or not duration:
                messagebox.showwarning("Warning", "Please enter text and duration.")
                return
            try:
                duration = float(duration)
                if duration <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Warning", "Duration must be a positive number.")
                return
            self.running = True
            for i in range(5, 0, -1):
                self.start_stop_button.config(text="Start in {} s".format(i))
                self.root.update()
                time.sleep(1)

            self.start_stop_button.config(text="Stop")

            self.thread = threading.Thread(target=self.type_text, args=(text, duration))
            self.thread.start()

    def type_text(self, text, duration):
        while self.running:
            pyautogui.typewrite(text)
            time.sleep(duration)

    def on_entry_focus_in(self, event):
        if self.additional_entry_var.get() == "Printed Text":
            self.additional_entry_var.set("")
            self.additional_entry.config(fg="black")

    def on_entry_focus_out(self, event):
        if not self.additional_entry_var.get():
            self.additional_entry_var.set("Printed Text")
            self.additional_entry.config(fg="grey")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoTyperApp(root)
    root.mainloop()


