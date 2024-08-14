import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Image Button Demo')


# download button handler
def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
    )


download_icon = tk.PhotoImage(file=r'printer.png')

download_button = ttk.Button(
    root,
    image=download_icon,
    text='Download the Content',
    compound=tk.LEFT,
    command=download_clicked
)

tk.Label(text="    ").grid(row=0, column=0)
tk.Label(text="    ").grid(row=1, column=0)
tk.Label(text="    ").grid(row=0, column=1)
tk.Label(text="    ").grid(row=0, column=2)
tk.Label(text="    ").grid(row=0, column=3)
download_button.grid(row=2, column=4)


root.mainloop()