"""
Homework Manager App!
created by JustJee 22/01/2021 
created to learn how to use Tkinter and have a app to manage homework!
"""

from tkinter import *

def submitAction():
    print("button clicked")

# Settings for the GUI
root = Tk()
root.title("Homework Manager!")
root.geometry("800x800")

# Title
appTitle = Label(root, text="Homework Manager!", font="Roboto 30")
appTitle.grid(row=0, column=0, pady=20, padx=5)

# Title underline
line = Canvas(root, width=400, height=3, bd=0,highlightthickness=0)
line.configure(bg="black")
line.grid(row=1, column=0, pady=1, padx=5)

# Homework text
homeworkText = Label(root, text="Enter homework to do:", font="Roboto 24")
homeworkText.grid(row=2,column=0, pady=20, padx=5)

# Homework to do text box
homeworkTodo = Entry(root, width=50)
homeworkTodo.grid(row=3, column=0, pady=20, padx=5)

# Time due text
timeDueText = Label(root, text="Enter date due:", font="Roboto 24")
timeDueText.grid(row=4,column=0, pady=20, padx=5)

# Date due text box
dateDue = Entry(root, width=50)
dateDue.grid(row=5, column=0, pady=20, padx=5)

# Submit button
submitButton = Button(root, text="Submit", command=submitAction)
submitButton.grid(row=6, column=0, pady=20, padx=5)









root.mainloop()