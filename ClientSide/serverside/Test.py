import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 10086))

strings = "posX=80&posY=90&Counter=0"
s.sendall(str.encode(strings))
while True:
    data = s.recv(2048)
    print('Received:')
    print("================================")
    print(data.decode("utf-8") )
    print("================================")

s.close()