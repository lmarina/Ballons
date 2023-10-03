import sys
from random import randint

# Tkinter management

try:
    # for Python2
    from Tkinter import *
    import Tkinter as tk
except ImportError:
    try:
         # for Python3
         from tkinter import *   
         import tkinter as tk
    except ImportError:
         print("------------------------------------------------------------------------------")
         print( "Warning !!!: a needed software TKINTER has to be installed to run this program")
         print("------------------------------------------------------------------------------")


#Sets up frame model

class MyApplication():

     
    # Initialization variables
    Count=10
    Delay=10
    Size=10
    Step=10
    job1=0
    job2=0
    job3=0
    job4=0
    job5=0
    job6=0
    job7=0
    job8=0

    #When a class is initialized, this is called as per any class
    def __init__(self, parent):
        self.myParent = parent

        print("stage Containers construction frames")
        
        self.main_container = Frame(parent)
        self.main_container = Frame(parent, height=400, width=400, background="green", borderwidth=2, highlightbackground="yellow",highlightthickness=2)

        self.top_frame = Frame(self.main_container)
        self.bottom_frame = Frame(self.main_container)
        self.main_container.grid(row=0, column=0, sticky="nsew")
        self.myParent.grid_rowconfigure(0, weight=1)
        self.myParent.grid_columnconfigure(0, weight=1)
        self.main_container.grid(row=0, rowspan=2, column=0, columnspan=4)

        print("stage Puts control frame values")

        self.Count=10
        self.Delay=10
        self.Size=10
        self.Step=10

        print("stage Frames & Canvas & Styler")

        self.top_frame = Frame(self.main_container)
        self.bottom_frame = Frame(self.main_container)

        self.middle_frame_top = Frame(self.main_container)
        self.middle_frame = Frame(self.main_container)
        self.middle_frame_bottom = Frame(self.main_container)

        self.canvas_frame = Canvas(self.main_container, height=400, width=400)
        self.canvas_frame.grid(row=1, column=0)

        self.main_container.grid(row=0, column=0, sticky="nsew")
        self.myParent.grid_rowconfigure(0, weight=1)
        self.myParent.grid_columnconfigure(0, weight=1)

        self.scaler1 = Scale(self.middle_frame,  length=400,variable=1.1, from_=20, to=1)
        self.scaler2 = Scale(self.middle_frame,  length=400,variable=1.2, from_=20, to=1)
        self.scaler3 = Scale(self.middle_frame,  length=400,variable=1.3, from_=20, to=1)
        self.scaler4 = Scale(self.middle_frame,  length=400,variable=1.4, from_=20, to=1)


        print("Frames disribution on screen")


        self.top_frame.grid(row=0, column=0, sticky="ew")
        self.bottom_frame.grid(row=2,  column=0,  sticky="ew")

        self.main_container.grid_rowconfigure(1, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        self.top_left = Frame(self.top_frame)
        self.top_center = Frame(self.top_frame)
        self.top_right = Frame(self.top_frame)


        self.middle_frame_top.grid(row=0,column=1,columnspan=4,sticky="ew")
        self.middle_frame.grid(row=1, rowspan=1,column=1, columnspan=2, sticky="ew")
        self.middle_frame_bottom.grid(row=2,rowspan=1,column=2, columnspan=4, sticky="ew")


        self.bottom_left = Frame(self.bottom_frame)
        self.bottom_left = Frame(self.bottom_frame)
        self.bottom_center = Frame(self.bottom_frame)
        self.bottom_left = Frame(self.bottom_frame)
        self.bottom_right = Frame(self.bottom_frame)

        print("stage Frames &Scales Deploy")

        self.top_left = Frame(self.top_frame, background="pink")
        self.top_right = Frame(self.top_frame, background="blue")
        self.top_center = Frame(self.top_frame, background="gray")

        self.top_left.grid(row=0, column=0, sticky="w")
        self.top_center.grid(row=0, column=1, sticky="n")
        self.top_right.grid(row=0, column=2, sticky="e")
        self.top_frame.grid_columnconfigure(1, weight=1)

        self.bottom_left = Frame(self.bottom_frame, background="pink")
        self.bottom_center = Frame(self.bottom_frame, background="blue")
        self.bottom_right = Frame(self.bottom_frame, background="gray")
        self.bottom_left.grid(row=2, column=0)
        self.bottom_center.grid(row=2, column=1)
        self.bottom_right.grid(row=2, column=2)

        self.scaler1.grid(row=2, rowspan=2,column=0)
        self.scaler1.set(10)
        self.scaler2.grid(row=2, rowspan=2,column=1)
        self.scaler2.set(10)
        self.scaler3.grid(row=2, rowspan=2,column=2)
        self.scaler3.set(10)
        self.scaler4.grid(row=2, rowspan=2,column=3)
        self.scaler4.set(10)


        self.top_left_label = Label(self.top_left, text="")
        self.top_center_label = Label(self.top_center, text= "Put mouse inside box to pop ballons")
        self.top_right_label = Label(self.top_right, text="")
        self.bottom_frame_top_label = Label(self.middle_frame_top, text="    Count Delay      Size Step ")
        self.bottom_frame_label = Label(self.middle_frame_bottom, text="Score:")

        self.top_left_label.grid(row=0, column=0, sticky="w")
        self.top_center_label.grid(row=0, column=0, sticky="n")
        self.top_right_label.grid(row=0, column=0, sticky="e")
        self.bottom_frame_top_label.grid(row=0, column=3, sticky="n")
        self.bottom_frame_label.grid(row=0, column=3, sticky="e")

        print("stage Buttons deploy & Frame initialization")

        self.button1 = Button(self.bottom_left,text='Start', width=10, command=helloStart)
        self.button2 = Button(self.bottom_center,text='Stop', width=10, command=helloStop)
        self.button3 = Button(self.bottom_right,text='Clear', width=10, command=helloClear)
        self.button1.grid(row=2, column=0, sticky="e")
        self.button2.grid(row=2, column=1, sticky="n")
        self.button3.grid(row=2, column=2, sticky="w")
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)


        self.scaler1.bind("<ButtonRelease-1>", self.updateValueCount)
        self.scaler2.bind("<ButtonRelease-1>", self.updateValueDelay)
        self.scaler3.bind("<ButtonRelease-1>", self.updateValueSize)
        self.scaler4.bind("<ButtonRelease-1>", self.updateValueStep)

        print("stage frames ready")
        print("Application logic")

    def updateValueCount(self,event):

        Count = self.scaler1.get()

        return Count

    def updateValueDelay(self,event):

        Delay = self.scaler2.get()

        return Delay

    def updateValueSize(self,event):

         Size = self.scaler3.get()

         return Size

    def updateValueStep(self,event):

         Step = self.scaler4.get()

         return Step


    def BallonsClear(self):
       self.canvas_frame.delete("all")
       print("clear")

    def BallonsStop(self):

       global job1
       global job2

       root.after_cancel(job1)
       root.after_cancel(job2)
       root.after_cancel(job3)
       root.after_cancel(job4)
       root.after_cancel(job5)
       root.after_cancel(job6)
       root.after_cancel(job7)
       root.after_cancel(job8)
       
       print("Stop")
      
       job1=0
       job2=0

    def NewBallons(self):

        global job1
        global job2
        global job3

        print("stage Let's start")

        x, y = randint(0, 400-1), randint(0, 400-1)
    oval=self.canvas_frame.create_oval(x-5, y-5, x+5, y+5, fill="red", outline="red", width = 10, outlinestipple='gray12',
    state="normal")

    self.score=0
    self.reduced=[]
    self.xWidth= self.scaler3.get()
    self.xSpeed= self.scaler2.get()

    if self.xSpeed == 2:
        self.ySpeed = 100
    elif self.xSpeed == 3:
            self.ySpeed = 200
    elif self.xSpeed == 4:
        self.ySpeed = 300
    elif self.xSpeed == 5:
        self.ySpeed = 400
    elif self.xSpeed == 6:
        self.ySpeed =  500
    elif self.xSpeed == 7:
        self.ySpeed = 600
    elif self.xSpeed == 8:
        self.ySpeed = 700
    elif self.xSpeed == 9:
        self.ySpeed = 800
    elif self.xSpeed == 10:
        self.ySpeed = 1000
    elif self.xSpeed == 11:
        self.ySpeed = 2000
    elif self.xSpeed == 12:
        self.ySpeed = 3000
    elif self.xSpeed == 13:
        self.ySpeed = 4000
    elif self.xSpeed == 14:
        self.ySpeed = 5000
    elif self.xSpeed == 15:
        self.ySpeed = 6000
    elif self.xSpeed == 16:
        self.ySpeed = 7000
    elif self.xSpeed == 17:
        self.ySpeed = 8000
    elif self.xSpeed == 18:
        self.ySpeed = 9000
    elif self.xSpeed == 19:
        self.ySpeed = 10000
    elif self.xSpeed == 20:
        self.ySpeed = 11000

    self.update()
    self.update2()
    job1=self.canvas_frame.after(self.ySpeed,self.Refresher)
    job2=self.canvas_frame.after((self.ySpeed*3),self.Refresher2)
    job3=self.canvas_frame.after(self.ySpeed,self.SizeReducer)
    self.canvas_frame.bind("<Button-1>", self.click2)

    def click2(self, event):

        xCount = self.scaler1.get()
        xWidth = 10
        xStep = self.scaler4.get()
        item = self.canvas_frame.find_withtag(CURRENT)
        itemsr = self.canvas_frame.find_withtag("SR")
        # if item is in shorter list size half score

        print(item)
        print() 
        print(itemsr)
        print()
        
        
        if (job1 != 0 and job2 != 0):
          if any(item in itemsr for item in item):
              self.canvas_frame.delete(itemsr)
              xWidth = 5

              if item:

               if (xStep >= 10 and xStep <= 25):
                      item = self.canvas_frame.find_withtag("A3")
                      xWidth = 15
               elif (xStep >= 25 and xStep <= 50):
                      item = self.canvas_frame.find_withtag("A3")
                      xWidth = 20
               elif (xStep >= 50 and xStep <= 75):
                      item = self.canvas_frame.find_withtag("A3")
                      xWidth = 25
               elif (xStep >= 75 and xStep <= 98 ):
                      item = self.canvas_frame.find_withtag("A3")
                      xWidth = 30         

               print("Point")
               self.canvas_frame.delete(item)
               self.score = self.score + xWidth
       
              self.bottom_frame_label.config(text = "Score:"+ str(self.score))

    def update(self):

      xWidth = self.scaler3.get()
      xCount = self.scaler1.get()
      xStep = self.scaler4.get()
      trasher = self.canvas_frame.find_withtag("A2")
      trasher2 = self.canvas_frame.find_withtag("A1")
      
      print("Some adjustments in Count:"+str(xCount))
      print("Some adjustments in Steps:"+str(xStep))
      print("More Ballons!!!")
      xTags = "A1"
      xState="normal"
      
      if trasher:
           self.canvas_frame.delete(trasher)

      if trasher2:
           self.canvas_frame.delete(trasher2)

      if xStep >= 19:
            xState = 'hidden'
      elif xStep > 1:
            xTags="A3"
            if xWidth > 1 :
               xWidth = xWidth - 25
               if xWidth < 1:
                  xWidth = xWidth + 25
      elif xStep==1:
            xState = 'normal'

             
      for i in range(xCount):
              x, y = randint(0, 400-1), randint(0, 400-1)
              oval=self.canvas_frame.create_oval(x-5, y-5, x+5, y+5, fill="red", outline="red", width = xWidth, outlinestipple='gray12',state=xState)
              self.canvas_frame.itemconfig(oval,tags="A1")
      
      

    def update2(self):

      xWidth = self.scaler3.get()
      xCount = self.scaler1.get()
      xStep = self.scaler4.get()
      trasher = self.canvas_frame.find_withtag("A1")
      trasher2 = self.canvas_frame.find_withtag("A2")

      
      print("More and  More ballons!!!!")
      xTags="A2"
      xState="normal"

      if trasher:
           self.canvas_frame.delete(trasher)

      if trasher2:
          self.canvas_frame.delete(trasher2)

      if xStep >= 19:
           xState = 'hidden'
      elif xStep > 1:
           xTags = "A3"
           if xWidth > 1 :
               xWidth = xWidth - 25
               if xWidth < 1 :
                  xWidth = xWidth + 25

      elif xStep == 1:
           xState = 'normal'

      for i in range(xCount):
          x, y = randint(0, 400-1), randint(0, 400-1)
          oval=self.canvas_frame.create_oval(x-5, y-5, x+5, y+5, fill="red",outline="red",width = xWidth, outlinestipple='gray12',
                                       state = xState)
          self.canvas_frame.itemconfig(oval,tags="A2")


    def delete(self):

       xWidth = self.scaler3.get()
       xCount = 1

       for i in range(xCount):
            x, y = randint(0, 400-1), randint(0, 400-1)
            oval=self.canvas_frame.create_oval(x-5, y-5, x+5, y+5, fill="",width = xWidth)
       self.canvas_frame.delete("all")
       self.score = 0

    def Refresher(self):
      global job4
      global job5

      trasher = self.canvas_frame.find_withtag("A1")
      job4=self.canvas_frame.after(self.ySpeed,self.update)
      job5=self.canvas_frame.after(self.ySpeed,self.Refresher)


    def Refresher2(self):
      global job6
      global job7
     
      trasher = self.canvas_frame.find_withtag("A2")
      self.canvas_frame.delete(trasher)
      job6=self.canvas_frame.after(self.ySpeed,self.update2)
      job7=self.canvas_frame.after(self.ySpeed,self.Refresher2)

    def SizeReducer(self):
      global job8

      xCount = self.scaler1.get()
      item = self.canvas_frame.find_withtag(CURRENT)
      self.reduced.append(self.xWidth/2)
 
      if len(self.reduced) == 1:
           if self.reduced[0] <= 1:
             self.reduced.append(1)              

      self.canvas_frame.delete(item)
      xState = "normal"
      xTags = "SR"

      for i in range(xCount):
          x, y = randint(0, 400-1), randint(0, 400-1)
          oval=self.canvas_frame.create_oval(x-5, y-5, x+5, y+5, fill="red",outline="red",width = self.reduced[len(self.reduced)-1], outlinestipple='gray12',state =xState)
          self.canvas_frame.itemconfig(oval,tags="SR")

      job8=self.canvas_frame.after(self.ySpeed,self.SizeReducer)


# Functions to call methods

def helloStart():
 
    app.NewBallons()

def helloStop():

    app.BallonsStop()    

def helloClear():

    app.BallonsClear()


# Main
root = Tk()
app = MyApplication(root)


# Main loop and Window Title

root.title("drawing swirling ballons")
root.mainloop()
