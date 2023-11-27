# IT WORKS!!!
# Even the video works, it's a bit slow, but it works!!!
# 0 Issues with the audio

import ui_window
import os

ui_window.show_ask_UI_window()

received_list = list(ui_window.return_selections())

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


# Run the command
os.system(f"{command}")