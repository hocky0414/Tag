from _thread import *
import Player.PlayerObj as player
import PlayerStatic
import MapObj.map as Map
import Status
import socket

import pickle

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
    return

def make_pos(player):
    #the position need to send to opposite player

    if player == 0:
       return players[0]
    elif player == 1:
        return players[1]

def threaded_client(conn,player):
    #First of first, we need to send initial position to current player
    #conn.sendall(str.encdoe("Player"+str(player)+"is connected"))

    caught = False
    temp = {}
    while not caught:
        try:
            data = pickle.loads(conn.recv(2048))
            if type(data)==type(player_thief):
                # The server need to respond opposite player's opposite player's position
                players[player] = data
                oppositePos = None
                if player == 0:
                    oppositePos = make_pos(1)
                elif player == 1:
                    oppositePos = make_pos(0)
                conn.sendall(pickle.dumps(oppositePos))
            elif type(data)==type(""):
                if "status" in data:
                    conn.sendall(pickle.dumps(status.getStates()))
                elif "&" in data:
                    for ele in data.split("&"):
                        (k,v) = ele.split("=")
                        temp[k]=v
                    if "thief" in temp['character']:
                        role=1
                    else:
                        role=0
                    if "True" in temp['ready'] and not readyPlayer[role] :
                        readyPlayer[role]=True
                        conn.sendall(pickle.dumps("ok"))
                    elif "True" in temp['ready'] and readyPlayer[role]:
                        conn.sendall(pickle.dumps("taken"))
                    elif "False" in temp['ready']:
                        readyPlayer[role]=False
                        conn.sendall(pickle.dumps("ok"))
                elif "init" in data:
                    if "thief" in temp['character']:
                        #print(make_pos(1))
                        conn.sendall(pickle.dumps(make_pos(1)))
                    elif 'cap' in temp['character']:
                       # print(make_pos(0))
                        conn.sendall(pickle.dumps(make_pos(0)))
            start=True
            for i in readyPlayer:
                if not i:
                    start=False
                    break
            if start:
                status.setIngame()
            print(temp)
        except:
            break
    player -=1
    conn.close()
    print("Disconnected")
host = ''
port=10086

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host,port))
serversocket.listen(2)
maxPlayer=2
currentPlayer = 0
status= Status.gameStatus()
readyPlayer= [False,False]
playerInfo = {}
initialList(playerInfo)
map = Map.Map(1000, 1000)
player_thief= player.PlayerObj(int(playerInfo['thief']['posX']), (playerInfo['thief']['posY']), PlayerStatic.getWid(), PlayerStatic.getHeight(), (255, 0, 0), map.block(), map)
player_police= player.PlayerObj(int(playerInfo['cap']['posX']),(playerInfo['cap']['posY']),PlayerStatic.getWid(),PlayerStatic.getHeight(),(0,255,0),map.block(),map)

players=[player_thief,player_police]

while True:
    conn, addr=serversocket.accept()
    print("Now connected to this address", addr)
    start_new_thread(threaded_client,(conn,currentPlayer))

    print("This is player"+str(currentPlayer))
    currentPlayer +=1

