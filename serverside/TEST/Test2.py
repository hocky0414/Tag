import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 10086))

strings = "GET"
s.sendall(str.encode(strings))
while True:
    data = s.recv(2048)
    print('Received:')
    print("================================")
    print(data.decode("utf-8") )
    print("================================")

s.close()