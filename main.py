import argparse
import subprocess
import re
from os import listdir
from os.path import isfile, join


def arg_parse():
    params = argparse.ArgumentParser()
    params.add_argument(
        "-p", "--path", help="The directory you want to exec this command on", type=str
    )
    params.add_argument(
        "-S",
        "--simulate",
        help="Run it  without really running it",
        action="store_true",
    )
    return params.parse_args()


def main():
    # Implement checking list to make sure script only converts video and music files
    args = arg_parse()

    badchars = "[ ]"
    musicdir = args.path
    regex = re.compile("^(.*?)\.")

    onlyfiles = [f for f in listdir(musicdir) if isfile(join(musicdir, f))]
    onlyfiles = [s.replace(badchars, "") for s in onlyfiles]

    songs = []
    for song in onlyfiles:
        result = regex.search(song)
        songs.append(result.group(0))
    mp3extensions = []
    for song in songs:
        songmp3 = f"{song}mp3"
        mp3extensions.append(songmp3)

    if args.simulate:
        width = len(onlyfiles[0]) * 2
        print("Changes that would have occured\n")
        for idx, song in enumerate(onlyfiles):
            imp = onlyfiles[idx]
            output = mp3extensions[idx]
            print(f"|{width*'-'}|")
            print(f"{imp} | {output}")
    else:
        for idx, song in enumerate(onlyfiles):
            ffmpeg_driver = subprocess.Popen(
                [
                    "ffmpeg",
                    "-i",
                    f"{musicdir}/{onlyfiles[idx]}",
                    f"{musicdir}/{mp3extensions[idx]}",
                ],
                stdout=subprocess.PIPE,
            )
            ffmpeg_driver.stdout.close()
            ffmpeg_driver.wait()


if __name__ is main():
    main()
