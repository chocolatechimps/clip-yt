# clip-yt
Save a clip of any YouTube video to your desktop. Download them as audio (mp3) or video (mp4).


Essentially, it formats an ffmpeg command in python and then saves it to your clipboard.
It's pretty jank, but it works.

Written in python and zsh.

clip-yt.py is the only file you need. 
zshrc and installer are part of a semi-automatic macos install.
I will streamline the install process later, but its not a high priority.

Requires:
yt-dlp
  using youtube-dl will result in slow downloads. downloads the video
clipboard
  pip utility to automatically copy the formatted command to the clipboard
ffmpeg
  clips the desired video segment, reformats into audio if desired
