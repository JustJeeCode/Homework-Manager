"""
Homework Manager App!
created by JustJee 22/01/2021 
created to learn how to use Tkinter and have a app to manage homework!
"""

from tkinter import *
from tkinter import ttk

# Settings for the GUI
root = Tk()
root.title("Homework Manager!")
root.geometry("800x800")

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
secondFrame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=secondFrame, anchor="nw")

# Variables
newRow = 9 #first new save
newRow2 = 10 #first delete button
deleteRow = newRow 
deleteRow2 = newRow2 

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
        global newRow2
        global homeworkDue
        global deleteButton
        global deleteRow
        global deleteRow2
        newRow += 2
        newRow2 += 2
        deleteRow += 2
        deleteRow2 += 2

        print("adding a row" + str(newRow))
        print("adding a row" + str(newRow2))

        homeworkDue = Label(secondFrame, text=savedHomeworkTodo + " | Date due: " + savedDateDue, font="Roboto 18")
        homeworkDue.grid(row=newRow, column=0, pady=10, padx=10)
        deleteButton = Button(secondFrame, text="Delete", font="Roboto 10", height=2, width=8, activebackground="red", command=delete_button_action)
        deleteButton.grid(row=newRow2, column=0, pady=2, padx=10)

def delete_button_action():
    print("delete button pressed")
    global deleteRow
    global deleteRow2
    global newRow
    global newRow2

    l = list(secondFrame.grid_slaves(row=int(deleteRow)))
    l2 = list(secondFrame.grid_slaves(row=int(deleteRow2)))
    print(l)
    for w in l:
        w.grid_forget()

    for w in l2:
        w.grid_forget()

    print("deleteting a row" + str(deleteRow))
    print("deleteting a row" + str(deleteRow2))
    deleteRow -= 2
    deleteRow2 -= 2
    newRow -= 2
    newRow2 -= 2


# Over title line work
line = Canvas(secondFrame, width=1920, height=3, bd=0,highlightthickness=0)
line.configure(bg="black")
line.grid(row=1, column=0, pady=0, padx=0)

# Title
appTitle = Label(secondFrame, text="Homework Manager!", font="Roboto 30")
appTitle.grid(row=2, column=0, pady=20, padx=5)

# Title underline
line = Canvas(secondFrame, width=1920, height=3, bd=0,highlightthickness=0)
line.configure(bg="black")
line.grid(row=3, column=0, pady=2, padx=0)

# Homework text
homeworkText = Label(secondFrame, text="Enter homework to do:", font="Roboto 24")
homeworkText.grid(row=4,column=0, pady=20, padx=5)

# Homework to do text box
homeworkTodo = Entry(secondFrame, width=50, bd=4, bg="white", font="Roboto 12")
homeworkTodo.grid(row=5, column=0, pady=20, padx=5)

# Time due text
timeDueText = Label(secondFrame, text="Enter date due:", font="Roboto 24")
timeDueText.grid(row=6,column=0, pady=20, padx=10)

# Date due text box
dateDue = Entry(secondFrame, width=50, bd=4, bg="white", font="Roboto 12")
dateDue.grid(row=7, column=0, pady=20, padx=10)

# Submit button 
submitButton = Button(secondFrame, text="Submit", font="Roboto 12", height=2, width=12, activebackground="lightgreen", command=submit_action)
submitButton.grid(row=8, column=0, pady=20, padx=5)

# Homework todo label underline
line = Canvas(secondFrame, width=1920, height=3, bd=0,highlightthickness=0)
line.configure(bg="black")
line.grid(row=9, column=0, pady=30, padx=0)

# Homework todo label
homeworkTodoLabel = Label(secondFrame, text="Homework to-do:", font="Roboto 24")
homeworkTodoLabel.grid(row=10, column=0, pady=20, padx=10)


root.mainloop()