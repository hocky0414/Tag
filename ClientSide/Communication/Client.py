#Lamport timeStamp
#Local events and message sending cause counter++
#message receiving  counter= MAX(message_receving_counter,counter)++
from Communication.LamportCounter import *
class communication_client:
    def __init__(self):
        self.lamport= lamportTime()
    def Send(self,str):
        str+="&Counter="+self.lamport.getCounter()
        self.lamport.incrementCounter()
        return
    def receive(self,str):
        reve_counter=str.split("&")[2]
        counter=int(reve_counter.split("=")[1])
        max= max(self.lamport,counter)
        self.lamport.setCounter(max)
        self.lamport.incrementCounter()
        return

