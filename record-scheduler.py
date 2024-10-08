import os
import json
import ffmpeg
from watchdog.observers import Observer
import logging

# Static definitions
# STREAM_URL = 'http://localhost:8880/stream'
STREAM_URL = 'https://wlmc.landmark.edu:8880/stream'
SAVE_PATH = ''

# Function to generate filenames based on host's name
def generate_filename(host_first_name, host_last_name, timestamp):
    filename = f"{host_first_name}_{host_last_name}_{timestamp.strftime('%m_%d_%Y')}_RAWDATA.mp3"
    full_path = os.path.join(SAVE_PATH, filename)
    return full_path

# Function to record the stream
def record_stream(duration, output_file):
    try:
        logging.info(f"Starting recording: {output_file}")
        (
            ffmpeg
            .input(STREAM_URL, t=duration)
            .output(output_file, acodec='copy')
            .overwrite_output()
            .run()
        )
        logging.info(f"Recording saved as {output_file}")
    except ffmpeg.Error as e:
        logging.error(f"An error occurred: {e.stderr.decode()}")

# Load schedules from JSON
def load_schedules():
    with open('schedule.json', 'r') as f:
        return json.load(f)

