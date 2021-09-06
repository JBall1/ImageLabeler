from tkinter import *
from tkinter import filedialog
import ctypes, os

folder_selected = "~/"

def callback():
    active.set(False)
    quitButton.destroy()
    JustGo = Button(root, text="Select Image Directory", command= lambda: KeepGoing())
    JustGo.pack()   
    JustGo.place(x=150, y=110)
    #root.destroy()         # Uncomment this to close the window



def KeepGoing():
    folder_selected = filedialog.askdirectory()

root = Tk()
root.geometry("400x268")
root.title("LabelMe")
root.configure(background='light blue')

root.resizable(False, False)


timeLeft = IntVar()
timeLeft.set(10)            # Time in seconds until shutdown

active = BooleanVar()
active.set(True)            # Something to show us that countdown is still going.


quitButton = Button(root, text="Select Image Directory", command=KeepGoing)
quitButton.pack()   
quitButton.place(x=150, y=150)


root.mainloop()  