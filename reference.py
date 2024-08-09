from tkinter import *
import os


# Quit subroutine
def quit():
    main_window.destroy()


# Print details of all the items
def print_items_details():
    name_count = 0
    # Create the column headings with color
    Label(main_window, font=("Helvetica", 12, "bold"), text="Row", fg="white", bg="black", relief="solid", bd=5).grid(
        column=0, row=7, padx=5, pady=5)
    Label(main_window, font=("Helvetica", 12, "bold"), text="Name", fg="white", bg="black", relief="sunken", bd=5).grid(
        column=1, row=7, padx=5, pady=5)
    Label(main_window, font=("Helvetica", 12, "bold"), text="Items Hired", fg="white", bg="black", relief="ridge",
          bd=5).grid(column=2, row=7, padx=5, pady=5)
    Label(main_window, font=("Helvetica", 12, "bold"), text="Receipt Number", fg="white", bg="black", relief="groove",
          bd=5).grid(column=3, row=7, padx=5, pady=5)
    Label(main_window, font=("Helvetica", 12, "bold"), text="Items Hired", fg="white", bg="black", relief="raised",
          bd=5).grid(column=4, row=7, padx=5, pady=5)
    # Add each item in the list into its own row
    while name_count < counters['total_entries']:
        Label(main_window, text=name_count, relief="sunken", font=("Helvetica", 10), fg="blue", bg="white").grid(
            column=0, row=name_count + 8, padx=5, pady=5)
        Label(main_window, text=(Items_details[name_count][0]), relief="sunken", font=("Helvetica", 10), fg="blue",
              bg="white").grid(column=1, row=name_count + 8, padx=5, pady=5)
        Label(main_window, text=(Items_details[name_count][1]), relief="sunken", font=("Helvetica", 10), fg="blue",
              bg="white").grid(column=2, row=name_count + 8, padx=5, pady=5)
        Label(main_window, text=(Items_details[name_count][2]), relief="sunken", font=("Helvetica", 10), fg="blue",
              bg="white").grid(column=3, row=name_count + 8, padx=5, pady=5)
        Label(main_window, text=(Items_details[name_count][3]), relief="sunken", font=("Helvetica", 10), fg="blue",
              bg="white").grid(column=4, row=name_count + 8, padx=5, pady=5)
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
        error_labels[0] = Label(main_window, fg="red", text="Required")
        error_labels[0].grid(column=2, row=0)
        input_check = 1
    # Check that Items Hired is not blank, set error text if blank
    if len(entry_ItemsHired.get()) == 0:
        error_labels[1] = Label(main_window, fg="red", text="Required")
        error_labels[1].grid(column=2, row=1)
        input_check = 1
    # Check that Receipt Number is not blank and between 2 and 15, set error text if invalid
    if entry_ReciptNumber.get().isdigit():
        if int(entry_ReciptNumber.get()) < 2 or int(entry_ReciptNumber.get()) > 15:
            error_labels[2] = Label(main_window, fg="red", text="Invalid number")
            error_labels[2].grid(column=2, row=2)
            input_check = 1
    else:
        error_labels[2] = Label(main_window, fg="red", text="Numbers only")
        error_labels[2].grid(column=2, row=2)
        input_check = 1
    # Check that Items Number is not blank and between 0 and 30, set error text if invalid
    if entry_ItemsNumber.get().isdigit():
        if int(entry_ItemsNumber.get()) < 0 or int(entry_ItemsNumber.get()) > 30:
            error_labels[3] = Label(main_window, fg="red", text="Invalid number")
            error_labels[3].grid(column=2, row=3)
            input_check = 1
    else:
        error_labels[3] = Label(main_window, fg="red", text="Numbers only")
        error_labels[3].grid(column=2, row=3)
        input_check = 1

    if input_check == 0:
        append_item()


def clear_error_messages():
    # Clear all error messages
    for label in error_labels:
        if label:
            label.destroy()


# Add the next item to the list


def append_item():
    # Append each item to its own area of the list
    Items_details.append([entry_Name.get(), entry_ItemsHired.get(), entry_ReciptNumber.get(), entry_ItemsNumber.get()])
    save_receipt_to_file(entry_ReciptNumber.get())
    # Clear the entry boxes
    entry_Name.delete(0, 'end')
    entry_ItemsHired.delete(0, 'end')
    entry_ReciptNumber.delete(0, 'end')
    entry_ItemsNumber.delete(0, 'end')
    counters['total_entries'] += 1


def save_receipt_to_file(receipt_number):
    if not os.path.exists('receipts'):
        os.makedirs('receipts')
    with open(f'receipts/{receipt_number}.txt', 'w') as file:
        file.write(f"Name: {entry_Name.get()}\n")
        file.write(f"Items Hired: {entry_ItemsHired.get()}\n")
        file.write(f"Receipt Number: {entry_ReciptNumber.get()}\n")
        file.write(f"Items Number: {entry_ItemsNumber.get()}\n")


# Delete a row from the list
def delete_row():
    row_index = int(delete_item.get())
    if 0 <= row_index < counters['total_entries']:
        delete_receipt_file(Items_details[row_index][2])
        del Items_details[row_index]
        counters['total_entries'] -= 1
        name_count = counters['name_count']
        delete_item.delete(0, 'end')
        # Clear the last item displayed on the GUI
        Label(main_window, text="       ").grid(column=0, row=name_count + 7)
        Label(main_window, text="       ").grid(column=1, row=name_count + 7)
        Label(main_window, text="       ").grid(column=2, row=name_count + 7)
        Label(main_window, text="       ").grid(column=3, row=name_count + 7)
        Label(main_window, text="       ").grid(column=4, row=name_count + 7)
        # Print all the items in the list
        print_items_details()


def delete_receipt_file(receipt_number):
    file_path = f'receipts/{receipt_number}.txt'
    if os.path.exists(file_path):
        os.remove(file_path)


# Create the buttons and labels
def setup_buttons():
    # Create all the labels, buttons, and entry boxes. Put them in the correct grid location
    Label(main_window, text="Name", bg="lightblue").grid(column=0, row=0, padx=20, pady=20, sticky=E)
    Label(main_window, text="Items Hired", bg="lightblue").grid(column=0, row=1, padx=20, pady=12, sticky=E)
    Button(main_window, text="Quit", command=quit, width=10).grid(column=4, row=0, padx=20, pady=12, sticky=E)
    Button(main_window, text="Append Details", command=check_inputs).grid(column=3, row=1, padx=12, pady=12)
    Button(main_window, text="Print Details", command=print_items_details, width=10).grid(column=4, row=1, padx=20,
                                                                                          pady=12, sticky=E)
    Label(main_window, text="Receipt Number", bg="lightblue").grid(column=0, row=2, padx=20, pady=12, sticky=E)
    Label(main_window, text="Items Number", bg="lightblue").grid(column=0, row=3, padx=20, pady=12, sticky=E)
    Label(main_window, text="Row #", bg="lightgray").grid(column=3, row=2, padx=20, pady=20, sticky=E)
    Button(main_window, text="Delete Row", command=delete_row, width=10).grid(column=4, row=3, padx=20, pady=12,
                                                                              sticky=E)
    Label(main_window, text="               ").grid(column=2, row=0)


# Start the program running
def main():
    main_window.geometry("780x400")
    main_window.title("*" * 50 + "John's Item Hire Program" + "*" * 50)
    # Set the window icon
    icon_path = "D:\OneDrive\Pictures\Saved Pictures\png format\WallpaperEngineLockOverride_randomAQSNXO.png"  # Ensure you have an 'icon.png' file in the same directory
    icon = PhotoImage(file=icon_path)
    main_window.iconphoto(False, icon)
    # Start the GUI
    setup_buttons()
    main_window.mainloop()


# Create empty list for item details and counters for entries in the list
counters = {'total_entries': 0, 'name_count': 0}
Items_details = []
error_labels = [None] * 4
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