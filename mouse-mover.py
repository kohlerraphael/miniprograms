import tkinter as tk
from tkinter import messagebox
import threading
import time
import pyautogui

class AutoMouseMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Mouse Mover")

        # Create a frame for Auto-mouse-mover
        self.frame_auto_mouse_mover = tk.Frame(root, bd=5, relief=tk.GROOVE)
        self.frame_auto_mouse_mover.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Title for Auto-mouse-mover
        self.title_label_auto_mouse_mover = tk.Label(self.frame_auto_mouse_mover, text="Auto Mouse Mover", font=("Helvetica", 16, "bold"))
        self.title_label_auto_mouse_mover.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Record Button for Auto-mouse-mover
        self.record_button_auto_mouse_mover = tk.Button(self.frame_auto_mouse_mover, text="Record", command=self.record_mouse_movement)
        self.record_button_auto_mouse_mover.grid(row=1, column=0, padx=5, pady=5)

        # Countdown Label for Recording
        self.record_countdown_var = tk.StringVar()
        self.record_countdown_label = tk.Label(self.frame_auto_mouse_mover, textvariable=self.record_countdown_var)
        self.record_countdown_label.grid(row=1, column=1, padx=5, pady=5)

        # Display Coordinates Label for Auto-mouse-mover
        self.coordinates_label_auto_mouse_mover = tk.Label(self.frame_auto_mouse_mover, text="Coordinates: (0, 0)")
        self.coordinates_label_auto_mouse_mover.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Row 3: Repetition Period Entry for Auto-mouse-mover
        self.repetition_period_label_auto_mouse_mover = tk.Label(self.frame_auto_mouse_mover, text="Repetition period [s]:")
        self.repetition_period_label_auto_mouse_mover.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.repetition_period_entry_auto_mouse_mover = tk.Entry(self.frame_auto_mouse_mover, width=10)
        self.repetition_period_entry_auto_mouse_mover.grid(row=3, column=1, padx=5, pady=5)

        # Row 4: Replay Button for Auto-mouse-mover
        self.replay_button_auto_mouse_mover = tk.Button(self.frame_auto_mouse_mover, text="Replay", command=self.replay_mouse_movement)
        self.replay_button_auto_mouse_mover.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Countdown Label for Replay
        self.replay_countdown_var = tk.StringVar()
        self.replay_countdown_label = tk.Label(self.frame_auto_mouse_mover, textvariable=self.replay_countdown_var)
        self.replay_countdown_label.grid(row=4, column=2, padx=5, pady=5)

        # Additional Variables for Auto-mouse-mover
        self.recording = False
        self.mouse_movements = []
        self.replay_active = False
        self.is_recording = False  # Add this flag to track recording state

    def record_mouse_movement(self):
        if self.is_recording:
            # Stop recording
            self.is_recording = False
            self.record_button_auto_mouse_mover.config(text="Record")
            self.record_countdown_var.set("Recording stopped")
            print(self.mouse_movements)
        else:
            # Start recording
            self.record_button_auto_mouse_mover.config(state=tk.DISABLED)
            self.update_record_countdown(5)

    def update_record_countdown(self, count):
        if count > 0:
            self.record_countdown_var.set(str(count))
            self.root.after(1000, self.update_record_countdown, count - 1)
        else:
            self.start_recording()

    def start_recording(self):
        self.record_countdown_var.set("")
        self.is_recording = True
        self.record_button_auto_mouse_mover.config(state=tk.NORMAL, text="Stop Recording")
        self.track_mouse_movement()

    def track_mouse_movement(self):
        if self.is_recording:
            x, y = pyautogui.position()
            self.mouse_movements.append((x, y))
            self.coordinates_label_auto_mouse_mover.config(text="Coordinates: ({}, {})".format(x, y))
            self.root.after(50, self.track_mouse_movement)  # Check position every 100 milliseconds

    def replay_mouse_movement(self):
        if not self.replay_active:
            self.replay_active = True
            self.replay_button_auto_mouse_mover.config(text = "Stop replay")
            if not self.is_recording and len(self.mouse_movements) > 0:
                period = float(0.050) # replay movements with same period as recording
                # self.replay_button_auto_mouse_mover.config(state=tk.DISABLED)
                threading.Thread(target=self.perform_replay, args=(period,)).start()
            else:
                messagebox.showwarning("Warning", "No recorded movements to replay.")
        elif self.replay_active:
            self.replay_active = False
            self.replay_button_auto_mouse_mover.config(text="Replay")


    def perform_replay(self, period):
            self.update_replay_countdown(3)
            time.sleep(3)  # Countdown period
            while(True):
                for movement in self.mouse_movements:
                    if not self.replay_active:
                        break
                    pyautogui.moveTo(movement[0], movement[1], duration=0.1)
                    time.sleep(period)
                time.sleep(float(self.repetition_period_entry_auto_mouse_mover.get()))
            self.replay_active = False
            self.replay_button_auto_mouse_mover.config(state=tk.NORMAL)

    def update_replay_countdown(self, count):
        if count > 0:
            self.replay_countdown_var.set(str(count))
            self.root.after(1000, self.update_replay_countdown, count - 1)
        else:
            self.replay_countdown_var.set("")
            self.replay_active = True

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoMouseMoverApp(root)
    root.mainloop()

