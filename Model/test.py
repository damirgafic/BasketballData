from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as ttk
from tkinter import ttk
import tkinter.ttk as ttk


class TestGUI(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.pack()

        self.mylist = ['test','test2','test3']
        variable = StringVar()
        variable.set(self.mylist[0]) # default value
        self.w = OptionMenu(*(root, variable) + tuple(self.mylist))
        self.w.pack()



root = Tk()
gui = TestGUI(root)
root.mainloop()