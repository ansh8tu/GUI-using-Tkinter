from tkinter import *

root = Tk()

def onPressed():
    myLabel = Label(root, text="Yay! Tickets booked, Looking forward to see you! ", fg ='red')
    myLabel.pack()

myFirstButton = Button(root, text = "Press here to book Tickets", padx="30", pady="20", fg = "white", bg = 'black', command = onPressed)
myFirstButton.pack()

root.mainloop()