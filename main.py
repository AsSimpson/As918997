from tkinter import *

root = Tk()

root.geometry("500x500")

def print_details():
    name_count = 0
    Label(root, font=("Helvetica", 10, "bold"), text="Row").grid(column=0, row=7)
    Label(root, font=("Helvetica", 10, "bold"), text="Name").grid(column=1, row=7)
    Label(root, font=("Helvetica", 10, "bold"), text="Items Hired").grid(column=2, row=7)
    Label(root, font=("Helvetica", 10, "bold"), text="Receipt Number").grid(column=3, row=7)
    Label(root, font=("Helvetica", 10, "bold"), text="Items Number").grid(column=4, row=7)
    while name_count < counters['total_entries']:
        Label(root, text=name_count).grid(column=0, row=name_count + 8)
        Label(root, text=(myList[name_count][0])).grid(column=1, row=name_count + 8)
        Label(root, text=(myList[name_count][1])).grid(column=2, row=name_count + 8)
        Label(root, text=(myList[name_count][2])).grid(column=3, row=name_count + 8)
        Label(root, text=(myList[name_count][3])).grid(column=4, row=name_count + 8)
        name_count += 1
        counters['name_count'] = name_count
label_HiredItems = Label(root, text="Hired items")
label_name = Label(root, text="Name")
Label_3 = Label(root, text="")
nameEntry = Entry(root)
button1 = Button(root, text="Append details")

var1 = nameEntry.get()
def append_details():
    dr_label = Label(root, text=var1)
    dr_label.grid(row=9, column=0)


label_HiredItems.grid(row=0, column=0)
label_name.grid(row=1, column=0)
Label_3.grid(row=2, column=0)
nameEntry.grid(row=3, column=0)
button1.grid(row=4, column=0)

counters = {'total_entries': 0, 'name_count': 0}
myList = []

root.mainloop()
