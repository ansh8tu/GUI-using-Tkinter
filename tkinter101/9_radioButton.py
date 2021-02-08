from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("The Saturday Night Pizza")
root.iconbitmap("allImagesUsed/pizza.ico")

label1 = Label(root, text="Welcome to The Saturday Night Pizza")
label1.pack(anchor=W)

var1 = StringVar()
var1.set('Welcome, Please choose the toppings!')


def onClick(value):
    label1 =Label(root, text=value)
    label1.pack(anchor=W)

radioButton1 = Radiobutton(root, text="Cheese", variable=var1, value='Cheese Ordered')
radioButton2 = Radiobutton(root, text="Mushroom", variable=var1, value='Mushroom Ordered')

radioButton1.pack(anchor=W)
radioButton2.pack(anchor=W)

myButton = Button(root, text="Choose Topping and Click me to order", command= lambda : onClick(var1.get()))
myButton.pack(anchor=W)

root.mainloop()