def show_ask_UI_window():
    import tkinter as tk
    from tkinter import ttk
    import os

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