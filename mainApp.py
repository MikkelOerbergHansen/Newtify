from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from custom_functions.Misc import *
from flask_login import LoginManager
from flask_login import UserMixin, login_user, logout_user, current_user, login_required

# Assuming these directories exist under your static directory
MUSIC_FOLDER = os.path.join('static', 'music')
COVER_FOLDER = os.path.join('static', 'img')





app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music_player.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "abc"
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)



class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True,
                         nullable=False)
    password = db.Column(db.String(250),
                         nullable=False)


@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)




class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    cover = db.Column(db.String(255), nullable=False)




### Note to mikkel: Add all class according to E/R diagram





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
        









@app.route('/test', methods=['GET','POST'])
def landingpage():
    
    
    return render_template('landingpage.html')


@app.route('/DEMO', methods=['GET','POST'])
def DEMO():
    songs = Song.query.all()
    print(songs[1])
    # Convert song objects to a list of dictionaries to pass to the frontend
    songs_data = [{"name": song.name, "path": song.path, "artist": song.artist, "cover": song.cover} for song in songs]
    
    return render_template('DEMOpage.html', songs=songs_data)





@app.route('/loginPage', methods=['GET','POST'])
def loginPage():
    if request.method == 'POST':
            username = request.form["username"]
            password = request.form["password"]
            remember = request.form.get("remember")

            user = Users.query.filter_by(username=request.form.get("username")).first()

            if not user or user.password != password:
                error_message ="check your input"
                return render_template('loginPage.html', errormessage = error_message)
        

            login_user(user)

########################################## vi prøver python login manager
##
## https://www.geeksforgeeks.org/how-to-add-authentication-to-your-app-with-flask-login/
##
## https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
##


            return redirect('/profile')
            
    
    
    return render_template('loginPage.html')




@app.route('/signupPage', methods=['GET','POST'])
def signupPage():
    if request.method == 'POST':
            username = request.form["username"]
            password = request.form["password"]
            print(username)
            print(password)
            ### right now the username has to be unique
            user = Users.query.filter_by(username=username).first()
            if user: # if a user is found, we want to redirect back to signup page so user can try again
                error_message ="this user already exist"
                print("test")
                return render_template('signupPage.html', errormessage = error_message)

            # Add entry to the database
            new_user = Users(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()

            user = Users.query.filter_by(username=request.form.get("username")).first()
            login_user(user)

            return redirect("/profile")
    
    return render_template('signupPage.html')





@app.route('/FAQpage', methods=['GET','POST'])
def FAQpage():
    
    
    return render_template('FAQpage.html')



@app.route('/ABOUTpage', methods=['GET','POST'])
def ABOUTpage():
    
    
    return render_template('ABOUTpage.html')



@app.route('/Mission', methods=['GET','POST'])
def Mission():
    
    
    return render_template('Mission.html')




@app.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    
    return render_template('profile.html', name=current_user.username)




@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('logout.html')









@app.route('/newpage', methods=['GET','POST'])
def newpage():
    
    
    return render_template('newpage.html')




if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This line creates all the tables based on the models defined
        add_songs()  # This line checks and adds the songs to the database
    app.run(debug=True)
