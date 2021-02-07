from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('My Favourite Artists!')
root.iconbitmap('allImagesUsed/imageViewerAppIcon.ico')

#frame1
frame1 = LabelFrame(root, text = '@camila_cabello', padx=10, pady=10, bd=2)
frame1.pack(padx=20, pady=20)

#to resize an image open it,resize it, use it
img11 = Image.open('allImagesUsed/img11.jpg')
ri1 = img11.resize((400,220), Image.ANTIALIAS)

img1 = ImageTk.PhotoImage(ri1)
labelImg = Label(frame1, image=img1)
labelImg.pack()

#frame2
frame2 = LabelFrame(root, text = '@lauvsongs', padx=10, pady=10, bd=2)
frame2.pack(padx=20, pady=20)

#to resize an image open it,resize it, use it
img22 = Image.open('allImagesUsed/lauv.jpg')
ri2 = img22.resize((400,220), Image.ANTIALIAS)

img2 = ImageTk.PhotoImage(ri2)
labelImg2 = Label(frame2, image=img2)
labelImg2.pack()


root.mainloop()