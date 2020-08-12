from _thread import *
import Player.PlayerObj as player
import PlayerStatic
import MapObj.map as Map
import Status
import socket
import time
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
    list['thief']['Counter'] = 0
    return


def make_pos(player):
    # the position need to send to opposite player

    if player == 0:
        return players[0]
    elif player == 1:
        return players[1]


def threaded_client(conn):
    recordTime = True
    gamelength = 10
    caught = False
    role = -1
    startTime = time.time()
    start = False
    ends = False
    temp = {}
    status = Status.gameStatus()
    while not caught:
        try:
            data = pickle.loads(conn.recv(2048))
            if type(data) == type(player_thief):
                # The server need to respond opposite player's opposite player's position
                if role != -1:
                    players[role] = data
                    oppositePos = None
                    if role == 0:
                        oppositePos = make_pos(1)
                    elif role == 1:
                        oppositePos = make_pos(0)
                    conn.sendall(pickle.dumps(oppositePos))
                else:
                    print("Not in game yet")
            elif type(data) == type(""):
                if "status" in data:
                    conn.sendall(pickle.dumps(status.getStates()))
                elif "&" in data:
                    for ele in data.split("&"):
                        (k, v) = ele.split("=")
                        temp[k] = v
                        print(v)
                    if "thief" in temp['character']:
                        role = 0
                    else:
                        role = 1
                    if "True" in temp['ready'] and not readyPlayer[role]:
                        readyPlayer[role] = True
                        conn.sendall(pickle.dumps("ok"))
                    elif "True" in temp['ready'] and readyPlayer[role]:
                        conn.sendall(pickle.dumps("taken"))
                    elif "False" in temp['ready']:
                        readyPlayer[role] = False
                        conn.sendall(pickle.dumps("ok"))
                elif "init" in data:
                    if "thief" in temp['character']:
                        conn.sendall(pickle.dumps(make_pos(0)))
                        print("Theif:" + str(make_pos(0).getPosition()))

                    elif 'cap' in temp['character']:
                        conn.sendall(pickle.dumps(make_pos(1)))
                        print("Police:" + str(make_pos(1).getPosition()))
            if False in readyPlayer:
                start = False
            else:
                start = True
            if start and (not ends):
                status.setIngame()
                if recordTime:
                    startTime = time.time()  # record start time
                    recordTime = False
            currentTime = time.time()
            policePos = players[1].getPosition()
            thiefPos = players[0].getPosition()
            if (currentTime - startTime) < gamelength and start and not ends:
                if (abs(policePos[0] - thiefPos[0]) < PlayerStatic.getWid()) and (
                        abs(policePos[1] - thiefPos[1]) < PlayerStatic.getHeight()):  # caught
                    ends = True
                    if role == 0:
                        status.setLose()
                    if role == 1:
                        status.setWin()
            elif (currentTime - startTime) >= gamelength and start and not ends:
                print("Out of time")
                ends = True
                if role == 0:
                    print("Thief wins")
                    status.setWin()
                if role == 1:
                    print("Police lose")
                    status.setLose()
        except:
            break
    conn.close()
    print("Disconnected")


host = ''
port = 10086

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(20)
maxPlayer = 2
currentPlayer = 0

readyPlayer = [False, False]
playerInfo = {}
initialList(playerInfo)
map = Map.Map(1000, 1000)
player_thief = player.PlayerObj(10, 10, PlayerStatic.getWid(), PlayerStatic.getHeight(), (255, 0, 0), map.block(), map)
player_police = player.PlayerObj(500, 500, PlayerStatic.getWid(), PlayerStatic.getHeight(), (0, 255, 0), map.block(),
                                 map)
players = [player_thief, player_police]
while True:
    conn, addr = serversocket.accept()
    print("Now connected to this address", addr)
    start_new_thread(threaded_client, (conn,))

    print("This is player" + str(currentPlayer))
    currentPlayer += 1
