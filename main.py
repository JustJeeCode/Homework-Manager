"""
Homework Manager App!
created by JustJee 22/01/2021 
created to learn how to use Tkinter and have a app to manage homework!
"""

from tkinter import *

# Variables
newRow = 10

# Saves the text in the entrys
def get_entrys():
    global savedHomeworkTodo
    global savedDateDue

    savedHomeworkTodo = homeworkTodo.get()
    savedDateDue = dateDue.get()

# Prints saved text and saves it
def submit_action():

    get_entrys()
    if savedHomeworkTodo == "" or savedDateDue == "":
        print("Error")
    else:
        # Homework Text
        global newRow
        newRow += 1

        global homeworkDue
        homeworkDue = Label(root, text=savedHomeworkTodo + " | Date due: " + savedDateDue, font="Roboto 18")
        homeworkDue.grid(row=newRow, column=0, pady=5, padx=10)


# Settings for the GUI
root = Tk()
root.title("Homework Manager!")
root.geometry("800x800")

# Over title line work
line = Canvas(root, width=800, height=3, bd=0,highlightthickness=0)
line.configure(bg="black")
line.grid(row=1, column=0, pady=10, padx=0)

# Title
appTitle = Label(root, text="Homework Manager!", font="Roboto 30")
appTitle.grid(row=2, column=0, pady=20, padx=5)

# Title underline
line = Canvas(root, width=800, height=3, bd=0,highlightthickness=0)
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
submitButton = Button(root, text="Submit", font="Roboto 12", height=2, width=12, activebackground="lightgreen", command=submit_action)
submitButton.grid(row=8, column=0, pady=20, padx=5)

# Submit underline
line = Canvas(root, width=800, height=3, bd=0,highlightthickness=0)
line.configure(bg="black")
line.grid(row=9, column=0, pady=30, padx=0)

# Homework todo label
homeworkTodoLabel = Label(root, text="Homework to-do:", font="Roboto 24")
homeworkTodoLabel.grid(row=10, column=0, pady=5, padx=10)









root.mainloop()