#Lamport timeStamp
#Local events and message sending cause counter++
#message receiving  counter= MAX(message_receving_counter,counter)++
from Communication.LamportCounter import *
import socket
class communication_client:
    def __init__(self):
        self.lamport= lamportTime()
        self.port=10086
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self,str):
        try:
            self.socket.connect(('', self.port))
            str+="&Counter="+self.lamport.getCounter()
            self.socket.sendall(str.encode())
            self.lamport.incrementCounter()
            print("Sent:"+str)
            self.socket.close()
        except:
            print("Failed to send message")
        return
    def receive(self):
        sendMessage="GET"
        self.socket.connect(('', self.port))
        self.socket.sendall(sendMessage.encode())
        reve_counter=self.socket.recv(2048).decode()[2]
        counter=int(reve_counter.split("=")[1])
        maxValue= max(self.lamport.getCounter(),counter)
        self.lamport.setCounter(maxValue)
        self.lamport.incrementCounter()
        return reve_counter

