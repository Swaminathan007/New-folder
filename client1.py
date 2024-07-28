import socket
import threading

def listen_for_commands(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

if __name__ == "__main__":
    client_id = 'client_02'
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    client_socket.sendall(client_id.encode())

    threading.Thread(target=listen_for_commands, args=(client_socket,)).start()

    while True:
        pass  # Keep the main thread alive
