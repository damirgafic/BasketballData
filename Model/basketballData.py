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
    sortRatings = []
    for i in range(len(players)):
        if players[i].salary != 'NoContract':  # to avoid players with no contract that have inflated ratio
            if int(players[i].salary.replace('$', '').replace(',','')) > salary and greaterThan:  # find greatest per/salary ratio:
                print(players[i].fName + ' ' + players[i].lastName + ' ')
                print(round(players[i].perSalaryRatio * 100000000, 3))
                sortRatings.append(players[i])
            elif int(players[i].salary.replace('$', '').replace(',', '')) < salary and not greaterThan:
                print(players[i].fName + ' ' + players[i].lastName + ' ')
                print(round(players[i].perSalaryRatio * 100000000, 3))
                sortRatings.append(players[i])

            # multiplying ratio here to make it a nice looking number
        else:
            pass
    max = len(sortRatings)-1
    if value:
        return 'The best PER-Salary ratio belongs to ' + sortRatings[max].fName + ' ' + sortRatings[max].lastName
    else:
        return 'The worst PER-Salary ratio belongs to ' + sortRatings[0].fName + ' ' + sortRatings[0].lastName

players = readFromFileToClass()
print(findBest(players, True, True, 20000000))
