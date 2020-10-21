from tkinter import *
from utils import *

from Model.utils import get_team_roster, teamArray

root = Tk()

variable = StringVar(root)
variable.set("Pick a Team")  # default value



teams = OptionMenu(*(root, variable) + tuple(teamArray))
teams.pack()

variable2 = StringVar(root)
variable2.set('Pick a Team')
teams2 = OptionMenu(*(root, variable2) + tuple(teamArray))
teams2.pack()


def ok():
    print("value is: " + variable.get())


def button_click():  # Manually inputting just to test
    print(variable.get())
    players = get_team_roster(variable.get())
    variableB = StringVar(root)
    variableB.set("Pick a Player")  # default value
    # playersATL = OptionMenu(root, variableB, *players, command=print_it())
    playersMenu = OptionMenu(*(root, variableB) + tuple(players))
    playersMenu.pack()


def button_click2():  # Manually inputting just to test
    players = get_team_roster(variable2.get())
    variableB = StringVar(root)
    variableB.set("Pick a Player")  # default value
    playersMenu = OptionMenu(*(root, variableB) + tuple(players))
    playersMenu.pack()


button = Button(root, text="OK", command=button_click)
button.pack()
button2 = Button(root, text="ok 2", command=button_click2)
button2.pack()
mainloop()
