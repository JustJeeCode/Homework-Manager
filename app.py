# Imports
import tkinter as tk
import tkinter.font

# Variables
width = 1920
height = 1080

root = tk.Tk()
root.geometry(str(width) + "x" + str(height))
root.title("Homework Manager!")

# Header Class
class Header(tk.Frame):
    def __init__(self):
        # Heading
        self.homeworkHeading = tk.Label(root, text = "Homework Manager", font = "FunSized 35 bold")
        self.homeworkHeading.grid(row = 1, column = 1, padx = 10, pady = 10)

        # Heading Underline
        self.titleUnderline = tk.Canvas(root, width = width, height = 3, bd = 0, highlightthickness = 0)
        self.titleUnderline.configure(bg = "black")
        self.titleUnderline.grid(row = 2, column = 1, pady = 10, padx = 0)


# Homework Class
class Homework(tk.Frame):
    def __init__(self):
        # Homework Label
        self.homeworkLabel = tk.Label(root, text = "Enter Homework To Do:", font = "Roboto 24")
        self.homeworkLabel.grid(row = 3, column = 1, pady = 50, padx = 0)

        # Homework Entry
        self.homeworkEntry = tk.Entry(root, width = 50, bd = 4, bg = "white", font="Roboto 12")
        self.homeworkEntry.grid(row = 4, column = 1, pady = 0, padx = 0)


# Date Class
class Date(tk.Frame):
    def __init__(self):
        # Date Label
        self.dateLabel = tk.Label(root, text = "Enter Date Due:", font = "Roboto 24")
        self.dateLabel.grid(row = 5, column = 1, pady = 50, padx = 0)

        # Date Entry
        self.dateEntry = tk.Entry(root, width = 50, bd = 4, bg = "white", font = "Roboto 12")
        self.dateEntry.grid(row = 6, column = 1, pady = 0, padx = 0)


# NewSubmission Class
class NewSubmission(tk.Frame):
    def __init__(self):
        self.submitButton = tk.Button(root, text = "Submit", font = "Roboto 12", height = 2, width = 12, activebackground = "lightgreen", command = print("print"))
        self.submitButton.grid(row = 7, column = 1, pady = 50, padx = 0)


# Homework Todo List Class
class TodoTitle(tk.Frame):
    def __init__(self):
        self.overline = tk.Canvas(root, width = width, height = 3, bd = 0,highlightthickness = 0)
        self.overline.configure(bg = "black")
        self.overline.grid(row = 8, column = 1, pady = 10, padx = 0)

        # Homework todo label
        self.TodoLabel = tk.Label(root, text = "Homework Todo:", font = "Roboto 24")
        self.TodoLabel.grid(row = 9, column = 1, pady = 10, padx = 0)


# Main App
class MainApplication(tk.Frame):
    header = Header()
    homework = Homework()
    date = Date()
    newSubmission = NewSubmission()
    TodoTitle = TodoTitle()


# Packing MainApp
MainApplication(root).grid(row = 0, column = 0)
root.mainloop()