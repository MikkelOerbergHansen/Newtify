from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename

# Assuming these directories exist under your static directory
MUSIC_FOLDER = os.path.join('static', 'music')
COVER_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music_player.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    cover = db.Column(db.String(255), nullable=False)

def add_songs():
    # Checking if there are any songs in the database
    if Song.query.count() == 0:
        # List of songs to add
        songs = [
            Song(name="Debt Crush", path="static/music/Mother of All - Debt Crush.mp3", artist="Mother of All", cover="static/img/moa.jpg"),
            Song(name="Som Aldrig Før", path="static/music/Nymaane - Som Aldrig Foer.mp3", artist="Nymaane", cover="static/img/album-cover-logo.jpg")
        ]
        db.session.bulk_save_objects(songs)
        db.session.commit()

@app.route('/')
def index():
    songs = Song.query.all()
    print(songs[1])
    # Convert song objects to a list of dictionaries to pass to the frontend
    songs_data = [{"name": song.name, "path": song.path, "artist": song.artist, "cover": song.cover} for song in songs]
    return render_template('index.html', songs=songs_data)

@app.route('/upload', methods=['GET','POST'])
def upload():
        if request.method == 'POST':
            name = request.form['name']
            artist = request.form['artist']
            cover = request.files['cover']
            song = request.files['song']

            # Create secure filenames and save the files
            cover_filename = secure_filename(cover.filename)
            song_filename = secure_filename(song.filename)
            cover.save(os.path.join(COVER_FOLDER, cover_filename))
            song.save(os.path.join(MUSIC_FOLDER, song_filename))

            # Add entry to the database
            new_song = Song(name=name, path=os.path.join(MUSIC_FOLDER, song_filename), artist=artist, cover=os.path.join(COVER_FOLDER, cover_filename))
            db.session.add(new_song)
            db.session.commit()

            # Redirect back to the main page or return a success message
            return redirect(url_for('index'))
        else:
             return render_template('upload.html')
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This line creates all the tables based on the models defined
        add_songs()  # This line checks and adds the songs to the database
    app.run(debug=True)
