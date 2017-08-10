# Download audio from youtube.com.

Based on https://github.com/rg3/youtube-dl package.

Use this simple script to download audio from youtube following provided link.

Dependencies:
```
ffprobe==0.5
youtube-dl==2017.7.23
```

## Installation

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage
Type `python youtube-download-audio.py -h` to see a list of command line arguments.

By default sctipt accepts an URL to the youtube playlist/video and then downloads it to the folder named as given playlist/video.

If command line argument `-f|--not-create-folder` passed, the mp3 file will be downloaded into current directory.

The script creates file `downloads.txt` along with downloaded mp3 files.
This file intended to store youtube IDs of already downloaded files, do not remove it if you're planning to interrupt/resume your download, and vise versa, remove it if you want to download some audious that were downloaded before.

## Possible issue

If you're getting an error `PostProcessingError('ffprobe or avprobe not found. Please install one.')` while running a script at the first time, you may find a solution [here](https://github.com/NixOS/nixpkgs/issues/5236)
