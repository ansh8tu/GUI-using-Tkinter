from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()
root.title('System Logs')
root.iconbitmap('allImagesUsed/warning.ico')

message = '''A critical error has occured and the process must be terminated

Would you like to create a crash dump to aid the developers in troubleshooting this issue? This may take upto 5 minutes.

NOTE: The process may appear unresponsive during this time.

'''
def onClick():
    response = messagebox.showerror('System Error', message)
    myLabel = Label(root, text=response)

    if response == 'ok':
        myLabel = Label(root, text='Closing Valorant!')
        myLabel.pack()


myButton = Button(root, text='Format Hard Disk!', command=onClick)
myButton.pack()


root.mainloop()