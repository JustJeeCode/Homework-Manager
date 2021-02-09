# Imports
import tkinter as tk
import tkinter.font
import os

# Variables
width = 1920
height = 1080

root = tk.Tk()
root.geometry(str(width) + "x" + str(height))
root.title("Homework Manager!")

background = tk.PhotoImage(file = "images\App_background.png")   
mainCanvas = tk.Canvas(root, width = width, height = height)
mainCanvas.pack(fill = "both", expand = True)

mainCanvas.create_image(0, 0, image = background, anchor = "nw")

# Header Class
class Header(tk.Frame):
    def __init__(self):
        # Heading
        self.homeworkHeading = mainCanvas.create_text(960, 50, text = "Homework Manager", font = "oldnewspapertypes 40 bold")

        # Heading Underline
        #line = canvas.create_line(x0, y0, x1, y1, ..., xn, yn, options)
        self.titleUnderline = mainCanvas.create_line(960, 70, 1920, 3)


# Homework Class
class Homework(tk.Frame):
    def __init__(self):
        # Homework Label
        self.homeworkLabel = mainCanvas.create_text(960, 180, text = "Enter Homework To Do:", font = "Linowrite 24")

        # Homework Entry
        self.homeworkEntry = mainCanvas.create_window(960, 200)


# Date Class
class Date(tk.Frame):
    def __init__(self):
        # Date Label
        self.dateLabel = mainCanvas.create_text(960, 250, text = "Enter Date Due:", font = "Linowrite 24")

        # Date Entry
        self.dateEntry = mainCanvas.create_window(960, 270)


# NewSubmission Class
class NewSubmission(tk.Frame):
    def __init__(self):
        self.submitButton = tk.Button(root, text = "Submit", font = "Linowrite 16", height = 1, width = 12, activebackground = "lightgreen", command = print("print"))
        self.submitButtonWindow = mainCanvas.create_window(880, 300, anchor = "nw", window = self.submitButton)

# Homework Todo List Class
class TodoTitle(tk.Frame):
    def __init__(self):
        self.overline = tk.Canvas(root, width = width, height = 3, bd = 0,highlightthickness = 0)
        self.overline.configure(bg = "black")

        # Homework todo label
        self.TodoLabel = mainCanvas.create_text(960, 380, text = "Homework Todo:", font = "Linowrite 24")


# Main App
class MainApplication(tk.Frame):
    header = Header()
    homework = Homework()
    date = Date()
    newSubmission = NewSubmission()
    todoTitle = TodoTitle()


# Packing MainApp
MainApplication(root).pack(side="top", fill="both", expand=True)
root.mainloop()