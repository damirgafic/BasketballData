from tkinter import *
from PIL import Image, ImageTk

from Model.basketballData import findBest, players


def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

def showStat():
    #print(findBest(players, True, True, int(e.get())))
   num = int(e.get())
   l = Label(center_frame, text=findBest(players, True, True, num)).pack()

root = Tk()
root.title("Title")
root.geometry('600x600')

frame = Frame(root, relief='raised', borderwidth=2)
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)

copy_of_image = Image.open("nba.png")
photo = ImageTk.PhotoImage(copy_of_image)

label = Label(frame, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

center_frame = Frame(frame, relief='raised', borderwidth=2)
center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(center_frame, text='Enter a minimum salary cap in dollars', width=30).pack()
e = Entry(center_frame, width=20)

e.pack()

Button(center_frame, width=20, text='Enter', command=showStat).pack()


root.mainloop()