# clip-yt
Save a clip of any YouTube video to your desktop. Download them as audio (mp3) or video (mp4).

# How it Work
Essentially, it formats an ffmpeg command in python and then saves it to your clipboard.
It's pretty jank, but it functions.
Written in python and zsh.

# Installing
1. copy clip-yt.py to your machine
2. run it with python
3. profit

# Requires:
yt-dlp
    downloads the video. This fork gets around the issue of slow download speeds. 
clipboard
    pip utility to automatically copy the formatted command to the clipboard
ffmpeg
    clips the desired video segment, reformats into audio if desired
