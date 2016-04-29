import Tkinter as tk
from random import randint
from Tkinter import *

class Baloons:
    

   def __init__(self,wdw, dimension, rootspeed):
        self.canvas= Canvas(wdw, width=dimension, height=dimension)
        self.canvas.grid(row=0, column=0)
        self.score=0
        self.xSpeed= app.updateValue(root)
        self.ySpeed = rootspeed
        self.update()
        self.update2()
        self.canvas.after(self.ySpeed,self.Refresher)
        self.canvas.after(self.ySpeed-5,self.Refresher2)
        self.canvas.bind("<Button-1>", self.click2)

   def click2(self, event):

       item = self.canvas.find_withtag(CURRENT)
       if item:
           self.canvas.delete(item)
           self.score = self.score + 1

       w.config(text = "Score:"+ str(self.score))

   def update(self):
      xCount = app.updateValue(root)
      trasher = self.canvas.find_withtag("A2")
      if trasher: 
           self.canvas.delete(trasher)

      for i in range(xCount):
          x, y = randint(0, 400-1), randint(0, 400-1)
          oval=self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")
          self.canvas.itemconfig(oval,tags="A1")


   def update2(self):
      xCount = app.updateValue(root)
      trasher = self.canvas.find_withtag("A1")

      if trasher: 
           self.canvas.delete(trasher)

      for i in range(xCount):
          x, y = randint(0, 400-1), randint(0, 400-1)
          oval=self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")
          self.canvas.itemconfig(oval,tags="A2")


   def delete(self):
       self.canvas.delete("all")


   def Refresher(self):
      self.canvas.after(self.ySpeed,self.update)
      self.canvas.after(self.ySpeed,self.Refresher)

  
   def Refresher2(self):
      trasher = self.canvas.find_withtag("A2") 
      self.canvas.delete(trasher)
      self.canvas.after(self.ySpeed,self.update2)
      self.canvas.after(self.ySpeed,self.Refresher2)


#Sets up a frame
class MyApplication(Frame):

    Count=1
    Delay=1
    Size=1
    Step=1

    #When a class is initialized, this is called as per any class 
    def __init__(self, master):

        #Similar to saying MyFrame = Frame(master)
        Frame.__init__(self, master)

        #Puts the frame on a grid. 
        self.grid(row=0,column=1)

        #Puts control frame values

        self.Count=1
        self.Delay=1
        self.Size=1
        self.Step=1         

        self.canvas=tk.Canvas(master, width=300, height=200, background='white')
        self.canvas.grid(row=0,column=0)


        label = Label(self, text='Count')
        label.grid(row=0,column=2)
        self.sc1 = Scale(self, variable=100, from_=100, to=1)
        self.sc1.bind("<ButtonRelease-1>", self.updateValue)
        self.sc1.grid(row=1, column=2)

        label = Label(self, text='Delay')
        label.grid(row=0, column=3)
        self.sc2 = Scale(self,variable=100, from_=100, to=1)
        self.sc2.bind("<ButtonRelease-1>", self.updateValue)
        self.sc2.grid(row=1,column=3)

        label = Label(self, text='Size')
        label.grid(row=0, column=4)
        self.sc3 = Scale(self,variable=100, from_=100, to=1)
        self.sc3.bind("<ButtonRelease-1>", self.updateValue)
        self.sc3.grid(row=1,column=4)

        label = Label(self, text='Step')
        label.grid(row=0, column=5)
        self.sc4 = Scale(self,variable=100, from_=100, to=1)
        self.sc4.bind("<ButtonRelease-1>", self.updateValue)
        self.sc4.grid(row=1,column=5)


    def updateValue(self,event):
   
        Count = self.sc1.get()
        Delay = self.sc2.get()
        Size = self.sc3.get()
        Step = self.sc4.get()

        return Count
        

def helloStart():
    global Turnedon
    
    if Turnedon == 1:
    
        ballonw = Baloons(root,400,1000)
        Turnedon = 0
        ballonw.update()

def helloStop():
     global Turnedon
     
     Turnedon = 1
     ballonw = Baloons(root,400,5000)
     ballonw.update()

def helloClear():

    if Turnedon == 0:
        ballonw = Baloons(root,400,1000)
        ballonw.delete()
        ballonw.update()


root = Tk()
app = MyApplication(root)
Turnedon = 1
ballonw = {}

button = Button(app, text='Start', command=helloStart)
button1 = Button(app, text='Stop', command=helloStop)
button2 = Button(app, text='Clear', command=helloClear)
button.grid(row=300,column=1,columnspan=2)
button1.grid(row=300,column=2,columnspan=3)
button2.grid(row=300,column=3,columnspan=5)


w = Label(root)
w.grid(column=10)
root.title("Ballons Game")

root.mainloop()
