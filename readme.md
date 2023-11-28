# YouTube Downloader GUI - Install Guide

##### You will need:
1. An up-to-date Mac
2. Admin/sudo privileges
3. The latest version of Python 3 installed and set as your default interpreter
4. VS Code (or another editor for code that can run Python)

##### Notes
1. If you already have Homebrew installed, skip to step 2
2. Technically, you are not allowed to download YouTube videos (according to YouTube’s terms of service). However, if you exercise good judgment with what you download and don’t violate any copyright laws, you shouldn't any have issues.

## Steps to install:

### Step 1: Install Homebrew
Run the command below and make sure to watch your terminal. After the program finishes installing, _**make sure to run the follow-up
commands**_ it tells you to.
```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Step 2: Using Homebrew, install the youtube-dl package
Run this in your terminal to install youtube-dl, the command line version of the code you are currently installing.
```zsh
brew install youtube-dl
```

### Step 3: Create a configuration file for youtube-dl
First, run this code in the terminal to create the config file for youtube-dl:
```zsh
touch ~/.config/youtube-dl/config
```

Then, run this to open the config file:
```zsh
nano ~/.config/youtube-dl/config
```

Then in this file, paste this (this sets videos to save to your desktop):
```zsh
-o ~/Desktop/%(title)s.%(ext)s
```

Then, on your keyboard, press:

**^ + o (control + o)**
- This stages the text to be saved to the file

**↵ (enter/return)**
- This saves the text to the file

**^ + x (control + x)**
- This closes the file

### Step 4: Clone this GitHub repository to your computer
This is the UI for youtube-dl. By default, the terminal is the only way to interact with youtube-dl. However, this repository has a Python program that will make this easier!
```zsh
git clone https://github.com/beck1888/ytdl-UI.git
```

### Step 5: Open this repository using VS Code
I strongly recommend using VS Code, but you may use a different editor if you know what you’re doing.

### Step 6: Run ‘main.py’
Try it out! This, when run, should show a pop-up window that asks for a video download type and a url. When you press the “Start Download” button, it will look like Python has frozen until the video completes downloading. This is normal. You can check the progress in the VS Code terminal, or use another app until the download is done.