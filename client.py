import socketio
import os
import subprocess
sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')
    list_files = os.listdir("D:\\New Folder\\captures")
    sio.emit('files',{"files":list_files})

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.event
def command(data):
    print('Received command:', data['command'])
    sio.emit("client_message",{"data":"Received"})
@sio.event
def analyse_file(data):
    command = f"{data['command']} -f /dataset/attack-captures/{data['file']}"
    res = subprocess.run(command)
    print(res)


if __name__ == '__main__':
    sio.connect('http://localhost:5000') #Replace localhost with IP
    sio.wait()
