import socket
import pickle

class clientNet():
    def __init__(self) -> None:
        self.host = '192.168.18.58'
        self.port=9090
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host,self.port))
        return pickle.loads(self.socket.recv(2048))

    def send(self,obj):
        self.socket.send(pickle.dumps(obj))
        return pickle.loads(self.socket.recv(2048))

        





