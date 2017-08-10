# -*- coding: utf-8 -*-

"""Download audio from youtube.com.
Use this simple script to download audio from
youtube following provided link.
Type python youtube-download-audio.py -h to see a list of
command line arguments.
Dependencies:
ffprobe==0.5
youtube-dl==2017.7.23
By default sctipt accepts an URL to the youtube playlist/video
and then downloads it to the folder named as given playlist/video.
If command line argument -f|--not-create-folder passed, the mp3 file
will be downloaded into current directory.
The script created file downloads.txt along with downloaded mp3 files.
This file intended to store youtube IDs of already downloaded files, do
not remove it if you're planning to interrupt/resume your download, and
vise versa, remove it if you want to download some audious that were downloaded
before.
"""

from __future__ import unicode_literals
from youtube_dl import YoutubeDL
import os
import argparse
import glob

# Default values
create_folder = True
create_plst = False

# CMD arguments
parser = argparse.ArgumentParser(
    description='Download mp3 files from provided youtube playlist URL'
)
parser.add_argument(
    '-u',
    '--url',
    action='store',
    dest='url',
    default=None,
    help='Required youtube URL. You can pass either playlist or single video URL',
    required=True
)
parser.add_argument(
    '-f',
    '--not-create-folder',
    action='store_false',
    dest='fold',
    help='Don\'t create a folder'
)
parser.add_argument(
    '-p',
    '--playlist',
    action='store_true',
    dest='plst',
    help='Create an m3u playlist from downloaded files'
)

parser.set_defaults(fold=True, plst=False)
results = parser.parse_args()
url = results.url
create_folder = results.fold
create_plst = results.plst

# Get playlist title and create a folder for it the argument
# -f wasn't present
foldername = ''
if create_folder:
    ydl_init_opts = {
        'quiet': True,
        'extract_flat': True
    }
    ydl_init = YoutubeDL(ydl_init_opts)
    ydl_init.add_default_info_extractors()
    info = ydl_init.extract_info(url, download=False)

    foldername = '{}/'.format(info['title'])

    if not os.path.exists(foldername):
        os.makedirs(foldername)

# Options for actual audio download
ydl_opts = {
    'verbose': True,
    'outtmpl': '{}%(title)s.%(ext)s'.format(foldername),
    'download_archive': '{}downloads.txt'.format(foldername),
    'format': 'bestaudio/best',  # choice of quality
    'yesplaylist': True,        # download playlist
    'ignoreerrors': True,       # ignore errors
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
ydl = YoutubeDL(ydl_opts)

ydl.download([url])

# Create playlist if there's agument -p passed
if create_plst:
    for (path, subdirs, files) in os.walk(foldername):
        os.chdir(path)
        if glob.glob("*.mp3") != []:
            _m3u = open(
                '{}.m3u'.format(foldername[:-1]),
                "w",
                encoding='utf-8'
            )
            for song in glob.glob("*.mp3"):
                _m3u.write(
                    u'{}\n'.format(song)
                )
            _m3u.close()
