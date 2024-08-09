# import tkinter so we can make a GUI
from tkinter import *


# print details of all the items
def print_items_details():
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica", 10, "bold"), text="Row").grid(column=0, row=7)
    Label(main_window, font=("Helvetica", 10, "bold"), text="Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica", 10, "bold"), text="Items Hired").grid(column=2, row=7)
    Label(main_window, font=("Helvetica", 10, "bold"), text="Receipt Number").grid(column=3, row=7)
    Label(main_window, font=("Helvetica", 10, "bold"), text="Items Number").grid(column=4, row=7)
    # Add each item in the list into its own row
    while name_count < counters['total_entries']:
        Label(main_window, text=name_count).grid(column=0, row=name_count + 8)
        Label(main_window, text=(Items_details[name_count][0])).grid(column=1, row=name_count + 8)
        Label(main_window, text=(Items_details[name_count][1])).grid(column=2, row=name_count + 8)
        Label(main_window, text=(Items_details[name_count][2])).grid(column=3, row=name_count + 8)
        Label(main_window, text=(Items_details[name_count][3])).grid(column=4, row=name_count + 8)
        name_count += 1
        counters['name_count'] = name_count


# Check the inputs are all valid
def check_inputs():
    clear_error_messages()
    input_check = 0
    Label(main_window, text="               ").grid(column=2, row=0)
    Label(main_window, text="               ").grid(column=2, row=1)
    Label(main_window, text="               ").grid(column=2, row=2)
    Label(main_window, text="               ").grid(column=2, row=3)
    # Check that Name is not blank, set error text if blank
    if len(entry_Name.get()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=0)
        input_check = 1
    # Check that Items Hired is not blank, set error text if blank
    if len(entry_ItemsHired.get()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=1)
        input_check = 1
    # Check that Receipt Number is not blank and between 2 and 15, set error text if invalid
    if entry_ReciptNumber.get().isdigit():
        if int(entry_ReciptNumber.get()) < 2 or int(entry_ReciptNumber.get()) > 15:
            Label(main_window, fg="red", text="").grid(column=2, row=2)
            input_check = 1
    else:
        Label(main_window, fg="red", text="Numbers only").grid(column=2, row=2)
        input_check = 1
    # Check that Items Number is not blank and between 0 and 30, set error text if invalid
    if entry_ItemsNumber.get().isdigit():
        if int(entry_ItemsNumber.get()) < 0 or int(entry_ItemsNumber.get()) > 30:
            Label(main_window, fg="red", text="").grid(column=2, row=3)
            input_check = 1
    else:
        Label(main_window, fg="red", text="Numbers only").grid(column=2, row=3)
        input_check = 1

    if input_check == 0:
        append_item()


def clear_error_messages():
    # Clear all error messages
    for row in range(4):
        Label(main_window, text="               ").grid(column=2, row=row)


# add the next item to the list
def append_item():
    # append each item to its own area of the list
    Items_details.append([entry_Name.get(), entry_ItemsHired.get(), entry_ReciptNumber.get(), entry_ItemsNumber.get()])
    # clear the entry boxes
    entry_Name.delete(0, 'end')
    entry_ItemsHired.delete(0, 'end')
    entry_ReciptNumber.delete(0, 'end')
    entry_ItemsNumber.delete(0, 'end')
    counters['total_entries'] += 1


# delete a row from the list
def delete_row():
    # find which row is to be deleted and delete it
    del Items_details[int(delete_item.get())]
    counters['total_entries'] -= 1
    name_count = counters['name_count']
    delete_item.delete(0, 'end')
    # clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0, row=name_count + 7)
    Label(main_window, text="       ").grid(column=1, row=name_count + 7)
    Label(main_window, text="       ").grid(column=2, row=name_count + 7)
    Label(main_window, text="       ").grid(column=3, row=name_count + 7)
    Label(main_window, text="       ").grid(column=4, row=name_count + 7)
    # print all the items in the list
    print_items_details()


# create the buttons and labels
def setup_buttons():
    # create all the labels, buttons, and entry boxes. Put them in the correct grid location
    Label(main_window, text="Name").grid(column=0, row=0, pady="10", padx="10", sticky=E)
    Label(main_window, text="Items Hired").grid(column=0, row=1, pady="10", padx="10", sticky=E)
    Button(main_window, text="Quit", command=quit, width=10).grid(column=4, row=0, pady="10", padx="10", sticky=E)
    Button(main_window, text="Append Details", command=check_inputs).grid(column=3, row=1,pady="10",padx="10")
    Button(main_window, text="Print Details", command=print_items_details, width=10).grid(column=4, row=1, pady="10", padx="10", sticky=E)
    Label(main_window, text="Receipt Number").grid(column=0, row=2, pady="10", padx="10", sticky=W)
    Label(main_window, text="Items Number").grid(column=0, row=3, pady="10", padx="10", sticky=E)
    Label(main_window, text="Row #").grid(column=3, row=2, sticky=E)
    Button(main_window, text="Delete Row", command=delete_row, width=10).grid(column=4, row=3, sticky=E)
    Label(main_window, text="               ").grid(column=2, row=0)


# start the program running
def main():
    # Start the GUI
    main_window.geometry("780x400")
    setup_buttons()
    main_window.mainloop()


# create empty list for item details and counters for entries in the list
counters = {'total_entries': 0, 'name_count': 0}
Items_details = []
main_window = Tk()
entry_Name = Entry(main_window)
entry_Name.grid(column=1, row=0)
entry_ItemsHired = Entry(main_window)
entry_ItemsHired.grid(column=1, row=1)
entry_ReciptNumber = Entry(main_window)
entry_ReciptNumber.grid(column=1, row=2)
entry_ItemsNumber = Entry(main_window)
entry_ItemsNumber.grid(column=1, row=3)
delete_item = Entry(main_window)
delete_item.grid(column=3, row=3)
main()