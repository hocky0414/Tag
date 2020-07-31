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
        self.pos= pickle.loads(self.Socket.recv(2048))
    def send(self,string):

        string+="&Counter="+str(self.lamport.getCounter())
        self.Socket.sendall(string.encode())
        self.lamport.incrementCounter()
        print("Sent:"+string)

        return
    def receive(self):
        try:
            sendMessage="GET"
            self.Socket.sendall(sendMessage.encode())

            data=self.Socket.recv(2048).decode("utf-8")
            counter=int(data.split("&")[2].split("=")[1])
            maxValue= max(self.lamport.getCounter(),counter)
            self.lamport.setCounter(maxValue)
            self.lamport.incrementCounter()
            return data
        except socket.error as e:
            print(e)
            return ""
    def getPos(self):
        return str(self.pos)

