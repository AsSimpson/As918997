import tkinter as tk
# create a desktop window whose size is '200x200'
window =tk.Tk()
window.title('my window')
window.geometry('200x200')

# define a string var named 'var1' and attach it to the label 'l'
var=tk.StringVar()
l=tk.Label(window,bg='yellow',width=20)
l.pack()

def print_selection():
    l.config(text='You have selected ' + var.get())

# create 3 radio button named 'r1', 'r2', 'r3'
r1 = tk.Radiobutton(window, text = 'Option A', variable=var, value='A', command = print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text = 'Option B', variable=var, value='B', command = print_selection)
r2.pack()

r3 = tk.Radiobutton(window, text = 'Option C', variable=var, value='C', command = print_selection)
r3.pack()

# refresh the program when it is over
window.mainloop()