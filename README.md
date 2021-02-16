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
python3 main.py
```

If you want to capture your ffmpeg output you can pipe to a file or pipe to null if you don't care, by default the script prints it.
