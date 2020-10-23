from operator import itemgetter

from Model.Players import Player


def readFromFileToClass():
    f = open("BasketballData2020.txt", "r+")
    players = f.read().splitlines()
    split = players[3].split(' ')
    pObjects = []
    for i in range(len(players)):
        split = players[i].split()
        try:
            pObjects.append(Player(split[0], split[1], split[2], float(split[3]),
                                   float(split[3]) / float(split[2].replace('$', '').replace(',', ''))))
        except (ValueError, ZeroDivisionError):
            pObjects.append(Player(split[0], split[1], split[2], float(split[3]), float(split[3]) / 1))

    sortedObjects = sorted(pObjects, key=lambda x: x.per)
    # for i in range(len(sortedObjects)):
    # print(sortedObjects[i].fName + ' ' + str(sortedObjects[i].per))
    return sortedObjects


def findBest(players, value, greaterThan, salary):  # greaterThan: bool decides whether we will look
    # for players above the salary or less than the salary
    # value is bool, if true find the best per/salary, if false find the worst per/salary
    sorted(players, key=lambda x: x.salary)

    players = sorted(players, key=lambda x: x.perSalaryRatio)
    for i in range(len(players)):
        if players[i].salary != 'NoContract':  # to avoid players with no contract that have inflated ratio
            if int(players[i].salary.replace('$', '').replace(',','')) > salary and greaterThan:  # find greatest per/salary ratio:
                print(players[i].fName + ' ' + players[i].lastName + ' ')
                print(round(players[i].perSalaryRatio * 100000000, 3))
            elif int(players[i].salary.replace('$', '').replace(',', '')) < salary and not greaterThan:
                print(players[i].fName + ' ' + players[i].lastName + ' ')
                print(round(players[i].perSalaryRatio * 100000000, 3))

            # multiplying ratio here to make it a nice looking number
        else:
            pass


players = readFromFileToClass()
findBest(players, True, True, 20000000)
