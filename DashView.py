from Tkinter import *
import math
from threading import Timer
 
class Screen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.totalDistance = 0
        self.nextDistance = 0.0
        self.lTurn = False
        self.rTurn = False
        
        master.wm_title("GPS HUD")
        
        self.ver = 5
        self.wMod = 20
        self.xOff = 4*self.wMod
        self.yOff = self.xOff
        self.canvasWidth = 700
        self.canvasHeight = 500
        
        self.w = Canvas(master, width=self.canvasWidth, height=self.canvasHeight)
        self.w.grid(row=0, column=0, columnspan=4)

        self.lArrowToggle = Button(master, text="LEFT",command=self.toggleLeft)
        self.lArrowToggle.grid(row=1, column=0)
        self.sbTotalDistance = Spinbox(master, from_ = 0, to = 100, increment=5, command=self.toggleTotal)
        self.sbTotalDistance.grid(row=1, column=1)
        self.sbNextDistance = Spinbox(master, from_ = 0.0, to = 5.0, increment=0.1, command=self.toggleNext)
        self.sbNextDistance.grid(row=1, column=2)
        self.rArrowToggle = Button(master, text="RIGHT",command=self.toggleRight)
        self.rArrowToggle.grid(row=1, column=3)
        
        self.updateScreen()
    
    def updateScreen(self):
        self.clearScreen()
        
        if self.lTurn:
            self.drawLeftArrow(150, 250, 100, 200)
        if self.rTurn:
            self.drawRightArrow(550, 250, 100, 200)
        if self.totalDistance:
            self.drawTotalDistance(25, 25)
        if self.nextDistance:
            self.drawNextDistance(350, 250)
    
    def toggleLeft(self):
        self.lTurn = not self.lTurn
        self.rTurn = False
        self.updateScreen()
    
    def toggleRight(self):
        self.rTurn = not self.rTurn
        self.lTurn = False
        self.updateScreen()
        
    def toggleTotal(self):
        self.totalDistance = self.sbTotalDistance.get()
        self.updateScreen()
    
    def toggleNext(self):
        self.nextDistance = self.sbNextDistance.get()
        self.updateScreen()
    
    def drawLeftArrow(self, x, y, w, h, color="white"):
        self.w.create_polygon(x+w, y-h/2, x, y, x+w, y+h/2, x+w/5, y, fill=color, outline=color)
    
    def drawRightArrow(self, x, y, w, h, color="white"):
        self.w.create_polygon(x-w, y-h/2, x, y, x-w, y+h/2, x-w/5, y, fill=color, outline=color)
    
    def drawTotalDistance(self, x, y, color="white"):
        canvas_id = self.w.create_text(x, y, anchor="nw", fill=color, font="Helvetica 18")
        self.w.itemconfig(canvas_id, text="TOTAL DISTANCE:  miles")
        self.w.insert(canvas_id, 16, self.totalDistance)
        
    def drawNextDistance(self, x, y, color="white"):
        canvas_id = self.w.create_text(x, y, fill=color, font="Helvetica 36")
        self.w.itemconfig(canvas_id, text=self.nextDistance )
    
    def clearScreen(self):
        color = "black"
        self.w.create_rectangle(0, 0, self.canvasWidth, self.canvasHeight, fill=color, outline=color)

screen = Screen( Tk() )
mainloop()



