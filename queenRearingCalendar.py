import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime, timedelta
import webbrowser

def generate_event_url(summary, start_date):
    base_url = "https://calendar.google.com/calendar/render?action=TEMPLATE"
    start_date_str = start_date.strftime('%Y%m%d')
    event_url = f"{base_url}&text={summary}&dates={start_date_str}/{start_date_str}&ctz=Europe/Berlin"
    return event_url

def export_to_google_calendar():
    events = [
        ("Brutwaben hinzufügen und füttern", strengthenColony_date_label.cget("text")),
        ("Königin entfernen", removeOld_date_label.cget("text")),
        ("Zuchtrahmen einsetzen", zr_einsetzen_date_label.cget("text")),
        ("2. Serie + Zellen gegen Verbauen schützen", serie_date_label.cget("text")),
        ("Zellen einkäfigen", cage_now_date_label.cget("text")),
        ("Schlupfkontrolle", schlupfkontrolle_date_label.cget("text"))
    ]

    for summary, date_str in events:
        if date_str:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            event_url = generate_event_url(summary, date)
            webbrowser.open(event_url)

def on_date_selected(event):
    selected_date = cal.selection_get()
    date_str = selected_date.strftime('%Y-%m-%d')

    strengthenColony_date = selected_date + timedelta(days=-20)
    strengthenColony_label.config(text=f"Brutwaben hinzufügen und füttern:")
    strengthenColony_date_label.config(text=strengthenColony_date.strftime('%Y-%m-%d'))

    removeOld_date = selected_date + timedelta(days=-9)
    removeOld_label.config(text=f"Königin entfernen:")
    removeOld_date_label.config(text=removeOld_date.strftime('%Y-%m-%d'))

    zr_einsetzen_label.config(text=f"Zuchtrahmen einsetzen:")
    zr_einsetzen_date_label.config(text=date_str)

    serie_date = selected_date + timedelta(days=5)
    serie_label.config(text=f"2. Serie + zellen gegen Verbauen schützen:")
    serie_date_label.config(text=serie_date.strftime('%Y-%m-%d'))

    cage_now_date = selected_date + timedelta(days=10)
    cage_now_label.config(text=f"Zellen einkäfigen:")
    cage_now_date_label.config(text=cage_now_date.strftime('%Y-%m-%d'))

    schlupfkontrolle_date = selected_date + timedelta(days=13)
    schlupfkontrolle_label.config(text=f"Schlupfkontrolle:")
    schlupfkontrolle_date_label.config(text=schlupfkontrolle_date.strftime('%Y-%m-%d'))

# Create the main window
root = tk.Tk()
root.title("Date Selection Program")
title_label = tk.Label(root, text="Datum des Umlarvens auswählen:", font=("Helvetica", 16, "bold"), fg="black")
title_label.pack(pady=10)

# Create a calendar widget
cal = Calendar(root, selectmode='day', date_pattern='y-mm-dd')
cal.pack(pady=20)

# Bind the calendar date selection event
cal.bind("<<CalendarSelected>>", on_date_selected)

# Create a main frame to hold everything
main_frame = tk.Frame(root)
main_frame.pack(pady=10, padx=10)

# Create a frame to hold the labels and dates
left_frame = tk.LabelFrame(main_frame, text="Tasks", padx=10, pady=10)
left_frame.pack(side="left", fill="both", expand=True)

# Custom font and color settings for the labels
label_font = ("Arial", 12, "normal")
label_color = "black"

# Labels to display the tasks
strengthenColony_label = ttk.Label(left_frame, text="(-20) Brutwaben hinzufügen und füttern:", font=label_font, foreground=label_color)
strengthenColony_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
strengthenColony_date_label = ttk.Label(left_frame, text="", font=label_font, foreground=label_color)
strengthenColony_date_label.grid(row=0, column=1, sticky='w', padx=5, pady=5)

removeOld_label = ttk.Label(left_frame, text="(-1) Königin entfernen:", font=label_font, foreground=label_color)
removeOld_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
removeOld_date_label = ttk.Label(left_frame, text="", font=label_font, foreground=label_color)
removeOld_date_label.grid(row=1, column=1, sticky='w', padx=5, pady=5)

zr_einsetzen_label = ttk.Label(left_frame, text="(0) Zuchtrahmen einsetzen:", font=("Arial", 14, "bold"), foreground="green")
zr_einsetzen_label.grid(row=2, column=0, sticky='w', padx=5, pady=5)
zr_einsetzen_date_label = ttk.Label(left_frame, text="", font=("Arial", 14, "bold"), foreground="green")
zr_einsetzen_date_label.grid(row=2, column=1, sticky='w', padx=5, pady=5)

serie_label = ttk.Label(left_frame, text="(5) 2. Serie + Zellen gegen Verbauen schützen:", font=label_font, foreground=label_color)
serie_label.grid(row=3, column=0, sticky='w', padx=5, pady=5)
serie_date_label = ttk.Label(left_frame, text="", font=label_font, foreground=label_color)
serie_date_label.grid(row=3, column=1, sticky='w', padx=5, pady=5)

info_label = ttk.Label(left_frame, text="day 6-9 crucial for larvae don't shake frame", font=label_font, foreground=label_color)
info_label.grid(row=4, column=0, sticky='w', padx=5, pady=5)

cage_now_label = ttk.Label(left_frame, text="(10) Zellen einkäfigen:", font=label_font, foreground=label_color)
cage_now_label.grid(row=5, column=0, sticky='w', padx=5, pady=5)
cage_now_date_label = ttk.Label(left_frame, text="", font=label_font, foreground=label_color)
cage_now_date_label.grid(row=5, column=1, sticky='w', padx=5, pady=5)

schlupfkontrolle_label = ttk.Label(left_frame, text="(13) Schlupfkontrolle:", font=label_font, foreground=label_color)
schlupfkontrolle_label.grid(row=6, column=0, sticky='w', padx=5, pady=5)
schlupfkontrolle_date_label = ttk.Label(left_frame, text="", font=label_font, foreground=label_color)
schlupfkontrolle_date_label.grid(row=6, column=1, sticky='w', padx=5, pady=5)

# Create a frame for the text box
right_frame = tk.LabelFrame(main_frame, text="Notes", padx=10, pady=10)
right_frame.pack(side="right", fill="both", expand=True)

# Add a text box with bullet points
text_box = tk.Text(right_frame, wrap="word", width=40, height=15)
text_box.pack(pady=10, padx=10)
text_box.insert(tk.END, "• Day 0, insert rearing frame with youngest larvae\n" +
                "• Preparation - Increase strength of colony by adding brood, pollen, nurse bees" +
                "• Point 1 - day 6-9 mustnt fall out of royal jelley\n" +
                "• Point 2 - Cage the cells  day 5, 10, 11 or 12 \n" +
                "• Point 3 - Queens will hatch day 13 \n" +
                "• Point 4 - After hatching check and carefully open all cells\n" +
                "• Point 5 - Use mating boxes only after queen bees have hatched")

# Add an export button
export_button = tk.Button(root, text="Export to Google Calendar", command=export_to_google_calendar)
export_button.pack(pady=10)

# Run the application
root.mainloop()
