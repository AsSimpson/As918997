import tkinter as tk
window =tk.Tk()
window.title('my window')
window.geometry('200x200')

var1=tk.StringVar()
l=tk.Label(window,bg='yellow',width=4,textvariable=var1)
l.pack()

def print_seletion():
    value=lb.get(lb.curselection())
    var1.set(value)
b1=tk.Button(window,text='insert point',width=15,height=2,command=print_seletion)
b1.pack()

var2=tk.StringVar()
var2.set((11,4,5,14))
lb=tk.Listbox(window,listvariable=var2)
list_items=[1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'frist')
lb.insert(2,'second')
lb.delete(2)
lb.pack()

window.mainloop()