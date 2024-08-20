import os
from tkinter import *

def viewFile():
    path = os.path.expanduser("~/python")
    for f in os.listdir(path):
        tex.insert(END, f + "\n")

if __name__ == '__main__':
    root = Tk()

    step= root.attributes('-fullscreen', True)
    step = LabelFrame(root, text="FILE MANAGER", font="Arial 20 bold italic")
    step.grid(row=0, columnspan=7, sticky='W', padx=100, pady=5, ipadx=130, ipady=25)

    Button(step, text="File View", font="Arial 8 bold italic", activebackground=
           "turquoise", width=30, height=5, command=viewFile).grid(row=1, column=2)
    Button(step, text="Quit", font="Arial 8 bold italic", activebackground=
           "turquoise", width=20, height=5, command=root.quit).grid(row=1, column=5)

    tex = Text(master=root)
    scr=Scrollbar(root, orient=VERTICAL, command=tex.yview)
    scr.grid(row=2, column=2, rowspan=15, columnspan=1, sticky=NS)
    tex.grid(row=2, column=1, sticky=W)
    tex.config(yscrollcommand=scr.set, font=('Arial', 8, 'bold', 'italic'))

    root.mainloop()