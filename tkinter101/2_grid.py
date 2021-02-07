from tkinter import *

#main 
root = Tk()

#creating a label
myLabelWithGrid = Label(root, text="Hello, let\'s go anywhere")
myName = Label(root, text = "Umm, let's stay at home only it\'s covid! ")

#so what the grid does is that it fixes the position of the label at the given (row,column) co-ordinate
myLabelWithGrid.grid(row="0", column="0")
myName.grid(row="1", column="0")

#run the code until user wants
root.mainloop()
