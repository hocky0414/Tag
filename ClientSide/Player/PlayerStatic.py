import random
pVel=20
pWid=25
pHeight=25
FOV=300
def getVel():
    return pVel
def getWid():
    return pWid
def getHeight():
    return pHeight
def getFOV():
    return FOV
def getColor():
    red= random.randint(0,255)
    blue=random.randint(0,255)
    green=random.randint(0,255)
    return (red,green,blue)