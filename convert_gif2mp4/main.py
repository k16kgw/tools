"""
Prerequisite:
- In order to use moviepy, the library must be installed beforehand.
  It can be installed using pip with the following command: pip install moviepy
  `pip install moviepy`
  
- Some systems may also require ffmpeg to be installed or added to the path.
  moviepy uses ffmpeg as a backend to convert videos, etc.

Instructions for use:
When executing this script, specify the GIF filename as an argument.
Example: `python script_name.py example.gif`

If not specified, all GIF files in the same directory will be converted to MP4.
"""
import sys
import os
from moviepy.editor import *

def convert_gif_to_mp4(gif_path):
    clip = VideoFileClip(gif_path)
    mp4_path = gif_path.rsplit('.', 1)[0] + '.mp4'  # Remove the extension from the gif filename and add .mp4
    clip.write_videofile(mp4_path, fps=clip.fps)

if __name__ == "__main__":
    gifs_to_convert = []

    if len(sys.argv) > 1:
        gifs_to_convert.append(sys.argv[1])
    else:
        for filename in os.listdir():
            if filename.endswith('.gif'):
                gifs_to_convert.append(filename)

    for gif_file in gifs_to_convert:
        convert_gif_to_mp4(gif_file)
