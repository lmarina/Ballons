import Tkinter as tk
from random import randint
from Tkinter import *


#Ballon's Class

class Baloons:
    

   def __init__(self,wdw, dimension, rootspeed):
        self.canvas= Canvas(wdw, width=dimension, height=dimension)
        self.canvas.grid(row=0, column=0)
        self.score=0
        self.xWidth= app.updateValueSize(root)
        self.xSpeed= app.updateValueDelay(root)
        self.ySpeed = rootspeed

        if self.xSpeed == 2:
            self.ySpeed = 2000
        elif self.xSpeed == 3:
            self.ySpeed = 3000
        elif self.xSpeed == 4:
            self.ySpeed = 4000
        elif self.xSpeed == 5:
            self.ySpeed = 5000
        elif self.xSpeed == 6:
            self.ySpeed = 6000
        elif self.xSpeed == 7:
            self.ySpeed = 7000
        elif self.xSpeed == 8:
            self.ySpeed = 8000
        elif self.xSpeed == 9:
            self.ySpeed = 9000
        elif self.xSpeed == 10:
            self.ySpeed = 10000
 
        self.update()
        self.update2()
        self.canvas.after(self.ySpeed,self.Refresher)
        self.canvas.after(self.ySpeed-5,self.Refresher2)
        self.canvas.bind("<Button-1>", self.click2)

   def click2(self, event):

       xWidth = app.updateValueSize(root)
       
       item = self.canvas.find_withtag(CURRENT)
       if item:
           self.canvas.delete(item)
           
           self.score = self.score + xWidth

       w.config(text = "Score:"+ str(self.score))

   def update(self):
      
      xWidth = app.updateValueSize(root)
      xCount = app.updateValueCount(root)
      trasher = self.canvas.find_withtag("A2")
      if trasher: 
           self.canvas.delete(trasher)

      for i in range(xCount):
          x, y = randint(0, 400-1), randint(0, 400-1)
          oval=self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red", width = xWidth)
          self.canvas.itemconfig(oval,tags="A1")


   def update2(self):

      xWidth = app.updateValueSize(root)
      xCount = app.updateValueCount(root)
      trasher = self.canvas.find_withtag("A1")

      if trasher: 
           self.canvas.delete(trasher)

      for i in range(xCount):
          x, y = randint(0, 400-1), randint(0, 400-1)
          oval=self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red",width = xWidth)
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
        self.height=400
        #Puts the frame on a grid. 
        self.grid(row=0,column=1)

        #Puts control frame values

        self.Count=1
        self.Delay=1
        self.Size=1
        self.Step=1         

        self.canvas=tk.Canvas(master, width=400, height=400, background='white')
        self.canvas.grid(row=0,column=0)


        label = Label(self, text='Count')
        label.grid(row=0,column=2,sticky=(N,S,E,W))
        self.sc1 = Scale(self, variable=1, from_=100, to=1)
        self.sc1.bind("<ButtonRelease-1>", self.updateValueCount)
        self.sc1.grid(row=1, column=2, sticky=(N,S,E,W))

	button = Button(root,text='Start', command=helloStart)
	button1 = Button(root,text='Stop', command=helloStop)
	button2 = Button(root,text='Clear', command=helloClear)
	button.grid(row=400,sticky=(W))
	button1.grid(row=400,sticky=(N))
	button2.grid(row=400,sticky=(E))


    def controlFramedelay(self):

        label = Label(self, text='Delay')
        label.grid(row=0, column=3,sticky=(N,S,E,W))
        self.sc2 = Scale(self,variable=1.1, from_=10, to=1)
        self.sc2.bind("<ButtonRelease-1>", self.updateValueDelay)
        self.sc2.grid(row=1,column=3,sticky=(N,S,E,W))

        
    def controlFramesize(self):
 
        label = Label(self, text='Size')
        label.grid(row=0, column=4, sticky=(N,S,E,W))
        self.sc3 = Scale(self,variable=1.2, from_=3, to=1)
        self.sc3.bind("<ButtonRelease-1>", self.updateValueSize)
        self.sc3.grid(row=1,column=4, sticky=(N,S,E,W))

    def controlFramestep(self): 
        label = Label(self, text='Step')
        label.grid(row=0, column=5,sticky=(N,S,E,W))
        self.sc4 = Scale(self,variable=20, from_=100, to=1)
        self.sc4.bind("<ButtonRelease-1>", self.updateValueStep)
        self.sc4.grid(row=1,column=5, sticky=(N,S,E,W))


    def updateValueCount(self,event):
   
        Count = self.sc1.get()

        return Count
        
    def updateValueDelay(self,event):

        Delay = self.sc2.get()
        
        return Delay

    def updateValueSize(self,event):

         Size = self.sc3.get()

         return Size

    def updateValueStep(self,event):

         Step = self.sc4.get()

         return Step

# Functions to initialize buttons
def helloStart():
    global Turnedon
    
    if Turnedon == 1:
    
        ballonw = Baloons(root,400,1000)
        Turnedon = 0
        ballonw.update()

def helloStop():
     global Turnedon
     
     Turnedon = 1
     ballonw = Baloons(root,400,99000)
     ballonw.update()

def helloClear():

    if Turnedon == 0:
        ballonw = Baloons(root,400,1000)
        ballonw.delete()
        ballonw.update()


# Main 
root = Tk()
app = MyApplication(root)
app.controlFramedelay()
app.controlFramesize()
app.controlFramestep()

Turnedon = 1

w = Label(root)
w.grid(column=10,sticky=(E))
w.config(text = "Score:"+ str(0))


root.title("Ballons Game")
root.mainloop()
