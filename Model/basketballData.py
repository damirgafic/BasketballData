from operator import itemgetter
from Model.Players import Player

def transferFromFileToClass():
    f = open("BasketballData2020.txt", "r+")
    players = f.read().splitlines()
    split = players[3].split(' ')
    pObjects = []
    for i in range(len(players)):
        split = players[i].split()
        pObjects.append(Player(split[0], split[1], split[2], float(split[3])))
    sortedObjects = sorted(pObjects, key=lambda x: x.per)
    for i in range(len(sortedObjects)):
        print(sortedObjects[i].fName + ' ' + str(sortedObjects[i].per))
transferFromFileToClass()
