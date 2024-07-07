import subprocess
import os

# Replace with your Twitch stream key
STREAM_KEY = 'live_776153896_BJgmYvCEa3ARuy7CSjdmwNj3rGamZ1'

# Get the absolute path to the video file
input_file = os.path.expanduser('~/TP3/TP3-main/cozylofi/lofi.webm')

# FFmpeg command with looping
command = [
    'ffmpeg',
    '-re',  # Read input at native frame rate
    '-stream_loop', '-1',  # Loop the input file indefinitely
    '-i', input_file,  # Input file
    '-c:v', 'libx264', '-preset', 'veryfast', '-maxrate', '3000k',
    '-bufsize', '6000k', '-pix_fmt', 'yuv420p', '-g', '60',
    '-c:a', 'aac', '-b:a', '160k',  # Audio settings
    '-f', 'flv', f'rtmp://live.twitch.tv/app/{STREAM_KEY}'
]

# Execute FFmpeg command
subprocess.run(command)
