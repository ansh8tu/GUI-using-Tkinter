from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Slide it away!')
root.iconbitmap('allImagesUsed/imageViewerAppIcon.ico')
root.geometry("600x600")

mySliderVertical = Scale(root, from_=0, to= 1000, tickinterval=100, length=300)
mySliderVertical.grid(row=0, column=3)

mySliderHorizontal = Scale(root, from_=0, to= 1000, orient=HORIZONTAL, tickinterval =100, length=300)
mySliderHorizontal.grid(row=1, column=1)

def resize():    
    myLabel = Label(root, text = f'{mySliderHorizontal.get()} x {mySliderVertical.get()}')
    myLabel.grid(row=2, column=1)
    root.geometry(f'{mySliderHorizontal.get()}x{mySliderVertical.get()}')


myButton = Button(root, text="Click here to Resize", command=resize)
myButton.grid(row=3, column=1)

root.mainloop()