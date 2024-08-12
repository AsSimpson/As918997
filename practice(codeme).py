from tkinter import *
import tkinter.font as tkFont
root = Tk()
root.geometry("500x500")

def print_details():
    name_count = 0
    while name_count < counters['total_entries']:
        Label(root, text=name_count, font=normal_font).grid(column=0, row=name_count + 8)
        Label(root, text=(myList[name_count][0]), font=normal_font).grid(column=1, row=name_count + 8)
        Label(root, text=(myList[name_count][1]), font=normal_font).grid(column=2, row=name_count + 8)
        Label(root, text=(myList[name_count][2]), font=normal_font).grid(column=3, row=name_count + 8)
        Label(root, text=(myList[name_count][3]), font=normal_font).grid(column=4, row=name_count + 8)
        name_count += 1
        counters['name_count'] = name_count


def myClick():
    myLabel3 = Label(root, text="Look! I clicked a Button!!")
    myLabel3.grid(row=10, column=0)
    name_count += 1

# Create a button
myButton1 = Button(root, text='Click me', padx=50, pady=60, command=myClick)

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Simpson")

# Shoving it onto the screen, use .grid instead of .pack
myLabel1.grid(row=1, column=0)
myLabel2.grid(row=2, column=0)
myButton1.grid(row=3, column=0)

counters = {'total_entries': 0, 'name_count': 0}
myList = []

normal_font = tkFont.Font(family="Agency FB", size=12, weight=tkFont.NORMAL)

root.mainloop()
