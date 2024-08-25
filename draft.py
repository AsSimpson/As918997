#Import the required libraries
from tkinter import *

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of Tkinter Frame
win.geometry("700x250")
def error_fix(widget_name):
   #Define a function to clear the content of the text widget
   def click(event):
      widget_name.configure(state=NORMAL)
      widget_name.delete(0, END)
      widget_name.configure(bg="white")
      widget_name.unbind('<Button-1>', clicked)
   
   #Create a Label widget
   label = Label(win, text= "Enter Your Name", font= ('Helvetica 13 bold'))
   label.pack(pady= 10)
   
   #Create an Entry widget
   widget_name = Entry(win, width=45)
   widget_name.insert(0, 'Enter Your Name Here...')
   widget_name.pack(pady=10)
   widget_name.configure(bg="red")
   
   #Bind the Entry widget with Mouse Button to clear the content
   clicked = widget_name.bind('<Button-1>', click)
error_fix("trial")
win.mainloop()