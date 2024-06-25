# pyinstaller --onefile --distpath C:\\path\\to\\output\\directory duplicate_file_detector.py


import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from tqdm import tqdm
import time
import threading

def browse_input_file():
    input_file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file_path)

def browse_output_directory():
    output_directory_path = filedialog.askdirectory()
    output_directory_entry.delete(0, tk.END)
    output_directory_entry.insert(0, output_directory_path)

def create_exe():
    input_file = input_file_entry.get()
    output_directory = output_directory_entry.get()

    if not input_file or not output_directory:
        messagebox.showerror("Error", "Please select both input file and output directory.")
        return

    def run_pyinstaller():
        try:
            subprocess.run(['pyinstaller', '--onefile', '--distpath', output_directory, input_file], check=True)
            messagebox.showinfo("Success", "Executable file created successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    progress_window = tk.Toplevel(root)
    progress_window.title("Creating .exe File")

    progress_label = tk.Label(progress_window, text="Creating .exe file...")
    progress_label.pack(padx=20, pady=10)

    progress_bar = tqdm(total=100, file=progress_window)

    def update_progress():
        for i in range(100):
            progress_bar.update(1)
            time.sleep(0.05)
        progress_bar.close()
        progress_window.destroy()

    threading.Thread(target=run_pyinstaller).start()
    threading.Thread(target=update_progress).start()

# GUI setup
root = tk.Tk()
root.title("Exe Creator")

# Input file selection
input_file_label = tk.Label(root, text="Select the input file:")
input_file_label.grid(row=0, column=0, padx=5, pady=5)

input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=5, pady=5)
input_file_entry.insert(0, "Select the input file")

browse_input_button = tk.Button(root, text="Browse", command=browse_input_file)
browse_input_button.grid(row=0, column=2, padx=5, pady=5)

# Output directory selection
output_directory_label = tk.Label(root, text="Select the output directory:")
output_directory_label.grid(row=1, column=0, padx=5, pady=5)

output_directory_entry = tk.Entry(root, width=50)
output_directory_entry.grid(row=1, column=1, padx=5, pady=5)
output_directory_entry.insert(0, "Select the output directory")

browse_output_button = tk.Button(root, text="Browse", command=browse_output_directory)
browse_output_button.grid(row=1, column=2, padx=5, pady=5)

# Create .exe button
create_exe_button = tk.Button(root, text="Create .exe file", command=create_exe)
create_exe_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# PyInstaller command text
pyinstaller_command_label = tk.Label(root, text="PyInstaller command:")
pyinstaller_command_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

pyinstaller_command_text = tk.Text(root, height=2, width=60)
pyinstaller_command_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
pyinstaller_command_text.insert(tk.END, "pyinstaller --onefile --distpath C:\\path\\to\\output\\directory file_name.py")

root.mainloop()


# pyinstaller --onefile --distpath C:\\path\\to\\output\\directory duplicate_file_detector.py