#!/bin/zsh

#   clip-yt installer
echo "Start Install"

echo " first, install brew"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo " install ffmpeg"
brew install ffmpeg

echo " install python ( includes pip )"
brew install python3

echo " install clipboard ( from pip )"
pip install clipboard

echo " install youtube-dlp"
brew install yt-dlp/taps/yt-dlp

echo " install vim"
brew install vim

echo " put clip-yt.py in its place"
mkdir ~/.scripts
cp ~/Desktop/clip-yt/clip-yt.py ~/.scripts

echo " make a zshrc - will overwrite whatever you have I think"
echo " if this is an issue for you, sucks to suck should've backed up"

cp ~/Desktop/clip-yt/zshrc ~/.zshrc

echo "\n\ninstall complete. please restart the terminal."
