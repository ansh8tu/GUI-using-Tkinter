from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Open Files Dialog box')
root.iconbitmap('allImagesUsed/imageViewerAppIcon.ico')
root.geometry("600x400")

root.filename = filedialog.askopenfilename(initialdir="/stuff/Applications", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))

newLabel = Label(root, text=root.filename).pack()
myImage = ImageTk.PhotoImage(Image.open(root.filename))
myNewLabel = Label(image=myImage).pack()

root.mainloop()