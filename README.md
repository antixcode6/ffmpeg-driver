# ffmpeg-driver 

When dealing with a lot of content of different file types that you are trying to push to a common file type - in my case MP3 - you may realize ffmpeg can only convert a single song at a time. This can be a pain in the butt if you have more than 10 files. 

So to resolve this issue I wrote a script in Python to

1. Capture file names in dir
1. Remove any unwanted [] in the name
1. Run a bulk conversion through ffmpeg to mp3

This will automatically leave the original files but if you are on linux this is as simple as doing an `rm *.mp4` or whatever.

# Usage
Drop the main.py file into the directory you wish to convert and run it, simple as. 

```
cd ~/Music/Alternative
git clone https://github.com/antixcode6/ffmpeg-driver.git
cd ffmpeg-driver

usage: ffmpy.py [-h] [-p PATH] [-S] [-f]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  The directory you want to exec this command on
  -S, --simulate        Run it without really running it
  -f, --force           This causes the program to be forced i.e. ffmpeg will not ask to overwrite files
```

```
python3 main.py -p "$HOME/testdir" -S

Output:
ffmpeg-driver git:(dev) ✗ python3 main.py -p "/home/grumbulon/testdir" -S
Changes that would have occured

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
The Caretaker - Everywhere at the end of time - Stage 3 (FULL ALBUM)-DuIGJiqCb8w.webm | The Caretaker - Everywhere at the end of time - Stage 3 (FULL ALBUM)-DuIGJiqCb8w.mp3
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
The Caretaker - Everywhere at the end of time - Stage 2 (FULL ALBUM)-4toH7J0cXR0.webm | The Caretaker - Everywhere at the end of time - Stage 2 (FULL ALBUM)-4toH7J0cXR0.mp3
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
The Caretaker - Everywhere At The End Of Time - Stage 6 (FULL ALBUM)-sM5hlrkaPSo.mkv | The Caretaker - Everywhere At The End Of Time - Stage 6 (FULL ALBUM)-sM5hlrkaPSo.mp3
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
The Caretaker - Everywhere At The End Of Time - Stage 4 (FULL ALBUM)-6gahbDemo-I.webm | The Caretaker - Everywhere At The End Of Time - Stage 4 (FULL ALBUM)-6gahbDemo-I.mp3
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
The Caretaker - Everywhere At The End Of The Time-j_rEHstx7v4.webm | The Caretaker - Everywhere At The End Of The Time-j_rEHstx7v4.mp3
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
The Caretaker -  Everywhere At The End Of Time - Stage 5 (FULL ALBUM)-5uLEZYLkGRU.webm | The Caretaker -  Everywhere At The End Of Time - Stage 5 (FULL ALBUM)-5uLEZYLkGRU.mp3
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
The Caretaker - Everywhere At The End Of Time - Stages 1-6 (Complete)-wJWksPWDKOc.webm | The Caretaker - Everywhere At The End Of Time - Stages 1-6 (Complete)-wJWksPWDKOc.mp3
```

If you want to capture your ffmpeg output you can pipe to a file or pipe to null if you don't care, by default the script prints it.
