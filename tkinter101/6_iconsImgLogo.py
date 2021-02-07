from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Lauv Songs')
root.iconbitmap('allImagesUsed/favicon.ico')

myImage = ImageTk.PhotoImage(Image.open('lauv1.png'))
imageLabel = Label(image=myImage)
imageLabel.pack()

def onPress():
    myLabel =Label(root, text='It\'s Covid time but we\'ll be back soon')
    myLabel.pack()

concertButton = Button(root, text=" Upcoming Events ", fg='black', command=onPress, width='60', borderwidth=5)
concertButton.pack()

exitButton = Button(root, text=" Exit App ", fg='black', command = exit, width='40', borderwidth=5)
exitButton.pack()

root.mainloop()