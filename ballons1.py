#!/bin/python

from Tkinter import *
from random import randint

root = Tk()
selinde=200
scoring=0
var = IntVar()


canvas = Canvas(root, width=400, height=400)
canvas.pack()

scale2 = Scale( root, variable = var, orient='horizontal')
scale2.pack(anchor=CENTER)


def sel():
   global selinde

   selection = var.get()
   selinde = int(selection)
   #label.config(text = selection)
   update(selinde)

def counterscores():

    global scoring
    scoring = scoring + 1
    w.config(text = "Score:"+ str(scoring))

def click(event):

        if canvas.find_withtag(CURRENT):
             canvas.itemconfig(CURRENT, state="hidden")
             canvas.update_idletasks()
             counterscores()
             canvas.after(200)
             canvas.delete("all")
             canvas.itemconfig(CURRENT, fill="red")
             update(selinde)

def update(selinde):
   for i in range(selinde):
        x, y = randint(0, 400-1), randint(0, 400-1)
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")

def callback():
    update()

update()

update(selinde)
canvas.bind("<Button-1>", click)

#canvas.after(500,callback)
button = Button(root, text="Set Ballons Scale Value", command=sel)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

w = Label(root)
w.config(text = "Score:"+ str(counterscores()))
w.pack()

root.title("Ballons Game")
root.mainloop()
                   
