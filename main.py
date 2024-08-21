import os
import time
import random
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image


# Check if the inputs are valid
def check_inputs():
    input_check = 0
    # Check that Name is not blank, set error text if blank
    if len(entry_Name.get()) == 0:
        messagebox.showerror(title="error", message="Input NAME please. ")
        input_check = 1
    # Check if any item is selected, set error text if blank
    if entry_ItemsPurchased.get() == "Please choose an item name. ":
        messagebox.showerror(title="error", message="Choose a PURCHASED ITEM NAME please. ")
        input_check = 1
    # Check that Receipt Number is not blank and between 2 and 15, set error text if invalid
    # Bug with item and receipt number validation check
    if entry_ReceiptNumber.get().isdigit():
        if int(entry_ReceiptNumber.get()) < 0 or int(entry_ReceiptNumber.get()) >= 2000:
            messagebox.showerror(title="error", message="Input a valid RECEIPT NUMBER please. ")
            input_check = 1
    else:
        messagebox.showerror(title="error", message="RECEIPT NUMBER should be a number. ")
        input_check = 1
    # Check that Items Number is not blank and between 0 and 30, set error text if invalid
    if entry_ItemsNumber.get().isdigit():
        if int(entry_ItemsNumber.get()) < 0 or int(entry_ItemsNumber.get()) > 100:
            messagebox.showerror(title="error", message="Input a valid RECEIPT NUMBER please. ")
            input_check = 1
    else:
        messagebox.showerror(title="error", message="RECEIPT NUMBER should be a number. ")
        input_check = 1

    if input_check == 0:
        append_item()


def append_item():
    # Append each item to its own area of the list
    Items_details.append([entry_Name.get(), entry_ItemsPurchased.get(), entry_ItemsNumber.get(), entry_ReceiptNumber.get()])
    save_receipt_to_file(entry_ReceiptNumber.get())
    # Clear the entry boxes
    entry_Name.delete(0, 'end')
    entry_ItemsPurchased.delete(0, 'end')
    entry_ReceiptNumber.delete(0, 'end')
    entry_ItemsNumber.delete(0, 'end')
    counters['total_entries'] += 1
    entry_ItemsPurchased.set("Please choose an item name. ")
    print_items_details()


def print_items_details():
    name_count = 0
    while name_count < counters['total_entries']:
        Label(bottom, text=name_count + 1, relief="sunken", font=("Helvetica", 10), fg="black", bg="IndianRed3").grid(
            column=0, row=name_count + 1, padx=5, pady=5)
        Label(bottom, text=(Items_details[name_count][0]), relief="sunken", font=fontNum1, fg="black",
              bg="IndianRed3").grid(column=1, row=name_count + 1, padx=5, pady=5)
        Label(bottom, text=(Items_details[name_count][1]), relief="sunken", font=fontNum1, fg="black",
              bg="IndianRed3").grid(column=2, row=name_count + 1, padx=5, pady=5)
        Label(bottom, text=(Items_details[name_count][2]), relief="sunken", font=fontNum1, fg="black",
              bg="IndianRed3").grid(column=3, row=name_count + 1, padx=5, pady=5)
        Label(bottom, text=(Items_details[name_count][3]), relief="sunken", font=fontNum1, fg="black",
              bg="IndianRed3").grid(column=4, row=name_count + 1, padx=5, pady=5)
        name_count += 1
        counters['name_count'] = name_count


def save_receipt_to_file(receipt_number):
    if not os.path.exists('savedata'):
        os.makedirs('savedata')
    with open(f'savedata/{receipt_number}.txt', 'w') as file:
        file.write(f"Name: {entry_Name.get()}\n")
        file.write(f"Items Hired: {entry_ItemsPurchased.get()}\n")
        file.write(f"Items Number: {entry_ItemsNumber.get()}\n")
        file.write(f"Receipt Number: {entry_ReceiptNumber.get()}\n")


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
        Label(bottom, text="    ", font=fontNum2, bg="IndianRed3").grid(column=0, row=name_count)
        Label(bottom, text="                   ", font=fontNum2, bg="IndianRed3").grid(column=1, row=name_count)
        Label(bottom, text="                 ", font=fontNum2, bg="IndianRed3").grid(column=2, row=name_count)
        Label(bottom, text="            ", font=fontNum2, bg="IndianRed3").grid(column=3, row=name_count)
        Label(bottom, text="            ", font=fontNum2, bg="IndianRed3").grid(column=4, row=name_count)
        # Print all the items in the list
        print_items_details()


def delete_receipt_file(receipt_number):
    file_path = f'savedata/{receipt_number}.txt'
    if os.path.exists(file_path):
        os.remove(file_path)


# Random receipt number generator
def random_receipt():
    randNum = random.randint(1, 2000)
    if len(entry_ReceiptNumber.get()) != 0:
        entry_ReceiptNumber.delete(0, "end")
    entry_ReceiptNumber.insert(0, str(randNum))


def pin_window():
    # print(button_pin["state"])
    if str(button_pin['bg']) != 'gray':
        root.attributes('-topmost', True)
        button_pin.configure(bg='gray', text="Unpin Window")
    elif str(button_pin['bg']) == 'gray':
        root.attributes('-topmost', False)
        button_pin.configure(bg='SeaGreen3', text="Pin Window")


def animation(current_frame=0):
    global loop, loop_2
    image = photoimage_objects[current_frame]

    gif_label.configure(image=image)

    current_frame += 1


    if current_frame == frames:
        current_frame = 0

    loop = right_column.after(50, lambda: animation(current_frame))
    # loop_2 = right_column.after(50, lambda: animation(current_frame))


def gif_image():
    global right_column, photoimage_objects, photoimage_objects_2, gif_label, gif_label_2
    right_column = Frame(root, bg='gold2')
    right_column.place(anchor=NW, relx=0, rely=0, relheight=0.15, relwidth=1)

    photoimage_objects = []
    for i in range(frames):
        obj = PhotoImage(file=gif_file, format=f"gif -index {i}")
        photoimage_objects.append(obj)

    gif_label = Label(right_column, bg='gold2', image="")
    gif_label.place(x=80, y=0)

    animation(current_frame=0)


# Create the buttons and labels
def setup_widgets():
    global entry_Name, entry_ReceiptNumber, entry_ItemsNumber, delete_item, entry_ItemsPurchased, middle, bottom, button_pin
    # Main columns
    left_column = Frame(root)
    left_column.place(anchor=NW, relx=0, rely=0.15, relheight=0.85, relwidth=1)

    # Create two frames to sort out all the widgets: Top one:
    top = (Frame(left_column, bg='yellow'))
    top.place(anchor=NW, relheight=0.3, relwidth=1)
    # Create all the labels, buttons, and entry boxes. Put them in the correct grid location
    Label(top, text="Name", bg="orange", font=fontNum1).grid(column=0, row=0, padx=20, pady=25, sticky=W)
    Label(top, text="Items Hired", bg="orange", font=fontNum1).grid(column=0, row=1, padx=20, pady=25, sticky=W)
    Label(top, text="Receipt Number", bg="orange", font=fontNum1).grid(column=2, row=0, padx=20, pady=25, sticky=W)
    Button(top, text="Random Number", bg="tomato", bd=5, font=fontNum3, height=1, command=random_receipt).grid(column=5, row=0, pady=30, sticky='NW')
    Label(top, text="Items Number", bg="orange", font=fontNum1).grid(column=2, row=1, padx=20, pady=25, sticky=W)
    
    # Get purchase information from user input
    entry_Name = Entry(top, width=23)
    entry_Name.grid(column=1, row=0, sticky=W)
    entry_ReceiptNumber = Entry(top, width=23)
    entry_ReceiptNumber.grid(column=3, row=0, sticky=W)
    entry_ItemsNumber = Entry(top, width=23)
    entry_ItemsNumber.grid(column=3, row=1, sticky=W)

    # create combobox
    purchase_list = ['Tables', 'Balloons', 'Party Hats', 'Snacks', 'Drinks', 'Serving Bowls']
    entry_ItemsPurchased = Combobox(top, values=purchase_list, state='readonly')
    entry_ItemsPurchased.grid(column=1, row=1, sticky=W)
    entry_ItemsPurchased.set("Please choose an item name. ")


    # Middle Frame:
    middle = Frame(left_column, bg='orange')
    middle.place(relheight=0.3, relwidth=1, rely=0.3)
    button_pin = Button(middle, text="Pin Window", font=fontNum1, width=20, height=1, bg='SeaGreen3', bd=10,
                        relief='raised', command=pin_window, state='normal', compound=LEFT)
    button_pin.grid(column=0, row=0, padx=10, sticky='NW')
    Button(middle, text="Submit", font=fontNum1, width=190, height=60, bg='OliveDrab1', bd=10, relief='raised',
           image=button_image, compound=LEFT, command=check_inputs).grid(column=1, row=0, padx=10, sticky='NW')
    Button(middle, text="QUIT", fg='red', font=fontNum1, width=15, height=1, bg='yellow2', bd=10, relief='raised',
           command=quit).grid(column=2, row=0, padx=10, sticky='NW')
    Button(middle, text="Delete Row", font=fontNum1, height=1, width=19, command=delete_row, bg='red', bd=10).grid(
        column=0, row=1, padx=10, pady=12, sticky=W)
    delete_item = Entry(middle, width=23)
    delete_item.grid(column=1, row=1, sticky=W)


    # Create the column headings with color
    # Bottom Frame
    bottom = Frame(left_column, bg='IndianRed3')
    bottom.place(relheight=0.4, relwidth=1, rely=0.6)
    Label(bottom, font=fontNum1, text="Row", fg="white", bg="chocolate1", width=4, height=2, relief="ridge", bd=5).grid(
        column=0, row=0)
    Label(bottom, font=fontNum1, text="Name", fg="white", bg="chocolate1", width=18, height=2, relief="ridge", bd=5).grid(
        column=1, row=0)
    Label(bottom, font=fontNum1, text="Items Hired", fg="white", bg="chocolate1", width=20, height=2, relief="ridge",
          bd=5).grid(column=2, row=0)
    Label(bottom, font=fontNum1, text="Hired Amount", fg="white", bg="chocolate1", width=14, height=2, relief="ridge",
          bd=5).grid(column=3, row=0)
    Label(bottom, font=fontNum1, text="Receipt Number", fg="white", bg="chocolate1", width=14, height=2, relief="ridge",
          bd=5).grid(column=4, row=0)



def main():
    global root, fontNum1, fontNum2, fontNum3, fontNum4, button_image, quit_image, append_image, gif_file, gif_file_2,\
        info, info_2, frames, frames_2, bg_image
    root = Tk()
    root.geometry("750x1000")
    root.title("*" * 50 + "Party Purchase" + "*" * 50)
    root.configure(bg='lightblue')
    root.wm_attributes("-transparentcolor", "#add123")


    # Set the window icon
    icon_path = r"images/Linux_logo.png"  # Ensure you have an 'icon.png' file in the same directory
    icon = PhotoImage(file=icon_path)
    root.iconphoto(False, icon)

    # import gif image
    gif_file = r"images/giphy3.1.gif"
    info = Image.open(gif_file)
    frames = info.n_frames  # number of frames
    gif_image()

    # define fonts
    fontNum1 = tkFont.Font(family="Agency FB", size=20, weight="bold")
    fontNum2 = tkFont.Font(family="Agency FB", size=30, weight="bold")
    fontNum3 = tkFont.Font(family="Arial", size=11, weight="bold")
    fontNum4 = tkFont.Font(family="Cooper Black", size=18, weight='normal')

    #   import images
    button_image = PhotoImage(file=r"images/printer.png")
    quit_image = PhotoImage(file=r"images/quit button.png")
    append_image = PhotoImage(file=r"images/append.png")

    # Start the GUI
    setup_widgets()

    messagebox.showinfo(title="Tips(1/3):", message="To record purchases by using this program, input all the required"
                                                    " information, then click the button 'Append Details'. To print"
                                                    " the information, please click the button 'Print Details. ")
    messagebox.showinfo(title="Tips(2/3):", message="Having trouble with thinking about receipt numbers all day? "
                                                    "You can actually generate a random receipt number by click the"
                                                    " button 'Random Number' beside 'Receipt Number' entry box. ")
    messagebox.showinfo(title="Tip(3/3):", message="Need a help? You can check the instructions of this program by"
                                                   " clicking 'Help' in any time.")
    root.mainloop()


counters = {'total_entries': 0, 'name_count': 0}
Items_details = []


main()
