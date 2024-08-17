import os
import time
import random
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox



def print_items_details():
    name_count = 0

    # Add each item in the list into its own row
    while name_count < counters['total_entries']:
        Label(root, text=name_count + 1, relief="sunken", font=("Helvetica", 10), fg="blue", bg="white").grid(
            column=0, row=name_count + 8, padx=5, pady=5)
        Label(root, text=(Items_details[name_count][0]), relief="sunken", font=fontNum1, fg="blue",
              bg="white").grid(column=1, row=name_count + 8, padx=5, pady=5)
        Label(root, text=(Items_details[name_count][1]), relief="sunken", font=("Helvetica", 10), fg="blue",
              bg="white").grid(column=2, row=name_count + 8, padx=5, pady=5)
        Label(root, text=(Items_details[name_count][2]), relief="sunken", font=("Helvetica", 10), fg="blue",
              bg="white").grid(column=3, row=name_count + 8, padx=5, pady=5)
        Label(root, text=(Items_details[name_count][3]), relief="sunken", font=("Helvetica", 10), fg="blue",
              bg="white").grid(column=4, row=name_count + 8, padx=5, pady=5)
        name_count += 1
        counters['name_count'] = name_count


# Check the inputs are all valid
def check_inputs():
    input_check = 0
    # Check that Name is not blank, set error text if blank
    if len(entry_Name.get()) == 0:
        messagebox.showerror(title="error", message="Input NAME please. ")
        input_check = 1
    # Check if any item is selected, set error text if blank
    if entry_ItemsPurchase.get() == "Please choose an item name. ":
        messagebox.showerror(title="error", message="Choose a PURCHASED ITEM NAME please. ")
        input_check = 1
    # Check that Receipt Number is not blank and between 2 and 15, set error text if invalid
    # Bug with item and receipt number validation check
    if entry_ReciptNumber.get().isdigit():
        if int(entry_ReciptNumber.get()) < 0 or int(entry_ReciptNumber.get()) >= 2000:
            messagebox.showerror(title="error", message="Input a valid RECEIPT NUMBER please. ")
            input_check = 1
    else:
        messagebox.showerror(title="error", text="RECEIPT NUMBER should be a number. ")
        input_check = 1
    # Check that Items Number is not blank and between 0 and 30, set error text if invalid
    if entry_ItemsNumber.get().isdigit():
        if int(entry_ItemsNumber.get()) < 0 or int(entry_ItemsNumber.get()) > 30:
            messagebox.showerror(title="error", text="Input a valid RECEIPT NUMBER please. ")
            input_check = 1
    else:
        messagebox.showerror(title="error", text="RECEIPT NUMBER should be a number. ")
        input_check = 1

    if input_check == 0:
        append_item()


# Add the next item to the list


def append_item():
    # Append each item to its own area of the list
    Items_details.append([entry_Name.get(), entry_ItemsPurchase.get(), entry_ReciptNumber.get(), entry_ItemsNumber.get()])
    save_receipt_to_file(entry_ReciptNumber.get())
    # Clear the entry boxes
    entry_Name.delete(0, 'end')
    entry_ItemsPurchase.delete(0, 'end')
    entry_ReciptNumber.delete(0, 'end')
    entry_ItemsNumber.delete(0, 'end')
    counters['total_entries'] += 1


def save_receipt_to_file(receipt_number):
    if not os.path.exists('savedata'):
        os.makedirs('savedata')
    with open(f'savedata/{receipt_number}.txt', 'w') as file:
        file.write(f"Name: {entry_Name.get()}\n")
        file.write(f"Items Hired: {entry_ItemsPurchase.get()}\n")
        file.write(f"Receipt Number: {entry_ReciptNumber.get()}\n")
        file.write(f"Items Number: {entry_ItemsNumber.get()}\n")


# Delete a row from the list
def delete_row():
    row_index = int(delete_item.get()) - 1
    if 0 <= row_index < counters['total_entries']:
        delete_receipt_file(Items_details[row_index][2])
        del Items_details[row_index]
        counters['total_entries'] -= 1
        name_count = counters['name_count']
        delete_item.delete(0, 'end')
        # Clear the last item displayed on the GUI
        Label(root, text="            ", font=fontNum2, bg="lightblue").grid(column=0, row=name_count + 7)
        Label(root, text="            ", font=fontNum2, bg="lightblue").grid(column=1, row=name_count + 7)
        Label(root, text="            ", font=fontNum2, bg="lightblue").grid(column=2, row=name_count + 7)
        Label(root, text="            ", font=fontNum2, bg="lightblue").grid(column=3, row=name_count + 7)
        Label(root, text="            ", font=fontNum2, bg="lightblue").grid(column=4, row=name_count + 7)
        # Print all the items in the list
        print_items_details()


def delete_receipt_file(receipt_number):
    file_path = f'savedata/{receipt_number}.txt'
    if os.path.exists(file_path):
        os.remove(file_path)


# Random receipt number generator
def random_receipt():
    randNum = random.randint(1, 2000)
    if len(entry_ReciptNumber.get()) != 0:
        entry_ReciptNumber.delete(0, "end")
    entry_ReciptNumber.insert(0, str(randNum))

# Create the buttons and labels
def setup_buttons():
    # Create all the labels, buttons, and entry boxes. Put them in the correct grid location
    Label(root, text="Name", bg="lightblue", font=fontNum1).grid(column=0, row=0, padx=10, pady=10, sticky=W)
    Label(root, text="Items Hired", bg="lightblue", font=fontNum1).grid(column=0, row=1, padx=10, pady=10, sticky=W)
    Label(root, text="Receipt Number", bg="lightblue", font=fontNum1).grid(column=0, row=2, padx=10, pady=10, sticky=W)
    Label(root, text="Items Number", bg="lightblue", font=fontNum1).grid(column=0, row=3, padx=10, pady=10, sticky=W)

    # Create the column headings with color
    Label(root, font=fontNum1, text="Row", fg="black", bg="cyan", width=10, relief="raised", bd=5).grid(
        column=0, row=7)
    Label(root, font=fontNum1, text="Name", fg="white", bg="black", relief="sunken", bd=5).grid(
        column=1, row=7, padx=5, pady=5)
    Label(root, font=fontNum1, text="Items Hired", fg="white", bg="black", relief="ridge",
          bd=5).grid(column=2, row=7, padx=5, pady=5)
    Label(root, font=fontNum1, text="Receipt Number", fg="white", bg="black", relief="groove",
          bd=5).grid(column=3, row=7, padx=5, pady=5)
    Label(root, font=fontNum1, text="Items Hired", fg="white", bg="black", relief="raised",
          bd=5).grid(column=4, row=7, padx=5, pady=5)

    # Button(root, text="Append Details", command=check_inputs, font=fontNum1).grid(column=1, row=4, padx=12, pady=12)

    Button(root, text="Delete Row", command=delete_row, width=10, bg='red', font=fontNum1).grid(column=0, row=5, padx=20, pady=12, sticky=E)

    Button(root, text="Random Number", height=1, command=random_receipt).grid(column=2, row=2, pady=15, sticky='NW')


def setup_image_button():
    #   Label(root, image=button_image, bg="lightblue").grid(column=2, row=0)
    Button(root, image=quit_image, command=quit).grid(column=2, row=0, padx=50, pady=20, sticky='NW')

    Button(root, text="Print Details", font=fontNum1, width=200, height=60, image=button_image, compound=LEFT,
           command=print_items_details).grid(
        column=2, row=3, padx=50, sticky='NW')

    Button(root, text="Append Details", font=fontNum1, width=200, height=60, image=append_image, compound=LEFT,
           command=check_inputs).grid(
        column=2, row=4, padx=50, sticky='NW')


def main():
    root.geometry("900x800")
    root.title("*" * 50 + "Party Purchase" + "*" * 50)
    root.configure(bg='lightblue')

    # Set the window icon
    icon_path = r"Linux_logo.png"  # Ensure you have an 'icon.png' file in the same directory
    icon = PhotoImage(file=icon_path)
    root.iconphoto(False, icon)
    # Start the GUI
    setup_buttons()
    setup_image_button()
    root.mainloop()


counters = {'total_entries': 0, 'name_count': 0}
Items_details = []
root = Tk()
# define fonts
fontNum1 = tkFont.Font(family="Agency FB", size=20, weight="bold")
fontNum2 = tkFont.Font(family="Agency FB", size=30, weight="bold")

# # create background frame
# front_frame = Frame(root, height=240, width=800)
# front_frame.grid(row=0, column=0, sticky="nsew")
#
# bg_image = PhotoImage(file=r"party_image.png")
# bg_label = Label(front_frame, image=bg_image)
# bg_label.grid(row=0, column=0)

# Get purchase information from user input
entry_Name = Entry(root, width=23)
entry_Name.grid(column=1, row=0, sticky=W)
entry_ReciptNumber = Entry(root, width=23)
entry_ReciptNumber.grid(column=1, row=2, sticky=W)
entry_ItemsNumber = Entry(root, width=23)
entry_ItemsNumber.grid(column=1, row=3, sticky=W)
delete_item = Entry(root, width=23)
delete_item.grid(column=1, row=5, sticky=W)

# create combobox
purchase_list = ['Tables', 'Balloons', 'Party Hats', 'Snacks', 'Drinks', 'Serving Bowls']
entry_ItemsPurchase = Combobox(root, values=purchase_list, state='readonly')
entry_ItemsPurchase.grid(column=1, row=1, sticky=W)
entry_ItemsPurchase.set("Please choose an item name. ")

#   import images
button_image = PhotoImage(file=r"printer.png")
quit_image = PhotoImage(file=r"quit button.png")
append_image = PhotoImage(file=r"append.png")

main()
