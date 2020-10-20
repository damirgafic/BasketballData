from tkinter import *
from utils import *

from Model.utils import get_team_roster

root = Tk()

variable = StringVar(root)
variable.set("Pick a Team")  # default value

teams = OptionMenu(root, variable, "ATL", "BKN", "BOS", "CHA", "CHI", "CLE", "DAL",
                   "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA",
                   "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHX", "POR",
                   "SAC", "SAS", "TOR", "UTA", "WAS")
teams.pack()


def ok():
    print("value is: " + variable.get())


def print_it(event):
    print(var.get())


def button_click():  # Manually inputting just to test
    players = get_team_roster(variable.get())
    variable1 = StringVar(root)
    variable1.set("Pick a Player")  # default value
    # playersATL = OptionMenu(root, variable1, *players, command=print_it())
    playersMenu = OptionMenu(*(root, variable1) + tuple(players))
    playersMenu.pack()


button = Button(root, text="OK", command=button_click)
button.pack()

mainloop()
