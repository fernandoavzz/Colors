import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import numpy as np

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

#Find image
def openfn():
    filename = filedialog.askopenfilename(title='Open')
    return filename

#Here's where we load the image
def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.grid()


#My attempt for gray filter but reloading an image
def gray():
    imagen = openfn()
    img = Image.open(imagen)
    img = img.convert("RGB")

    datas = img.getdata()

    new_image_data = []

    for item in datas:
        # change all white (also shades of whites) pixels to yellow
        if item[0] in list(range(0, 255)):
            new_image_data.append((20, 40, 60))
        else:
            new_image_data.append(item)

    # update image data
    img.putdata(new_image_data)

    # save new image
    img.save("test_image_altered_background.jpg")

    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.grid()

    
#buttons
btn = tk.Button(root, text='Select an image', command=open_img).grid(column=0,row=0)
gray = tk.Button(root, text='Gray filter', command=gray).grid(column=1,row=0)
root.mainloop()