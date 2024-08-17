# Import the required libraries
from tkinter import *
from tkinter import ttk


def new_window():
    Toplevel(win).title(str(counters['name_count']))
    counters['name_count'] += 1


# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

counters = {'total_entries': 1, 'name_count': 1}

# Add a Frame
frame1= Frame(win, bg="LightPink1")

# Add an optional Label widget
Label(frame1, text="Welcome Folks!", font=('Aerial 18 bold italic'), background="white").grid(column=0, row=0)
frame1.pack(pady=10)

# Add a Button widget in second frame
ttk.Button(frame1, text="New Window", command=new_window).grid(column=0, row=1)

win.mainloop()
