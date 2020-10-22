from Model.Players import Player


class Node:

    def __init__(self, data, name):

        self.left = None
        self.right = None
        self.data = data #per
        self.name = name

    def insert(self, data, name):
        if self:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, name)
                else:
                    self.left.insert(data, name)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, name)
                else:
                    self.right.insert(data, name)
           # elif data == self.data:
           #     if self.left is None:
            #        self.left = Node(data, name)
        else:
            self.data = data
            self.name = name

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(str(self.data) + ' ' + self.name),
        if self.right:
            self.right.PrintTree()


def transferFromFileToClass():
    f = open("BasketballData2020.txt", "r+")
    players = f.read().splitlines()
    split = players[3].split(' ')
    pObjects = []
    tree = Node(-100, 'na')
    tree.PrintTree()
    for i in range(len(players)):
        split = players[i].split()
        pObjects.append(Player(split[0], split[1], split[2], float(split[3])))
        #print(pObjects[i].fName + ' ' + pObjects[i].lastName + ' ' + pObjects[i].salary)


        try:
            pObjects[i].salary = int(pObjects[i].salary.replace('$', '').replace(',', ''))
            tree.insert(pObjects[i].per/pObjects[i].salary, pObjects[i].fName+' '+pObjects[i].lastName)
        except (ZeroDivisionError, ValueError):
            tree.insert(50/-1, pObjects[i].fName+' '+pObjects[i].lastName)


    tree.PrintTree()

transferFromFileToClass()
