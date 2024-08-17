from tkinter import *

root = Tk()
root.title("Simpson's Practice")
root.geometry("800x240")

bg = PhotoImage(file=r'party_image.png')

# create a label
my_label = Label(root, image=bg)
my_label.place(x=0,y=0, relwidth=1, relheight=1)

# add something to the top of our image
my_text = Label(root, text="Welcome!")
my_text.pack()

my_frame = Frame(root)
my_frame.pack()

my_button1 = Button(my_frame, text="Exit").grid(column=0, row=0, padx=20)
my_button2 = Button(my_frame, text="Start").grid(column=1, row=0, padx=20)
my_button3 = Button(my_frame, text="Reset").grid(column=2, row=0, padx=20)

root.mainloop()
