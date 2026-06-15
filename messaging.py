import socket
import threading

HOST = "10.17.31.13"  # The server's hostname or IP address
PORT = 65435  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '10.17.31.13'
    port = 65435
    client_socket.connect((host, port))

    while True:
        message = input("Enter your message: ")
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print(f"Server response: {response}")

if __name__ == "__main__":
    main()