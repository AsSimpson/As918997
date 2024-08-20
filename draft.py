from tkinter import *
import tkinter.scrolledtext as st

root = Tk()
root.title("ScrolledText Widget")

entry_set = []

def scrolled_receipt():
    def submit_entry():
        receipt_area.configure(state='normal')
        receipt_area.insert(END, f"{insert_entry1.get()}\t")
        receipt_area.insert(END, f"{insert_entry2.get()}\t")
        receipt_area.insert(END, f"{insert_entry3.get()}\t")
        receipt_area.insert(END, f"{insert_entry4.get()}\n")
        insert_entry1.delete(0, "end")
        insert_entry2.delete(0, "end")
        insert_entry3.delete(0, "end")
        insert_entry4.delete(0, "end")
        receipt_area.configure(state='disabled')

    insert_entry1 = Entry(width=50)
    insert_entry1.grid(row=0)

    insert_entry2 = Entry(width=50)
    insert_entry2.grid(row=2)

    insert_entry3 = Entry(width=50)
    insert_entry3.grid(row=3)

    insert_entry4 = Entry(width=50)
    insert_entry4.grid(row=4)

    entry_set.append([insert_entry1.get(), insert_entry2.get(), insert_entry3.get(), insert_entry4.get()])

    button_insert = Button(text="Submit", command=submit_entry)
    button_insert.grid(row=5)

    # Creating scrolled text area

    receipt_area = st.ScrolledText(root, width=150, height=8, font=("Times New Roman", 15))

    receipt_area.grid(column=0, row=7, pady=10, padx=10)

    # widget with Read only by disabling the state
    receipt_area.configure(state='disabled')


scrolled_receipt()

root.mainloop()
