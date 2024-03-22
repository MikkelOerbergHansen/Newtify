####
#
# Our main application
#
###
from flask import Flask, render_template, jsonify, request
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Load the music file
song_path = 'static/Nymaane - Som Aldrig Foer.mp3'  # Replace this with the path to your music file
pygame.mixer.music.load(song_path)

app = Flask(__name__)

# Global variables to track play status, start time, and song duration
is_playing = False
start_time = None
song_duration = 240  # Duration in seconds, replace with your song's duration

@app.route('/')
def index():
    # The index.html should have a button that when clicked, sends a request to '/play-music'
    return render_template('index.html')

@app.route('/toggle-music', methods=['GET'])
def toggle_music():
    global is_playing, start_time
    if is_playing:
        pygame.mixer.music.stop()
        is_playing = False
        start_time = None
        return jsonify({'status': 'stopped'}), 200
    else:
        pygame.mixer.music.play()
        is_playing = True
        start_time = time.time()
        return jsonify({'status': 'playing'}), 200

@app.route('/get-progress', methods=['GET'])
def get_progress():
    global song_duration
    if is_playing and start_time:
        elapsed_time = time.time() - start_time
        progress = elapsed_time / song_duration * 100  # Progress as a percentage
        return jsonify({'progress': progress, 'is_playing': is_playing}), 200
    else:
        return jsonify({'progress': 0, 'is_playing': is_playing}), 200

@app.route('/deep-dive')
def deep_dive():
    return render_template('deep-dive.html')

if __name__ == '__main__':
    app.run(debug=True)