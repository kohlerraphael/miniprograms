import os
import tkinter as tk
from tkinter import filedialog, messagebox

def find_duplicates(directory):
    duplicates = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            path = os.path.join(root, filename)
            key = (os.path.getsize(path), filename)
            if key in duplicates:
                duplicates[key].append(path)
            else:
                duplicates[key] = [path]
    return [paths for paths in duplicates.values() if len(paths) > 1]

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def compare_files():
    directory = folder_entry.get()
    if not os.path.isdir(directory):
        result_text.set("Please select a valid directory.")
        return

    global duplicates
    duplicates = find_duplicates(directory)
    if not duplicates:
        result_text.set("No duplicates found.")
        return

    global current_tab_index
    current_tab_index = 0
    show_duplicates()

def show_duplicates():
    clear_duplicates_display()

    if not duplicates:
        return

    global current_tab_index
    paths = duplicates[current_tab_index]
    result = ""
    for path in paths:
        file_size_mb = os.path.getsize(path) / (1024 * 1024) # Convert to MB
        file_size_mb = "{:.2f}".format(file_size_mb)  # Format to 2 decimal places
        row_frame = tk.Frame(root)
        row_frame.grid(row=current_tab_index+4, column=0, columnspan=4, padx=5, pady=5, sticky=tk.W+tk.E)

        open_folder_button = tk.Button(row_frame, text="Open Folder", command=lambda p=path: open_folder(p))
        open_folder_button.grid(row=0, column=0, padx=5, pady=5)

        file_size_label = tk.Label(row_frame, text=f"{file_size_mb} MB")
        file_size_label.grid(row=0, column=1, padx=5, pady=5)

        path_label = tk.Label(row_frame, text=path)
        path_label.grid(row=0, column=2, padx=5, pady=5)

        delete_button = tk.Button(row_frame, text="Delete", command=lambda p=path: delete_file(p))
        delete_button.grid(row=0, column=3, padx=5, pady=5)

        current_tab_index += 1

    update_navigation_buttons()

def clear_duplicates_display():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame) and widget.grid_info().get('row', -1) >= 4:
            widget.destroy()

def update_navigation_buttons():
    previous_button.config(state=tk.NORMAL if current_tab_index > 0 else tk.DISABLED)
    next_button.config(state=tk.NORMAL if current_tab_index < len(duplicates) - 1 else tk.DISABLED)

def navigate_previous():
    global current_tab_index
    if current_tab_index > 0:
        current_tab_index -= 1
        show_duplicates()

def navigate_next():
    global current_tab_index
    if current_tab_index < len(duplicates) - 1:
        current_tab_index += 1
        show_duplicates()

# Function to open folder
def open_folder(path):
    os.startfile(os.path.dirname(path))

# Function to delete file
def delete_file(path):
    confirm = messagebox.askyesno("Delete File", "Do you really want to delete this file?")
    if confirm:
        os.remove(path)
        messagebox.showinfo("File Deleted", f"The file {os.path.basename(path)} has been deleted.")
        compare_files()

# GUI setup
root = tk.Tk()
root.title("Duplicate File Detector")

# Title
title_label = tk.Label(root, text="Detect duplicates in the following directory:", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=tk.W)

# Directory selection
folder_label = tk.Label(root, text="Select Folder:")
folder_label.grid(row=1, column=0, padx=5, pady=5)

folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=1, column=1, padx=5, pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=1, column=2, padx=5, pady=5)

# Compare button
compare_button = tk.Button(root, text="Compare", command=compare_files)
compare_button.grid(row=1, column=3, padx=5, pady=5)

# Result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky=tk.W+tk.E)

# Navigation buttons
previous_button = tk.Button(root, text="◀ Previous", command=navigate_previous, state=tk.DISABLED)
previous_button.grid(row=3, column=0, padx=5, pady=5)

next_button = tk.Button(root, text="Next ▶", command=navigate_next, state=tk.DISABLED)
next_button.grid(row=3, column=3, padx=5, pady=5)

# Initialize global variables
duplicates = []
current_tab_index = 0

# Start GUI
root.mainloop()
