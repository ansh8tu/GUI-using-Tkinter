from tkinter import *

root = Tk()
root.title("Ticket Booking System")

labelForUser = Label(root, text = 'Username : ' )
labelForUser.pack()

userInput = Entry(root, bg='white', fg='black', width='50')
userInput.pack()
userInput.insert(0, "Username : ")

def onClick():
    messageUser =  f"Congratulations {userInput.get()} , there you go! Tickets Booked!!"
    onCLickLabel = Label(root, text = messageUser)
    onCLickLabel.pack()

mainButton = Button(root, text = "Click here to book Tickets", fg='white', bg='black', command= onClick)
mainButton.pack()

root.mainloop()