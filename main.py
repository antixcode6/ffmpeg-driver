import argparse
import subprocess
import re
from os import listdir
from os.path import isfile, join


class ffmpeg_driver:
    def __init__(self, path, simulate, force, old_music_dir=[], new_music_dir=[]):
        self.path = path
        self.simulate = simulate
        self.force = force

    def format_songs(self) -> list:
        musicdir = self.path
        bad_chars = "[ ]"
        regex = re.compile("^(.*?)\.")
        bad_file_ext = (".py", ".mp3")
        self.old_music_dir = [f for f in listdir(musicdir) if isfile(join(musicdir, f))]
        self.old_music_dir = [
            f for f in self.old_music_dir if not f.endswith(bad_file_ext)
        ]
        self.old_music_dir = [s.replace(bad_chars, "") for s in self.old_music_dir]

        songs = []
        for song in self.old_music_dir:
            result = regex.search(song)
            songs.append(result.group(0))

        mp3extensions = []
        for song in songs:
            songmp3 = f"{song}mp3"
            mp3extensions.append(songmp3)

        self.new_music_dir = mp3extensions

    def execute(self):
        width = len(self.old_music_dir[0]) * 2
        if self.simulate:
            print("Changes that would have occured\n")
        for idx, song in enumerate(self.old_music_dir):
            imp = self.old_music_dir[idx]
            output = self.new_music_dir[idx]
            print(f"|{width*'-'}|")
            print(f"{imp} | {output}")

        if self.force:
            for idx, song in enumerate(self.old_music_dir):
                ffmpeg_driver = subprocess.Popen(
                    [
                        "ffmpeg",
                        "-i",
                        f"{self.path}/{self.old_music_dir[idx]}",
                        f"{self.path}/{self.new_music_dir[idx]}",
                        "-y",
                    ],
                    stdout=subprocess.PIPE,
                )
                ffmpeg_driver.stdout.close()
                ffmpeg_driver.wait()
        else:
            for idx, song in enumerate(self.old_music_dir):
                ffmpeg_driver = subprocess.Popen(
                    [
                        "ffmpeg",
                        "-i",
                        f"{self.path}/{self.old_music_dir[idx]}",
                        f"{self.path}/{self.new_music_dir[idx]}",
                    ],
                    stdout=subprocess.PIPE,
                )
                ffmpeg_driver.stdout.close()
                ffmpeg_driver.wait()


def arg_parse():
    params = argparse.ArgumentParser()
    params.add_argument(
        "-p",
        "--path",
        help="The directory you want to exec this command on",
        type=str,
    )
    params.add_argument(
        "-S",
        "--simulate",
        help="Run it  without really running it",
        action="store_true",
    )
    params.add_argument(
        "-f",
        "--force",
        help="This causes the program to be forced i.e. ffmpeg will not ask to overwrite files nicely",
        action="store_true",
    )

    return params.parse_args()


def main():
    args = arg_parse()

    driver = ffmpeg_driver(args.path, args.simulate, args.force)
    driver.format_songs()
    driver.execute()


if __name__ is main():
    main()


