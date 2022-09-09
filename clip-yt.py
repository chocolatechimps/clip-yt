import os
import re

#   A YouTube Clip Downloader
#   Download sections of YouTube videos as an mp3 or mp4
#   Requires ffmpeg and yt-dlp
#   Written in Python

#   colors
red = "\u001b[31m"
white = "\u001b[37m"
black = "\u001b[30m"

#   youtube logo
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

#   Version and Credits
print(art)
print(red + "                     Clip-Yt 2.2 by Reid Vanatta 09.09.22\n\n" + white)

#   what video do you want
video = input("Youtube Link:\n")
video = "\"" + video + "\""

#   what format do you want
print()
print("Downlaod as Audio or Video?\n")
print("1. Video (mp4)")
print("2. Audio (mp3)\n")
print("type 1 or 2 and press enter")
format = input("")
print()

# sanitize format input. it can only be 1 or 2
if format.isalpha():
    print(red + 'Please Type 1 or 2' + white)
    exit()
else:
    pass

if int(format) == 2 or int(format) == 1:
    pass
else:
    print(red + 'Please Choose a Valid Format')
    print(white + 'You Entered ' + str(format))
    exit()


#   where should the clip get taken
start = input("Start Time HH:mm:ss :    ")
end = input("Stop  Time HH:mm:ss :    ")

#   make sure the time input is formatted right
#   this is probably the most complex part and
#   could probably be done a lot simpler. regex?
def sanitize_time(time):
    if len(time) != 8 or time[2] != ':' or time[5] != ':':
        print('Make Sure To Include Colons')
        exit()
    else:
        pass

    time_int = input(time.replace(':',''))

    if re.search('[a-zA-z]', time_int) == True:
        print('Only Numbers 0 to 9 and : are Accepted')
    else:
        return True

sanitize_time(start)
sanitize_time(end)

#   start the download
#   these commands are really complicated and you probably don't want to mess with them
print(red + 'Download Starting...')
if int(format) == 1:
    #   downlaod video
    videoCommand = "ffmpeg -ss " + start + " -to " + end + " -i \"$(yt-dlp -f best --get-url " + video + ")\" -c:v copy -c:a copy ~/Desktop/new_clip.mp4;open ~/Desktop/new_clip.mp4"
    os.system(videoCommand)
    print(red + 'Check Your Desktop')
elif int(format) == 2:
    #   download audio
    #   this downloads an mp4 of the clip and then converts it to a mp3 with ffmpeg
    audioCommand = "ffmpeg -ss " + start + " -to " + end + " -i \"$(yt-dlp -f best --get-url " + video + ")\" -c:v copy -c:a copy ~/Desktop/temp_clip.mp4; ffmpeg -i ~/Desktop/temp_clip.mp4 ~/Desktop/new_clip.mp3;rm ~/Desktop/temp_clip.mp4; open ~/Desktop/new_clip.mp3"
    os.system(audioCommand)
    print(red + 'Check Your Desktop')
else:
    print(red + "Invalid Format. Could Not Download" + white)
    quit()
