import tkinter as tk
# create a desktop window whose size is '200x200'
window =tk.Tk()
window.title('my window')
window.geometry('200x200')

# define a string var named 'var1' and attach it to the label 'l'
var1=tk.StringVar()
l=tk.Label(window,bg='yellow',width=4,textvariable=var1)
l.pack()

# define a function
def print_seletion():
    value=lb.get(lb.curselection())
    var1.set(value)

# create a button and attach the function define before to it
b1=tk.Button(window,text='insert point',width=15,height=2,command=print_seletion)
b1.pack()

# define a string variable 'var2' set its value as a set
var2=tk.StringVar()
var2.set((11,4,5,14))

# create a list to hold set 'var2'
lb=tk.Listbox(window,listvariable=var2)
# set down the arrangement in the list
list_items=[1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'frist')
lb.insert(2,'second')
lb.delete(2)
lb.pack()

# refresh the program when it is over
window.mainloop()