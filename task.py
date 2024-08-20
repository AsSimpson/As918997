from tkinter import *
import random


def quit():
    main_window.destroy()


def generate_random():
    bg_colour = "red"

    # random number 1
    random_number1 = random.randint(1, 10)
    # random number2
    random_number2 = random.randint(1, 10)

    if random_number1 == 6 or random_number2 == 6:
        bg_colour = "green"
    # create labels
    Label(main_window, text=random_number1, bg=bg_colour, width=10).grid(column=0, row=1, sticky=E)
    Label(main_window, text=random_number2, bg=bg_colour, width=10).grid(column=1, row=1, sticky=E)

    if random_number1 == 6 or random_number2 == 6:
        bg_colour = "green"
        print("We got 6. ")


def main():
    Button(main_window, text="Quit", command=quit, width=10).grid(column=0, row=0)
    Button(main_window, text="Random", command=generate_random, width=10).grid(column=1, row=0)
    main_window.mainloop()


main_window = Tk()
main()
