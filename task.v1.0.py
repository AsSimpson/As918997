from tkinter import *
import random


def quit():
    main_window.destroy()


def generate_random():
    bg_colour1 = "red"
    bg_colour2 = "red"
    # random number 1
    random_number1 = random.randint(1, 10)
    if random_number1 == 6:
        bg_colour1 = "yellow"
        print("We got 6 on left side. ")
    Label(main_window, text=random_number1, bg=bg_colour1, width=11).grid(column=0, row=1, sticky=E)

    # random number2
    random_number2 = random.randint(1, 10)
    if random_number2 == 6:
        bg_colour2 = "yellow"
        print("We got 6 on right side. ")
    Label(main_window, text=random_number2, bg=bg_colour2, width=11).grid(column=1, row=1, sticky=E)


def main():
    Button(main_window, text="Quit", command=quit, width=10).grid(column=0, row=0)
    Button(main_window, text="Random", command=generate_random, width=10).grid(column=1, row=0)
    main_window.mainloop()


main_window = Tk()
main()
