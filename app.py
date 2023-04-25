from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# createing a new falsk app and socketIO instance

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is secret key"
socketio = SocketIO(app)

# define a route for the homepage

@app.route('/')
def index():
    return render_template('index.html')

# define a route for the chat messages

@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

# run the flask app

if __name__ == '__main__':
    socketio.run(app, port=8080)
