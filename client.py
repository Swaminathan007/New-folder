import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server') 

@sio.event
def command(data):
    print('Received command:', data['command'])
    sio.emit('client_message', {'message': f"Command received: {data['command']}"})

if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    sio.wait()
