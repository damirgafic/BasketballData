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
    # print(findBest(players, True, True, int(e.get())))
    try:
        num = int(e.get().replace('$', '').replace(',', ''))
        if num < 51000:  # no players return if value is under 51,000
            num = 51000
        if num > 41000000:
            num = 40000000  # no players return if value is over 41,000,000
        if checkVar1.get() and checkVar2.get():
            Label(center_frame, text=findBest(players, True, True, num)).pack()
        elif checkVar1.get() and not checkVar2.get():
            Label(center_frame, text=findBest(players, True, False, num)).pack()
        elif not checkVar1.get() and checkVar2.get():
            Label(center_frame, text=findBest(players, False, True, num)).pack()
        else:
            Label(center_frame, text=findBest(players, False, False, num)).pack()
    except ValueError:
        newWindow = Tk()
        newWindow.title('ValueError')
        Label(newWindow, text='Enter a Valid Number. Example: $25,632,400', bg='red').pack()


root = Tk()
root.title("efficiency ratings based on contracts of players from 2019-2020 NBA season")
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

logo = Image.open('nbaLogo.png')
logoPhoto = ImageTk.PhotoImage(logo)

Label(center_frame, image=logoPhoto).pack()

Label(center_frame, text='Enter a minimum/maximum salary cap in dollars', width=40).pack()
e = Entry(center_frame, width=20)
e.pack()

checkVar1 = BooleanVar()
checkBut1 = Checkbutton(center_frame, text='Best PER/Salary ratio', variable=checkVar1, onvalue=True, offvalue=False)
checkBut1.pack()

checkVar2 = BooleanVar()
checkBut2 = Checkbutton(center_frame, text="Greater than Salary Cap", variable=checkVar2, onvalue=True, offvalue=False)
checkBut2.pack()

Button(center_frame, width=20, text='Enter', command=showStat).pack()

root.mainloop()
