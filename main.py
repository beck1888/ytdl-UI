# main.py

# Import libraries
import tkinter as tk # deals with gui
from tkinter import ttk # same module as above, just called in a specific way
import os # used to run the formatted yt-dl command in the users terminal
import sys
import threading

# Define functions
def show_ask_UI_window():
    def on_submit():
        # root.destroy()
        global selected_option
        global entered_text
        selected_option = dropdown.get()
        entered_text = entry.get()
        print("Point 1 clear")
        # close tkinter
        popup.destroy()
        root.destroy()

    # Create the main window
    root = tk.Tk()
    root.withdraw()
    root.title("YouTube-dl UI")

    # Create the pop-up window
    popup = tk.Toplevel(root)
    popup.geometry("600x250")

    options = ['audio (.mp3)', 'video (.mp4)'] # Dropdown options for the pop-up

    # Create and place the dropdown
    dropdown_label = ttk.Label(popup, text="Select a format for your download")
    dropdown_label.pack(pady=10)
    dropdown = ttk.Combobox(popup, values=options, state="readonly")
    dropdown.pack(pady=10)

    # Create and place the text box
    entry_label = ttk.Label(popup, text="Paste video the full URL:")
    entry_label.pack(pady=10)
    entry = ttk.Entry(popup, width=50)
    entry.pack(pady=10)

    # Create and place the submit button
    submit_button = ttk.Button(popup, text="Start Download", command=on_submit)
    submit_button.pack(pady=20)

    # Run the main loop (needed for tkinter to function)
    root.mainloop()
    # root.quit()

def return_selections(): # Outputs selected format and pasted URL which becomes a list
    list_of_return = [selected_option, entered_text]
    return list_of_return

# CODE THAT RUNS STARTS HERE
show_ask_UI_window() # Puts up the graphical window that asks for the inputs

received_list = return_selections() # Gets the selections and inputs from the GUI as a list

url = received_list[1] # Set the URL to the second item in the list returned

# Build the command to run in the user's terminal
if received_list[0] == 'audio (.mp3)': # If the user only wants audio
    command = f"youtube-dl --extract-audio --audio-format mp3 '{url}'"
else: # If audio is not selected, the other option (mp4) is what the user wants
    command = f"youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' '{url}'"



# Run the command (print only for now - testing)
import time
print(command)
to_run = command

for i in range(10):
    time.sleep(0.4)
    percent = str(10 * round(((10 * (i+1)))/10))
    print(f"{percent}% done")

'''What if instead, the progress of the download is just displayed in another tkinter window'''

# os.system(f"{command}")