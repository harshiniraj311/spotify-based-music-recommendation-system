from flask import Flask, render_template, request
from main import playlist_model, playlist_analysis  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        playlist_id = request.form['playlist_id']
        if 'get_recommendations' in request.form:
            num_songs = int(request.form['num_songs'])
            if num_songs > 0:
                model = "Spotify Model"
                result, logs = playlist_model(playlist_id, model, num_songs)
                return render_template('index.html', result=result.iterrows(), logs=logs, analysis=None)
        elif 'playlist_analysis' in request.form:
            tracks, logs = playlist_analysis(playlist_id)
            return render_template('index.html', result=None, logs=logs, analysis=tracks)
    return render_template('index.html', result=None, logs=None, analysis=None)

if __name__ == '__main__':
    app.run(debug=True)
