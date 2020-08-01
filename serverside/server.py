from _thread import *
from Player import PlayerObj
import socket
import sys
import pickle
host = "LOCALHOST"
port=10086
playerInfo = {}
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host,port))
serversocket.listen(2)
currentPlayer = 0
print("Server is started, waitting for hearing from clients:")
def initialList(list):
    list['cap'] = {}
    list['thief'] = {}
    list['cap']['posX'] = 10
    list['cap']['posY'] = 10
    list['cap']['Counter'] = 0
    list['thief']['posX'] = 500
    list['thief']['posY'] = 500
    list['thief']['Counter']=0
def make_pos(player,list):
    #the position need to send to opposite player
    strings = ""
    if player == 0:
        strings = "posX="+str(list['cap']['posX'])+"&posY="+str(list['cap']['posY'])+"&Counter="+str(list['cap']['Counter'])
    elif player == 1:
        strings = "posX="+str(list['thief']['posX'])+"&posY="+str(list['thief']['posY'])+"&Counter="+str(list['thief']['Counter'])
    return strings
def read_pos(player,data):
    #this is update player's position on server
    if player == 0:
        for info in data.split('&'):
            (key,value) = info.split('=')
            playerInfo['cap'][key]=value
    elif player == 1:
        for info in data.split('&'):
            (key,value) = info.split('=')
            playerInfo['thief'][key]=value

    return
def threaded_client(conn,player):
    #First of first, we need to send initial position to current player
    #conn.sendall(str.encdoe("Player"+str(player)+"is connected"))
    conn.send(pickle.dumps(make_pos(player,playerInfo)))
    caught = False
    while not caught:
        try:
            data = conn.recv(2048).decode('utf-8')
            if 'GET' in data:
                # The server need to respond opposite player's opposite player's position
                oppositePos = ""
                if player == 0:
                    oppositePos = make_pos(1, playerInfo)
                elif player == 1:
                    oppositePos = make_pos(0, playerInfo)
                conn.sendall(str.encode(oppositePos))
            else:
                # Server do not need to respond any information, just update current player's position
                read_pos(player, data)
                print(data)
        except:
            break
    player -=1
    conn.close()
    print("Disconnected")
initialList(playerInfo)
print(playerInfo)
while True:
    conn, addr=serversocket.accept()
    print("Now connected to this address", addr)
    start_new_thread(threaded_client,(conn,currentPlayer))
    print("This is player"+str(currentPlayer))
    currentPlayer +=1

