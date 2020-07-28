class lamportTime:
    def __init__(self):
        self.lamport_counter=0
    def getCounter(self):
        return self.lamport_counter
    def incrementCounter(self):
        self.lamport_counter+=1;
        return
    def setCounter(self,value):
        self.lamport_counter=value
        return
