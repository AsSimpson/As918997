import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.geometry("500x300")
# Create fonts with different weights and slants
normal_font = tkFont.Font(family="Agency FB", size=40, weight=tkFont.NORMAL)

# Create labels using different font styles
label = tk.Label(root, text="Normal Text", font=normal_font)
label.pack()

root.mainloop()
