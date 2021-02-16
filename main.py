import subprocess
import re
from os import listdir
from os.path import isfile, join


def main():
    badchars = "[ ]" 
    musicdir = "."
    regex = re.compile("^(.*?)\.")
    
    onlyfiles = [f for f in listdir(musicdir) if isfile(join(musicdir, f))]
    onlyfiles = [s.replace(badchars, "") for s in onlyfiles]
    
    songs = []
    for song in onlyfiles:
        result = regex.search(song)
        songs.append(result.group(0))
    #ffmpeg_driver = subprocess.onlyfiles(["ffmpeg", "-i", f"{song}.mp3"], stdout=subprocess.PIPE)
    mp3extensions = []
    for song in songs:
        songmp3 = f"{song}mp3"
        mp3extensions.append(songmp3)

    for idx, song in enumerate(onlyfiles):
        imp = onlyfiles[idx]
        output = mp3extensions[idx]
        ffmpeg_driver = subprocess.Popen(["ffmpeg", "-i", onlyfiles[idx], mp3extensions[idx]], stdout=subprocess.PIPE)
        ffmpeg_driver.stdout.close()
        ffmpeg_driver.wait()

#    for newsong in newlist:
 #       print(newsong)



if __name__ is main():
    main()
