from tkinter import *
from utils import *

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


def button_click():
    if variable.get() == "ATL":
        variable1 = StringVar(root)
        variable1.set("Pick a Player")  # default value
        playersATL = OptionMenu(root, variable1, "DeAndre' Bembry", "Charles Brown Jr.")
        playersATL.pack()


button = Button(root, text="OK", command=button_click)
button.pack()

mainloop()
