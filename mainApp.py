from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # This route will simply render the HTML template for the music player.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
