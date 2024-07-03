from tkinter import *
import random


def quit():
    main_window.destroy()


def generate_random():
    random_number1 = random.randint(1, 10)
    Label(main_window, text=random_number1).grid(column=0, row=1, sticky=E)
    if random_number1 == 6:
        print("We got 6 on left side. ")

    random_number2 = random.randint(1, 10)
    Label(main_window, text=random_number2) .grid(column=1, row=1, sticky=E)
    if random_number2 == 6:
        print("We got 6 on right side. ")


def main():
    Button(main_window, text="Quit", command=quit, width=10)  .grid(column=0, row=0)
    Button(main_window, text="Random", command=generate_random, width=10)  .grid(column=1, row=0)
    main_window.mainloop()


main_window = Tk()
main()
