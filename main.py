import os
import tkinter
from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk

if __name__ == '__main__':
    root = Tk()
    root.title('Image Viewer')
    root.geometry('1420x780')
    frame1 = Canvas(root, width=1420, height=780)
    frame1.pack()
    frame_background = PhotoImage(file="Screenshot 2022-11-12 135956.png")
    frame1.create_image(960, 390, anchor=CENTER, image=frame_background)
    global n

    def browsefile():
        global file_path
        file_path = filedialog.askdirectory()
        global imdir
        imdir = file_path + "/"
        global c
        c = []
        global imagename
        for i in os.listdir(imdir):
            if ('.jpg' in i) or ('.png' in i) or ('.jpeg' in i):
                u = imdir + i
                width, height = Image.open(u).size
                scale = height / 700
                new_width = width / scale
                if (new_width <= 1340):
                    image = Image.open(u).resize((int(new_width), 700))
                    c.append(ImageTk.PhotoImage(image))
                elif (new_width > 1340):
                    scale2 = width / 1340
                    new_height = int(height / scale2)
                    image = Image.open(u).resize((1340, new_height))
                    c.append(ImageTk.PhotoImage(image))
        global label
        if c != []:
            pixel = tkinter.PhotoImage(width=1, height=1)
            label = Label(root, image=pixel)
            label.place(x=710, y=425, anchor=CENTER)
            label.configure(image=c[0])
            label.grid_forget()
            Status = Label(root, text='1 out of ' + str(len(c)), width=18)
            Status.place(x=1260, y=10)
            Next["state"] = NORMAL
        else:
            imagename = Label(root, height=1, foreground='Blue', width=46)
            imagename.place(x=100, y=10)
            imagename.configure(text='No Images Found in this file.')
        n = len(os.listdir(imdir)[0])
        imagename = Label(root, height=1, foreground='Blue', width=n)
        imagename.place(x=100, y=10)
        imagename.configure(text=os.listdir(imdir)[0])
        Back["state"] = DISABLED


    def next():
        if Back["state"] == DISABLED:
            Back["state"] = NORMAL
        t = imagename.cget('text')
        for p in range(len(os.listdir(imdir))):
            o = os.listdir(imdir)[p]
            if t == o:
                label.place(x=710, y=425, anchor=CENTER)
                label.configure(image=c[p + 1])
                imagename.place(x=100, y=10)
                n = len(os.listdir(imdir)[p + 1])
                imagename.configure(text=os.listdir(imdir)[p + 1], width=n)
                Status = Label(root, text=str(p+2) + ' out of ' + str(len(c)), width=18)
                Status.place(x=1260, y=10)
                if p == (len(os.listdir(imdir)) - 2):
                    Next["state"] = DISABLED
                    break
                break


    def back():
        if Next["state"] == DISABLED:
            Next["state"] = NORMAL
        t = imagename.cget('text')
        for p in range(len(os.listdir(imdir))):
            o = os.listdir(imdir)[p]
            if t == o:
                label.place(x=710, y=425, anchor=CENTER)
                label.configure(image=c[p - 1])
                imagename.place(x=100, y=10)
                n = len(os.listdir(imdir)[p - 1])
                imagename.configure(text=os.listdir(imdir)[p - 1], width=n)
                Back.grid_forget()
                Status = Label(root, text=str(p) + ' out of ' + str(len(c)), width=18)
                Status.place(x=1260, y=10)
                if p == 1:
                    Back["state"] = DISABLED
                    break
                break


    pixel = tkinter.PhotoImage(width=1, height=1)
    Back = Button(root, text="<", image=pixel, height=70, width=20, command=back, compound="c")
    Back.place(x=0, y=360)

    Next = Button(root, text=">", image=pixel, height=70, width=20, command=next, compound="c")
    Next.place(x=1395, y=360)

    img = Image.open('Screenshot 2022-11-17 142415.png').resize((80, 60))
    browse = ImageTk.PhotoImage(img)
    Browse = Button(root, image=browse, command=browsefile, bd=0, compound="c", relief='sunken', anchor=NW)
    Browse.place(x=0, y=0)

    frame1.create_text(45, 70, text="Browse Folder")
    frame1.create_window(1, 1, anchor=NW, window=Browse)

    root.mainloop()
