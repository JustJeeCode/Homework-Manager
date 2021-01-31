"""
Homework Manager App!
created by JustJee 22/01/2021 
created to learn how to use Tkinter and have a app to manage homework!
"""

# GUI resolution
width = 1920
height = 1080

# Imports
from tkinter import *
from tkinter import ttk


# Variables
global savedHomework
global savedDate
global homeworkList
savedHomework = ""
savedDate = ""
homeworkList = []


# Settings for the GUI
root = Tk()
root.title("Homework Manager!")
root.geometry(str(width) + "x" + str(height))



class Rows:
    def __init__(self, homeworkRow, dateRow):
        self.homeworkRow = homeworkRow
        self.dateRow = dateRow

    def add_rows(self):
        self.homeworkRow += 2
        self.dateRow += 2

rows = Rows(11, 12)

class Entrys:
    def __init__(self, savedHomework, savedDate, homeworkList):
        self.savedHomework = savedHomework
        self.savedDate = savedDate
        self.homeworkList = homeworkList

    def get_entrys(self):
        self.savedHomework = homeworkTodo.get()
        self.savedDate = dateDue.get()

        self.homeworkList.append(savedHomework)
        self.homeworkList.append(rows.homeworkRow)
        self.homeworkList.append(savedDate)
        self.homeworkList.append(rows.dateRow)

        rows.add_rows()
        self.create_entrys()

    def create_entrys(self):
        newHomework = Label(root, text=self.savedHomework + " | Date due: " + self.savedDate, font="Roboto 18")
        newHomework.grid(row=rows.homeworkRow, column=0, pady=10, padx=10)
        deleteButton = Button(root, text="Delete", font="Roboto 10", height=2, width=8, activebackground="red")
        deleteButton.grid(row=rows.dateRow, column=0, pady=2, padx=10) 

entrys = Entrys(savedHomework, savedDate, homeworkList)




# Over title line work
line = Canvas(root, width=width, height=3, bd=0,highlightthickness=0)
line.configure(bg="black")
line.grid(row=1, column=0, pady=0, padx=0)

# Title
appTitle = Label(root, text="Homework Manager!", font="Roboto 30")
appTitle.grid(row=2, column=0, pady=20, padx=5)

# Title underline
line = Canvas(root, width=width, height=3, bd=0,highlightthickness=0)
line.configure(bg="black")
line.grid(row=3, column=0, pady=2, padx=0)

# Homework text
homeworkText = Label(root, text="Enter homework to do:", font="Roboto 24")
homeworkText.grid(row=4,column=0, pady=20, padx=5)

# Homework to do text box
homeworkTodo = Entry(root, width=50, bd=4, bg="white", font="Roboto 12")
homeworkTodo.grid(row=5, column=0, pady=20, padx=5)

# Time due text
timeDueText = Label(root, text="Enter date due:", font="Roboto 24")
timeDueText.grid(row=6,column=0, pady=20, padx=10)

# Date due text box
dateDue = Entry(root, width=50, bd=4, bg="white", font="Roboto 12")
dateDue.grid(row=7, column=0, pady=20, padx=10)

# Submit button 
submitButton = Button(root, text="Submit", font="Roboto 12", height=2, width=12, activebackground="lightgreen", command=entrys.get_entrys)
submitButton.grid(row=8, column=0, pady=20, padx=5)

# Homework todo label underline
line = Canvas(root, width=width, height=3, bd=0,highlightthickness=0)
line.configure(bg="black")
line.grid(row=9, column=0, pady=30, padx=0)

# Homework todo label
homeworkTodoLabel = Label(root, text="Homework to-do:", font="Roboto 24")
homeworkTodoLabel.grid(row=10, column=0, pady=20, padx=10)


root.mainloop()