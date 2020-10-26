'''
Things to be done:
-scrape all salaries and PER stats

'''
import tkinter as tk
from PIL import Image, ImageTk

from Model.basketballData import findBest, players

'''
window = tk.Tk()
image = Image.open('nba.png')
photo_image = ImageTk.PhotoImage(image)
label = tk.Label(window, image = photo_image)
label.pack()

mainloop()
'''

from tkinter import *


def checkStatus():
    print(checkVar1.get())


root = Tk()
checkVar1 = BooleanVar()
checkBut1 = Checkbutton(root, text='Best', variable=checkVar1, onvalue=True, offvalue=False, command=checkStatus)
checkBut1.pack()

root.mainloop()
