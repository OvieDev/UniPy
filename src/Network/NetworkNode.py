import socket


class NetworkNode:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def host_website(self):
        HOSTNAME = "localhost"
        PORT = 60055
        with self.server as server:
            server.bind((HOSTNAME, PORT))
            server.listen()
            conn, addr = server.accept()
            with conn:
                while True:
                    conn.sendall("oh boi here we go again".encode())
                    break


    def connect(self):
        self.client.connect(("localhost", 60055))
        data = self.client.recv(1024)
        print(data)

