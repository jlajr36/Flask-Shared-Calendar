from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KET'] = 'secretkey'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')