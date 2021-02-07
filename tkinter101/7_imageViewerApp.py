from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Lauv's Album")
root.iconbitmap('allImagesUsed/imageViewerAppIcon.ico')

myImage1 = ImageTk.PhotoImage(Image.open('allImagesUsed/img1.jfif'))
myImage2 = ImageTk.PhotoImage(Image.open('allImagesUsed/img2.jfif'))
myImage3 = ImageTk.PhotoImage(Image.open('allImagesUsed/img3.jfif'))
myImage4 = ImageTk.PhotoImage(Image.open('allImagesUsed/img4.jfif'))
myImage5 = ImageTk.PhotoImage(Image.open('allImagesUsed/img5.jfif'))

gallery = [myImage1, myImage2, myImage3, myImage4, myImage5]

#do keep in mind these bd and relief and also sticky
statusLabel = Label(root, text = f'Img 1 of {len(gallery)}', bd=1, relief=SUNKEN, anchor = E)
statusLabel.grid(row = 2, column = 0, columnspan=3, sticky=W+E)

myLabel = Label(image = gallery[0])
myLabel.grid(row=0, column=0, columnspan=3)

def onForwardClick(imageNumber):

    global myLabel
    global forwardButton
    global backButton

    myLabel.grid_forget()
    myLabel = Label(image = gallery[imageNumber-1])
    forwardButton = Button(root, text='Next>>',  fg='#5B0E2D', bg ='#FFA781', borderwidth=2, command = lambda : onForwardClick(imageNumber+1))
    backButton = Button(root, text='<<Back',  fg='#5B0E2D', bg ='#FFA781', borderwidth=2, command = lambda : onBackwardClick(imageNumber-1))

    if imageNumber==5:
        forwardButton = Button(root, text='Next>>',  fg='#5B0E2D', bg ='#FFA781', borderwidth=2, state = DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    backButton.grid(row=1, column=0)
    forwardButton.grid(row=1, column=2)

    #added status bar
    statusLabel = Label(root, text = f'Img {imageNumber} of {len(gallery)}', bd=1, relief=SUNKEN, anchor = E)
    statusLabel.grid(row = 2, column = 0, columnspan=3, sticky=W+E)


def onBackwardClick(imageNumber):

    global myLabel
    global forwardButton
    global backButton

    myLabel.grid_forget()
    myLabel = Label(image = gallery[imageNumber-1])
    forwardButton = Button(root, text='Next>>',  fg='#5B0E2D', bg ='#FFA781', borderwidth=2, command = lambda : onForwardClick(imageNumber+1))
    backButton = Button(root, text='<<Back',  fg='#5B0E2D', bg ='#FFA781', borderwidth=2, command = lambda : onBackwardClick(imageNumber-1))

    if imageNumber==1:
        backButton = Button(root, text='<<Back',  fg='#5B0E2D', bg ='#FFA781', borderwidth=2, state = DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    backButton.grid(row=1, column=0)
    forwardButton.grid(row=1, column=2)

    statusLabel = Label(root, text = f'Img {imageNumber} of {len(gallery)}', bd=1, relief=SUNKEN, anchor = E)
    statusLabel.grid(row = 2, column = 0, columnspan=3, sticky=W+E)


backButton = Button(root, text='<<Back',  fg='#5B0E2D', bg ='#FFA781', borderwidth=2, command = onBackwardClick, state = DISABLED)
exitAppButton = Button(root, text='Exit Application', fg='#5B0E2D', bg ='#FFA781', borderwidth=2, command=exit, width=20)
forwardButton = Button(root, text='Next>>',  fg='#5B0E2D', bg ='#FFA781', borderwidth=2, command = lambda : onForwardClick(2))

backButton.grid(row=1, column=0)
exitAppButton.grid(row=1, column=1, pady=10)
forwardButton.grid(row=1, column=2)



root.mainloop()