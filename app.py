from flask import *
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

clients = []

@app.route('/',methods=["GET","POST"])
def index():
    if(request.method == "POST"):
        if(len(clients) == 1):
            command = request.form['command']
            socketio.emit('command', {'command': command})
            flash("Message sent to client")
        else:
            flash("No clients connected")
    return render_template('index.html')



@socketio.on('connect')
def handle_connect():
    if(len(clients) == 1):
        flash("Client connected")
        return
    clients.append(request.sid)
    print(f'Client connected: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect():
    clients.remove(request.sid)
    print(f'Client disconnected: {request.sid}')

@socketio.on('client_message')
def handle_client_message(data):
    print(f'Received message from client: {data["message"]}')

if __name__ == '__main__':
    socketio.run(app, debug=True,host="0.0.0.0")
