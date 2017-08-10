# Download audio from youtube.com.

Based on https://github.com/rg3/youtube-dl package.

Use this simple script to download audio from youtube following provided link.

Dependencies:
```
ffprobe==0.5
youtube-dl==2017.7.23
```

## Usage
Type python youtube-download-audio.py -h to see a list of command line arguments.

By default sctipt accepts an URL to the youtube playlist/video and then downloads it to the folder named as given playlist/video.

If command line argument `-f|--not-create-folder` passed, the mp3 file will be downloaded into current directory.

The script created file downloads.txt along with downloaded mp3 files.

This file intended to store youtube IDs of already downloaded files, do not remove it if you're planning to interrupt/resume your download, and vise versa, remove it if you want to download some audious that were downloaded before.

