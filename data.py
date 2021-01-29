from main import *

class HandleEntry:
    def __init__(self, homeworkEntry, dateEntry):
        self.homeworkEntry = homeworkEntry
        self.dateEntry = dateEntry

class SubmitEntry:
    def __init__(self, addHomeworkRow, addDateRow, homeworkLabel, dateLabel):
        self.homeworkLabel = homeworkLabel
        self.dateLabel = dateLabel
        self.addHomeworkRow = addHomeworkRow
        self.addDateRow = addDateRow
        self.addHomeworkRow = 0
        self.addDateRow = 0

    def submit_action(self):
        if HandleEntry.homeworkEntry == "" or HandleEntry.dateEntry == "":
            print("error")
        else:
            self.addHomeworkRow += 2
            self.addDateRow += 2

            self.homeworkLabel = Label(root, text=HandleEntry.homeworkEntry + " | Date due: " + HandleEntry.dateEntry, font="Roboto 18")
            self.homeworkLabel.grid(row=self.addHomeworkRow, column=0, pady=10, padx=10)
            self.dateLabel.Button(root, text="Delete", font="Roboto 10", height=2, width=8, activebackground="red", command=print("delete"))
            self.dateLabel.grid(row=self.addDateRow, column=0, pady=2, padx=10)