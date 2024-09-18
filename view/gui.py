import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def log_message(message):
    """Function to log messages to the text area."""
    log_area.insert(END, message + '\n')
    log_area.see(END)  # Automatically scroll to the latest entry

def start_action():
    """Function for the Start button."""
    log_message("Game Started")

def stop_action():
    """Function for the Stop button."""
    log_message("Game Stopped")

app = ttk.Window(themename="darkly")  # Use 'darkly' theme for dark mode

app.title("Texas Holdem")
app.geometry('450x600')

# Configure the grid to allow the window to auto-adjust
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(2, weight=1)

# Create a frame for buttons
frame_buttons = ttk.LabelFrame(app, text="Controls")
frame_buttons.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

# Add Start button using grid and attach the start_action function
start_button = ttk.Button(frame_buttons, text="Start", bootstyle=SUCCESS, command=start_action)
start_button.grid(row=0, column=0, padx=10)

# Add Stop button using grid and attach the stop_action function
stop_button = ttk.Button(frame_buttons, text="Stop", bootstyle=DANGER, command=stop_action)
stop_button.grid(row=0, column=1, padx=10)

# Configure the button frame to expand horizontally
frame_buttons.grid_columnconfigure(0, weight=1)
frame_buttons.grid_columnconfigure(1, weight=1)

# Create a LabelFrame for additional information titled "Info"
frame_info = ttk.LabelFrame(app, text="Info")
frame_info.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

# Add some information inside the Info frame
info_label = ttk.Label(frame_info, text="This is some informational text about the game.")
info_label.grid(row=0, column=0, padx=10, pady=5)

# Create another LabelFrame titled "Details" next to the "Info" frame
frame_details = ttk.LabelFrame(app, text="Details")
frame_details.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

# Add some details inside the "Details" frame
details_label = ttk.Label(frame_details, text="Here are more game details.")
details_label.grid(row=0, column=0, padx=10, pady=5)


# Create a LabelFrame for the text area (logs display) titled "Logs"
frame_logs = ttk.LabelFrame(app, text="Logs")
frame_logs.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

# Add a Text widget for log display with adjusted height (e.g., 15 rows)
log_area = ttk.Text(frame_logs, height=15, width=50)
log_area.grid(row=1, column=0, sticky="nsew")

# Add a vertical scrollbar for the log area
scrollbar = ttk.Scrollbar(frame_logs, orient="vertical", command=log_area.yview)
scrollbar.grid(row=1, column=1, sticky='ns')
log_area.configure(yscrollcommand=scrollbar.set)

# Configure the log frame to expand
frame_logs.grid_columnconfigure(0, weight=1)
frame_logs.grid_rowconfigure(0, weight=1)

app.mainloop()
