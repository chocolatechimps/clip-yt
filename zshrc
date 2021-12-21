
#rice for zsh prompt

#PROMPT='%F{30}%n%F{20} @ %F{6}%1d%F{20} >>> %F{253}'
PROMPT='%F{30}%n%F{244} || %F{6}%1d%F{20} >>> %F{253}'
RPROMPT="%F{63}%* %F{244}|| %F{61}%W %F{reset}"

# general shortcuts

alias c='clear'
alias cls='clear; ls'
alias home='cd ~'
alias ls='ls -G'
alias e='exit'
alias reloadconf='source ~/.zshrc'

#instant access to frequent configs
#prefix is always rc

alias rczsh='vim ~/.zshrc'
alias rcvim='vim ~/.vimrc'

# clip-ty shortcut
alias clipyt='python3 ~/.scripts/clip-yt.py'

