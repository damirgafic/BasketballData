# Read from file and create class to hold player information

class Player:
    league = 'NBA'

    def __init__(self, fName, lastName, salary, per):
        self.fName = fName
        self.lastName = lastName
        self.salary = salary
        self.per = per
