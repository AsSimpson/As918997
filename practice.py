import tkinter as tk
# create a desktop window whose size is '200x200'
window =tk.Tk()
window.title('my window')
window.geometry('200x200')

# create a label for print_selection
l=tk.Label(window,bg='yellow',width=20)
l.pack()

# define a function to print the outcome
def print_selection(v):
    l.config(text='You have selected ' + v)

# add scale widget
s = tk.Scale(window,label='try me', from_=5, to=11,orient=tk.HORIZONTAL,length=200,
             showvalue=0,tickinterval=3,resolution=0.01,command=print_selection)
s.pack()

# refresh the program when it is over
window.mainloop()