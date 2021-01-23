"""
Homework Manager App!
created by JustJee 22/01/2021 
created to learn how to use Tkinter and have a app to manage homework!
"""

from tkinter import *

# Settings for the GUI
root = Tk()
root.title("Homework Manager!")
root.geometry("800x800")

# Title
appTitle = Label(root, text="Homework Manager!", font="Roboto 30")
appTitle.pack(pady="20", padx="5")

# Title underline
line = Canvas(root, width=400, height=3, bd=0,highlightthickness=0)
line.configure(bg="black")
line.pack(pady="5", padx="5")








root.mainloop()