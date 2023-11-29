# From ui_window.py

def show_ask_UI_window():
    import tkinter as tk
    from tkinter import ttk
    # import os

    def on_submit():
        global selected_option
        global entered_text
        selected_option = dropdown.get()
        entered_text = entry.get()


        # Close the pop-up window
        popup.destroy()

        # Kill the Python process
        root.destroy()

        # return [selected_option, entered_text]

    # Create the main window
    root = tk.Tk()
    root.withdraw()
    root.title("YouTube-dl UI")

    # Create a pop-up window
    popup = tk.Toplevel(root)
    popup.geometry("600x250")


    # Dropdown options
    options = ['audio (.mp3)', 'video (.mp4)']

    # Create and place the dropdown
    dropdown_label = ttk.Label(popup, text="Select a format for your download")
    dropdown_label.pack(pady=10)

    dropdown = ttk.Combobox(popup, values=options, state="readonly")
    dropdown.pack(pady=10)

    # Create and place the text box with a wider width (e.g., width=30)
    entry_label = ttk.Label(popup, text="Paste video the full URL:")
    entry_label.pack(pady=10)

    entry = ttk.Entry(popup, width=50)  # Adjust the width as needed
    entry.pack(pady=10)

    # Create and place the submit button
    submit_button = ttk.Button(popup, text="Start Download", command=on_submit)
    submit_button.pack(pady=20)

    # Run the main loop
    root.mainloop()

def return_selections():
    list_of_return = [selected_option, entered_text]
    return list_of_return




# - - - - - - 
# Start of active code


import os

show_ask_UI_window()

received_list = list(return_selections())

# Clean up media type and set URL to own var
if received_list[0] == 'audio (.mp3)':
    media_type = 'mp3'
else:
    media_type = 'mp4'

url = received_list[1]

# print(f"{media_type}, {url}") # Check outputs

# Build command
# PLEASE KEEP IN MIND THAT THIS COMMAND ASSUMES THE .CONFIG FILE IS SET TO DESKTOP
if media_type == 'mp3': # Command for audio only
    command = f"youtube-dl --extract-audio --audio-format mp3 '{url}'"
else: # Mp4 file
    command = f"youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' '{url}'"


# Run the command (print only for now - testing)
print(command)
# os.system(f"{command}")