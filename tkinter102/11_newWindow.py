from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('My Favourite Artists')
root.iconbitmap('allImagesUsed/imageViewerAppIcon.ico')


def onPressedLauv():
    global myImage

    anotherWindow = Toplevel()
    anotherWindow.title('This is Lauv!')
    anotherWindow.iconbitmap('allImagesUsed/imageViewerAppIcon.ico')

    myImage = ImageTk.PhotoImage(Image.open('allImagesUsed/lauv1.png'))
    imageLabel = Label(anotherWindow, image=myImage)
    imageLabel.pack()

    anotherWindowButton = Button(anotherWindow, text='Exit', command=anotherWindow.destroy, width=70)
    anotherWindowButton.pack()

def onPressedCamila():
    global myImage

    anotherWindow = Toplevel()
    anotherWindow.title('This is Camila!')
    anotherWindow.iconbitmap('allImagesUsed/imageViewerAppIcon.ico')

    myImage = ImageTk.PhotoImage(Image.open('allImagesUsed//img11.jpg'))
    imageLabel = Label(anotherWindow, image=myImage)
    imageLabel.pack()

    anotherWindowButton = Button(anotherWindow, text='Exit', command=anotherWindow.destroy, width=70)
    anotherWindowButton.pack()


myImage2 = ImageTk.PhotoImage(Image.open('allImagesUsed/a.jpg'))
imageLabel1 = Label(root, image=myImage2)
imageLabel1.pack()

button1 = Button(root, text='Click Me to Checkout Lauv\'s Collection', command=onPressedLauv, padx=10, pady=3, width=70)
button1.pack()

button2 = Button(root, text='Click Me to Checkout Camila\'s Collection', command=onPressedCamila, padx=10, pady=3, width=70)
button2.pack()

button2 = Button(root, text='Click Me to Exit App', command=root.destroy, padx=10, pady=3, width=70)
button2.pack()

root.mainloop()