import os
import random
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image
from Simpson_library import GradientFrame

def show_error(object_name):
    # Define a function to clear the content of the text widget
    def click(event):
        object_name.delete(0, END)
        object_name.configure(bg="white")
        object_name.unbind('<Button-1>', clicked)
    object_name.configure(bg="firebrick1")
    clicked = object_name.bind('<Button-1>', click)

# Check if the inputs are valid
def check_inputs():
    input_check = 0

    # Check if Name is blank, set error text if blank
    if len(entry_Name.get()) ==0 or len(entry_Name.get()) > 10 or not entry_Name.get().isalpha():
        show_error(entry_Name)
        messagebox.showerror(title="error", message="Name required, name must be consisted by letters and less than 10 letters")
        input_check = 1
    # Check if the combobox is still in default
    if entry_ItemsPurchased.get() == "Please choose an item name. ":
        messagebox.showerror(title="error", message="Choose a PURCHASED ITEM NAME please. ")
        input_check = 1
    # Check the validation of receipt number(range: 0-2000 include 0 & 2000)
    if entry_ReceiptNumber.get().isdigit():
        if int(entry_ReceiptNumber.get()) <= 0 or int(entry_ReceiptNumber.get()) >= 2000:
            show_error(entry_ReceiptNumber)
            messagebox.showerror(title="error", message="Input a valid RECEIPT NUMBER please. The receipt number should "
                                                        "be a integer which greater that 0, less than 2001. ")
            input_check = 1
    else:
        show_error(entry_ReceiptNumber)
        messagebox.showerror(title="error", message="RECEIPT NUMBER should be an integer. ")
        input_check = 1
    # Check that Items Number is not blank and between 0 and 30, set error text if invalid
    if entry_ItemsNumber.get().isdigit():
        if int(entry_ItemsNumber.get()) <= 0 or int(entry_ItemsNumber.get()) > 100:
            show_error(entry_ItemsNumber)
            messagebox.showerror(title="error", message="RECEIPT NUMBER should be a integer which greater than 0, less than 101. ")
            input_check = 1
    else:
        show_error(entry_ItemsNumber)
        messagebox.showerror(title="error", message="Input a valid RECEIPT NUMBER please. ")
        input_check = 1

    if input_check == 0:
        messagebox.showinfo("Receipt", f"Details appended successfully! Your receipt number is {str(entry_ReceiptNumber.get())}")
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

    loop = title_frame.after(50, lambda: animation(current_frame))
    # loop_2 = title_frame.after(50, lambda: animation(current_frame))


def gif_image():
    global title_frame, photoimage_objects, photoimage_objects_2, gif_label, gif_label_2
    title_frame = Frame(main_f, bg='gold2')
    title_frame.place(anchor=NW, relx=0, rely=0, relheight=0.25, relwidth=1)

    photoimage_objects = []
    for i in range(frames):
        obj = PhotoImage(file=gif_file, format=f"gif -index {i}")
        photoimage_objects.append(obj)

    gif_label = Label(title_frame, bg='gold2', image="")
    gif_label.place(x=70, y=0)

    animation(current_frame=0)


def receipt_window():
    global receipt_win, bottom
    try:
        receipt_win.destroy()
    except:
        pass
        
    receipt_win = Toplevel(root)
    receipt_win.geometry("750x670")
    receipt_win.title("Purchase Details Window")
    receipt_win.iconphoto(False, icon)
    receipt_win.configure(bg='IndianRed3')
    
    name_count = 0
    # Create the column headings with color
    # Bottom Frame
    bottom = Frame(receipt_win, bg='IndianRed3')
    bottom.place(relheight=1, relwidth=1, rely=0)
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

    # Add each item in the list into its own row
    for name_count, item in enumerate(Items_details):
        Label(bottom, text=(name_count + 1), relief="sunken", font=fontNum1, fg="black", bg="white").grid(
            column=0, row=name_count + 1, padx=5, pady=5)
        Label(bottom, text=item[0], relief="sunken", font=fontNum1, fg="black", bg="white").grid(
            column=1, row=name_count + 1, padx=5, pady=5)
        Label(bottom, text=item[1], relief="sunken", font=fontNum1, fg="black", bg="white").grid(
            column=2, row=name_count + 1, padx=5, pady=5)
        Label(bottom, text=item[2], relief="sunken", font=fontNum1, fg="black", bg="white").grid(
            column=3, row=name_count + 1, padx=5, pady=5)
        Label(bottom, text=item[3], relief="sunken", font=fontNum1, fg="black", bg="white").grid(
            column=4, row=name_count + 1, padx=5, pady=5)
    counters['name_count'] = name_count

# Create the buttons and labels
def setup_widgets():
    global entry_Name, entry_ReceiptNumber, entry_ItemsNumber, delete_item, entry_ItemsPurchased, middle, bottom,\
        button_pin, main_f
    # Main columns
    main_f = Frame(root)
    main_f.place(anchor=NW, relx=0, rely=0, relheight=1, relwidth=1)

    # Create two frames to sort out all the widgets: Top one:
    top = (Frame(main_f, bg='yellow'))
    top.place(anchor=NW, rely=0.25, relheight=0.35, relwidth=1)
    # Create all the labels, buttons, and entry boxes. Put them in the correct grid location
    Label(top, text="Name", bg="orange", font=fontNum1).grid(column=0, row=0, padx=20, pady=25, sticky=W)
    Label(top, text="Items Hired", bg="orange", font=fontNum1).grid(column=0, row=1, padx=20, pady=25, sticky=W)
    Label(top, text="Receipt Number", bg="orange", font=fontNum1).grid(column=2, row=0, padx=20, pady=25, sticky=W)
    Button(top, text="Random Number", bg="tomato", bd=5, font=fontNum3, height=1, command=random_receipt).grid(column=5, row=0, pady=30, sticky='NW')
    Label(top, text="Hired Amount", bg="orange", font=fontNum1).grid(column=2, row=1, padx=20, pady=25, sticky=W)
    
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
    middle = Frame(main_f, bg='orange')
    middle.place(relheight=0.4, relwidth=1, rely=0.6)
    button_pin = Button(middle, text="Pin Window", font=fontNum1, width=20, height=1, bg='SeaGreen3', bd=10,
                        relief='raised', command=pin_window, state='normal', compound=LEFT)
    button_pin.grid(column=0, row=0, padx=10, sticky='NW')
    Button(middle, text="Submit", font=fontNum1, width=200, height=60, bg='OliveDrab1', bd=10, relief='raised',
           image=button_image, compound=LEFT, command=check_inputs).grid(column=1, row=0, padx=20, sticky='NW')
    Button(middle, text="QUIT", fg='red', font=fontNum1, width=20, height=1, bg='yellow2', bd=10, relief='raised',
           command=quit).grid(column=2, row=0, padx=10, sticky='NW')
    Button(middle, text="Delete Row", font=fontNum1, height=1, width=20, command=delete_row, bg='red', bd=10).grid(
        column=0, row=1, padx=10, pady=12, sticky=W)
    delete_item = Entry(middle, width=23)
    delete_item.grid(column=1, row=1, sticky=W)
    Button(middle, text="Print Details", font=fontNum1, height=1, width=20, bg='PaleGreen2', bd=10, relief='raised',
           command=receipt_window).grid(column=2, row=1, padx=10, pady=12)



def main():
    global root, fontNum1, fontNum2, fontNum3, fontNum4, button_image, quit_image, append_image, gif_file, gif_file_2,\
        info, info_2, frames, frames_2, bg_image, icon
    root = Tk()
    root.geometry("750x650")
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
    gif_image()

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
