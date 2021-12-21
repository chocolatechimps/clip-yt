import clipboard as c

red = "\u001b[31m"
white = "\u001b[37m"
black = "\u001b[30m"

art = black + """MMMMMMMMMMMWNXXKK00OOOkkkkkkxxxxxxxxxxddddxxxxxxxxxxkkkkkkOOO00KKXXNWMMMMMMMMMMM
MMMMMMMWN0xoc::;;;""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """;;;::cox0NWMMMMMMM
MMMMMMNOl;""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """;lONMMMMMM
MMMMMNx;""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """;xNMMMMM
MMMMWO:""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """:OWMMMM
MMMMNd,""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """dNMMMM
MMMWKl,""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """lKWMMM
MMMWO:""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,""" + white + """:l:""" + red + """,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """:OWMMM
MMMWk;""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,""" + white + """;xXKkdc;""" + red + """,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """;kWMMM
MMMNx;""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,""" + white + """;xNWMWX0xol:""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """;xNMMM
MMMNd,""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,""" + white + """;xNMMMMMWWNKkoc;""" + red + """,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """,dNMMM
MMMNd,""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,""" + white + """;xNMMMMMMMMMMWXOxl;""" + red + """,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """dNMMM
MMMNd,""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,""" + white + """;xNMMMMMMMMMMMMMWN0d:""" + red + """,,,,,,,,,,,,,,,,,,,,,,,""" + black + """dNMMM
MMMNd,""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,""" + white + """;xNMMMMMMMMMMMWWXOdc;""" + red + """,,,,,,,,,,,,,,,,,,,,,,,""" + black + """dNMMM
MMMNd""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,""" + white + """;xNMMMMMMMMWN0xo:""" + red + """,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """dNMMM
MMMNx;""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,""" + white + """;xNMMMWWX0Odc;""" + red + """,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """;xNMMM
MMMNx;""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,""" + white + """;xNWNKko:;""" + red + """,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """;xNMMM
MMMWO:""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,""" + white + """;okdc;""" + red + """,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """:OWMMM
MMMW0c,""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """c0WMMM
MMMMXo,""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """oXMMMM
MMMMNx;""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """;xNMMMM
MMMMWKl,""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """lKWMMMM
MMMMMW0l;""" + red +""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """;l0WMMMMM
MMMMMMWXOo:""" + red +""";,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""" + black + """;:oOXWMMMMMM
MMMMMMMMMWX0kxxddoolllcccccc::::::::::::::::::::::::cccccclllooddxxk0XWMMMMMMMMM
MMMMMMMMMMMMMMMMWWWWWWNNNNNNXXXXXXXXXXXKKXXXXXXXXXXXNNNNNNWWWWWWMMMMMMMMMMMMMMMM"""

print(art)
print(red + "                     Clip-Yt 2.1 by Reid Vanatta 08.23.21\n\n" + white)

#   what video do you want
video = input("Youtube Link:\n")
video = "\"" + video + "\""

#   what format do you want
print()
print("Downlaod as Audio or Video?\n")
print("1. Video (mp4)")
print("2. Audio (mp3)\n")
print("type 1 or 2 and press enter")
format = int(input(""))
print()

#   where should the clip get taken
start = input("Start Time HH:mm:ss :    ")
end = input("Stop  Time HH:mm:ss :    ")

if format == 1:
    #   downlaod video
    videoCommand = "ffmpeg -ss " + start + " -to " + end + " -i \"$(yt-dlp -f best --get-url " + video + ")\" -c:v copy -c:a copy /Users/reid/Desktop/new_clip.mp4;echo 'Check Your Desktop'"
    c.copy(videoCommand)
elif format == 2:
    #   download audio
    audioCommand = "ffmpeg -ss " + start + " -to " + end + " -i \"$(yt-dlp -f best --get-url " + video + ")\" -c:v copy -c:a copy /Users/reid/Desktop/temp_clip.mp4; ffmpeg -i ~/Desktop/temp_clip.mp4 ~/Desktop/new_clip.mp3;rm ~/Desktop/temp_clip.mp4; echo 'Check Your Desktop'"
    c.copy(audioCommand)
else:
    print("Invalid Format")
    quit()

print()
print("Command Copied to Clipboard")
print("Paste and Hit Enter to Start Download")
print()


