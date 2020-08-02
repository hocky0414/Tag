#Lamport timeStamp
#Local events and message sending cause counter++
#message receiving  counter= MAX(message_receving_counter,counter)++
from Communication.LamportCounter import *
import socket
import pickle
class communication_client:
    def __init__(self):
        self.lamport= lamportTime()
        self.port=10086
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Socket.connect(('LOCALHOST', self.port))
        self.player= pickle.loads(self.Socket.recv(2048))
    def send(self,player):
        self.Socket.sendall(pickle.dumps(player))
        self.lamport.incrementCounter()
        return pickle.loads(self.Socket.recv(2048))

