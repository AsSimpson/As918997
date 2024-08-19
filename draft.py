from tkinter import *
from PIL import Image

root = Tk()
root.title("Displaying Gif")
root.geometry("1000x500")
root.configure(bg="lightblue")

# left_column = Frame(root, bg='black')
# left_column.place(relx=0, relwidth=0.5, relheight=1)


def gif_image():

    right_column = Frame(root)
    right_column.place(relx=0.5, relwidth=0.5, relheight=1)
    gif_file = r'firework.gif'
    info = Image.open(gif_file)

    frames = info.n_frames  # number of frames

    photoimage_objects = []
    for i in range(frames):
        obj = PhotoImage(file=gif_file, format=f"gif -index {i}")
        photoimage_objects.append(obj)


    def animation(current_frame=0):
        global loop
        image = photoimage_objects[current_frame]

        gif_label.configure(image=image)
        current_frame = current_frame + 1

        if current_frame == frames:
            current_frame = 0

        loop = right_column.after(50, lambda: animation(current_frame))



    gif_label = Label(right_column, image="")
    gif_label.pack()

    animation(current_frame=0)

gif_image()

root.mainloop()


