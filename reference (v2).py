import os
import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


# Quit subroutine
def quit_program():
    Main_win.destroy()


# Print details of all the items
def print_details():
    global detail_window
    try:
        detail_window.destroy()  # 如果窗口已经存在，先销毁它
    except:
        pass

    detail_window = Toplevel(Main_win)
    detail_window.title("All the items hired Details ")
    detail_window.iconphoto(False, icon)
    detail_window.geometry("600x600")
    detail_window.configure(bg="skyblue")

    name_count = 0
    # Create the column headings with color
    Label(detail_window, font=("Helvetica", 12, "bold"), text="Name", fg="white", bg="black", relief="sunken",
          bd=5).grid(column=1, row=0, padx=5, pady=5)
    Label(detail_window, font=("Helvetica", 12, "bold"), text="Items Hired Name", fg="white", bg="black",
          relief="ridge", bd=5).grid(column=2, row=0, padx=5, pady=5)
    Label(detail_window, font=("Helvetica", 12, "bold"), text="Total number of items hired", fg="white", bg="black",
          relief="groove", bd=5).grid(column=3, row=0, padx=5, pady=5)
    Label(detail_window, font=("Helvetica", 12, "bold"), text="Receipt Number", fg="white", bg="black", relief="raised",
          bd=5).grid(column=4, row=0, padx=5, pady=5)
    Label(detail_window, font=("Helvetica", 12, "bold"), text="Hire Days", fg="white", bg="black", relief="solid",
          bd=5).grid(column=5, row=0, padx=5, pady=5)
    # Add each item in the list into its own row
    for name_count, item in enumerate(item_details):
        Label(detail_window, text=item[0], relief="sunken", font=("Helvetica", 10), fg="blue", bg="white").grid(
            column=1, row=name_count + 1, padx=5, pady=5)
        Label(detail_window, text=item[1], relief="sunken", font=("Helvetica", 10), fg="blue", bg="white").grid(
            column=2, row=name_count + 1, padx=5, pady=5)
        Label(detail_window, text=item[2], relief="sunken", font=("Helvetica", 10), fg="blue", bg="white").grid(
            column=3, row=name_count + 1, padx=5, pady=5)
        Label(detail_window, text=item[3], relief="sunken", font=("Helvetica", 10), fg="blue", bg="white").grid(
            column=4, row=name_count + 1, padx=5, pady=5)
        Label(detail_window, text=item[4], relief="sunken", font=("Helvetica", 10), fg="blue", bg="white").grid(
            column=5, row=name_count + 1, padx=5, pady=5)
    counters['name_count'] = name_count


# Show error message in a popup window
def show_wrong_message(message):
    messagebox.showerror("Error", message)


# Check the inputs are all valid
def check_inputs():
    input_check = 0
    # Check that Name is not blank and only contains letters
    if len(entry_name.get()) == 0 or not entry_name.get().isalpha():
        show_wrong_message("Name is required and must only contain letters")
        input_check = 1
    # Check that Items Hired is not blank
    if len(entry_items_name.get()) == 0 or not entry_items_name.get().isalpha():
        show_wrong_message("Items Hired Name is required and must only contain letters")
        input_check = 1
    # Check that Total number of items hired is not blank and between 0 and 100
    if entry_items_number_need_hired.get().isdigit():
        if int(entry_items_number_need_hired.get()) <= 0 or int(entry_items_number_need_hired.get()) > 500:
            show_wrong_message(
                "Total number of items hired must be a positive number and cannot exceed 100 items or not less than and equal to 0")
            input_check = 1
    else:
        show_wrong_message("Total number of items hired is required and must be a positive number")
        input_check = 1

    # Check that Hire Days is not blank and a positive number
    if entry_hire_days.get().isdigit():
        if int(entry_hire_days.get()) <= 0:
            show_wrong_message("Hire days must be a positive number")
            input_check = 1
    else:
        show_wrong_message("Hire days is required and must be a positive number")
        input_check = 1

    if input_check == 0:
        append_item()
        receipt_number = item_details[-1][3]
        messagebox.showinfo("Receipt", f"Details appended successfully! Your receipt number is {receipt_number}")


# Generate a receipt number that is easy to remember
def give_receipt_NO():
    counters['receipt_counter'] += 1
    return f"{time.strftime('%d-%m-%Y')}-{counters['receipt_counter']:03d}"


# Add the next item to the list
def append_item():
    receipt_number = give_receipt_NO()
    item_details.append([entry_name.get(), entry_items_name.get(), entry_items_number_need_hired.get(), receipt_number,
                         entry_hire_days.get()])
    save_receit_in_file(receipt_number)
    # Clear the entry boxes
    entry_name.delete(0, 'end')
    entry_items_name.delete(0, 'end')
    entry_items_number_need_hired.delete(0, 'end')
    entry_hire_days.delete(0, 'end')
    counters['total_entries'] += 1


def save_receit_in_file(receipt_number):
    if not os.path.exists('receipts'):
        os.makedirs('receipts')
    with open(f'receipts/{receipt_number}.txt', 'w') as file:
        file.write(f"Name: {entry_name.get()}\n")
        file.write(f"Items Hired Name: {entry_items_name.get()}\n")
        file.write(f"Total number of items hired: {entry_items_number_need_hired.get()}\n")
        file.write(f"Hire Days: {entry_hire_days.get()}\n")
        file.write(f"Receipt Number: {receipt_number}\n")


def delete_receipt():
    receipt_number = delete_receipt_entry.get()
    for item in item_details:
        if item[3] == receipt_number:
            item_details.remove(item)
            counters['total_entries'] -= 1
            delete_receipt_file(receipt_number)
            delete_receipt_entry.delete(0, 'end')
            print_details()
            return
    show_wrong_message("Receipt number not found")


def delete_receipt_file(receipt_number):
    file_path = f'receipts/{receipt_number}.txt'
    if os.path.exists(file_path):
        os.remove(file_path)


# Delete all items
def delete_allitems():
    if item_details:
        item_details.clear()
        counters['total_entries'] = 0
        for receipt_file in os.listdir('receipts'):
            os.remove(os.path.join('receipts', receipt_file))
        print_details()
        messagebox.showinfo("Info", "All hired items have been deleted.")
    else:
        show_wrong_message("Can Not find items that need to delete.")


# Show history of a receipt number
def History():
    history_window = Toplevel(Main_win)
    history_window.title("Show History")
    history_window.iconphoto(False, icon)
    history_window.geometry("500x300")
    history_window.configure(bg="lightgoldenrodyellow")

    Label(history_window, text="Receipt Number", fg='black', bg="gold1", relief="solid", bd=2).grid(column=0, row=0,
                                                                                                    padx=25, pady=25,
                                                                                                    sticky=E)
    global entry_receipt_search
    entry_receipt_search = Entry(history_window)
    entry_receipt_search.grid(column=1, row=0)
    Button(history_window, text="Search", fg='brown', bg="orange", relief="ridge", bd=4, command=search_receipt,
           width=15).grid(column=1, row=1, padx=20, pady=20)


def search_receipt():
    receipt_number = entry_receipt_search.get()
    file_path = f'receipts/{receipt_number}.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            history_content = file.read()
        Show_内容_receipt(history_content)
    else:
        show_wrong_message("Receipt not exist")


def Show_内容_receipt(content):
    content_window = Toplevel(Main_win)
    content_window.title("Receipt Content")
    content_window.iconphoto(False, icon)
    content_window.geometry("500x300")

    text = Text(content_window)
    text.insert(1.0, content)
    text.config(state=DISABLED)
    text.pack(expand=1, fill=BOTH)


# Create the main page buttons and labels
def setup_main_buttons(button_frame):
    Button(button_frame, font='System', text="Append Details", fg='blue', bg='lightblue', relief='raised', bd=7,
           command=appenditems_page, width=15).grid(column=0, row=0, padx=17, pady=17)
    Button(button_frame, font='System', text="Delete Details", fg='red', bg='lightblue', relief='raised', bd=7,
           command=return_page, width=15).grid(column=0, row=1, padx=17, pady=17)
    Button(button_frame, font='System', text="Print All Items Details", fg='darkgreen', bg='lightblue', relief='raised',
           bd=7, command=print_details, width=17).grid(column=1, row=0, padx=15, pady=15)
    Button(button_frame, font='System', text="Search Hired Items", fg='darkgoldenrod4', bg='lightblue', relief='raised',
           bd=7, command=History, width=17).grid(column=1, row=1, padx=15, pady=15)
    Button(button_frame, font='System', text="Quit", fg='white', bg='red', relief='raised', bd=5, command=quit_program,
           width=9).grid(column=2, row=0, padx=15, pady=15)
    Button(button_frame, font='System', text="Instruction", fg='white', bg='Gold', relief='raised', bd=5,
           command=instruction_page, width=9).grid(column=2, row=1, padx=15, pady=15)


def instruction_page():
    intro_window = Toplevel(Main_win)
    intro_window.title("_John's Item Hire Program")
    intro_window.iconphoto(False, icon)
    intro_window.geometry("530x420")

    intro_window.configure(bg="white")

    # 创建一个框架来放置 Text 和 Scrollbar
    frame = Frame(intro_window)
    frame.pack(fill=BOTH, expand=True)

    # 创建 Text 小部件
    text_widget = Text(frame, wrap=WORD, state=DISABLED)
    text_widget.pack(side=LEFT, fill=BOTH, expand=True)

    # 创建 Scrollbar 小部件
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=text_widget.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # 配置 Text 小部件的 yscrollcommand，使其与 Scrollbar 关联
    text_widget.config(yscrollcommand=scrollbar.set)
    text_widget.pack(pady=25)

    # 在 Text 小部件的末尾插入文本
    text_widget.config(state='normal')
    text_widget.insert(END, "This is an example of how to use the wrap and END options in Tkinter's Text widget.\n")
    text_widget.insert(END, "The text will wrap at word boundaries to ensure it doesn't break in the middle of a word.")
    text_widget.config(state=DISABLED)


def appenditems_page():
    add_details_window = Toplevel(Main_win)
    add_details_window.title("_John's Party Hire Program")
    add_details_window.iconphoto(False, icon)
    add_details_window.geometry("530x440")

    # bg_image = PhotoImage(file=r"output-onlinepngtools (2).png")
    bg_image = PhotoImage(file=r"party_image.png")
    bg_label = Label(add_details_window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(add_details_window, text="Name", font=("Aial", 10), fg='white', bg="green", relief='groove', bd=4).grid(
        column=0, row=0, padx=30, pady=30, sticky=E)
    Label(add_details_window, text="Items Hired Name", font=("Aial", 10), fg='white', bg='green', relief='groove',
          bd=4).grid(column=0, row=1, padx=30, pady=30, sticky=E)
    Label(add_details_window, text="Total number of items hired", font=("Aial", 10), fg='white', bg="green",
          relief='groove', bd=4).grid(column=0, row=2, padx=30, pady=30, sticky=E)
    Label(add_details_window, text="Hire Days", font=("Aial", 10), fg='white', bg="green", relief='groove', bd=4).grid(
        column=0, row=3, padx=30, pady=30, sticky=E)

    global entry_name, entry_items_name, entry_items_number_need_hired, entry_hire_days, append_image
    entry_name = Entry(add_details_window)
    entry_name.grid(column=1, row=0)

    # 创建组合框（Combobox）以取代文本输入框
    items_list = ["Table", "Bench", "Chair", 'Glass']
    entry_items_name = Combobox(add_details_window, values=items_list)
    entry_items_name.set("Pick or Input item name")
    entry_items_name.grid(column=1, row=1)

    entry_items_number_need_hired = Entry(add_details_window)
    entry_items_number_need_hired.grid(column=1, row=2)
    entry_hire_days = Entry(add_details_window)
    entry_hire_days.grid(column=1, row=3)

    # Load image for the button
    append_image = PhotoImage(file=r"Linux_logo.png")
    append_button = Button(add_details_window, text="Append Details", font=("Aial", 10), fg='blue', bg='lightgreen',
                           relief='ridge', bd=7, command=check_inputs, width=145, image=append_image, compound="right")
    append_button.grid(column=1, row=5, padx=20, pady=20)

    # Keep a reference to the images to prevent garbage collection
    add_details_window.bg_image = bg_image
    add_details_window.append_image = append_image


def return_page():
    delete_details_window = Toplevel(Main_win)
    delete_details_window.title("Delete Details")
    delete_details_window.iconphoto(False, icon)
    delete_details_window.geometry("500x400")

    bg_image = PhotoImage(file=r"party_image.png")
    bg_label = Label(delete_details_window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(delete_details_window, text="Receipt Number", fg='red', bg='orange', relief='flat', bd=3).grid(column=0,
                                                                                                         row=0, padx=22,
                                                                                                         pady=22,
                                                                                                         sticky=E)

    global delete_receipt_entry
    delete_receipt_entry = Entry(delete_details_window)
    delete_receipt_entry.grid(column=1, row=0)

    Button(delete_details_window, text="Delete Receipt", fg='red', bg='pink', relief='ridge', bd=3,
           command=delete_receipt, width=13).grid(column=2, row=0, padx=18, pady=18)
    Button(delete_details_window, text="Delete All Hired Items", fg='red', bg='pink', relief='ridge', bd=3,
           command=delete_allitems, width=18).grid(column=1, row=1, padx=18, pady=18)

    delete_details_window.bg_image = bg_image


# Start the program running
def main():
    global Main_win, icon
    Main_win = Tk()
    Main_win.geometry("500x550")
    Main_win.title("John's Item Hire Program")

    icon_path = r"Linux_logo.png"
    icon = PhotoImage(file=icon_path)
    Main_win.iconphoto(False, icon)

    # Create a frame for the top half with background image
    top_frame = Frame(Main_win, height=380, width=500)
    top_frame.grid(row=0, column=0, sticky="nsew")
    top_frame.grid_propagate(False)

    bg_image = PhotoImage(file=r"Linux_logo.png")
    bg_label = Label(top_frame, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a frame for the buttons in the bottom half
    button_frame = Frame(Main_win, height=175, width=490, bg='navy')
    button_frame.grid(row=1, column=0, sticky="nsew")
    button_frame.grid_propagate(False)

    setup_main_buttons(button_frame)

    Main_win.mainloop()


# Create empty list for item details and counters for entries in the list
counters = {'total_entries': 0, 'name_count': 0, 'receipt_counter': 0}
item_details = []

main()