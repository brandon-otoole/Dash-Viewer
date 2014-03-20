from Tkinter import *
import math
from threading import Timer
 
class Screen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.totalDistance = True
        self.nextDistance = True
        self.lTurn = False
        self.rTurn = False
        
        master.wm_title("GPS HUD")
        
        self.ver = 5
        self.wMod = 20
        self.xOff = 4*self.wMod
        self.yOff = self.xOff
        self.canvSize = 700
        
        self.w = Canvas(master, width=self.canvSize, height=self.canvSize)
        self.w.grid(row=0, column=0, columnspan=4)

        self.lArrowToggle = Button(master, text="LEFT",command=self.toggleLeft)
        self.lArrowToggle.grid(row=1, column=0)
        self.b1 = Button(master, text="Total Distance",command=self.toggleTotal)
        self.b1.grid(row=1, column=1)
        self.b2 = Button(master, text="Next Distance",command=self.toggleNext)
        self.b2.grid(row=1, column=2)
        self.rArrowToggle = Button(master, text="RIGHT",command=self.toggleRight)
        self.rArrowToggle.grid(row=1, column=3)
        
        self.updateScreen()
    
    def updateScreen(self):
        self.ver = (self.ver + 1)%7
        
        self.clearScreen()
        
        if self.lTurn:
            self.drawLeftArrow(150, 250, 100, 200)
        if self.rTurn:
            self.drawRightArrow(550, 250, 100, 200)
        if self.totalDistance:
            self.drawTotalDistance()
        if self.nextDistance:
            self.drawNextDistance()
        
        #self.drawAlignment(self.xOff, self.yOff, self.wMod)
        #self.drawAlignment(self.xOff + 14*self.wMod, self.yOff, self.wMod)
        #self.drawAlignment(self.xOff, self.yOff+14*self.wMod, self.wMod)
        #self.drawTiming(self.xOff, self.yOff, self.wMod)
        #self.drawVersion(self.xOff, self.yOff, self.wMod)
        #self.drawFormat(self.ver, self.xOff, self.yOff, self.wMod)
    
    def toggleLeft(self):
        self.lTurn = True
        self.rTurn = not self.lTurn
        self.updateScreen()
    
    def toggleRight(self):
        self.rTurn = True
        self.lTurn = not self.rTurn
        self.updateScreen()
        
    def toggleTotal(self):
        self.totalDistance = not self.totalDistance
        self.updateScreen()
    
    def toggleNext(self):
        self.nextDistance = not self.nextDistance
        self.updateScreen()
    
    def drawLeftArrow(self, x, y, w, h, color="white"):
        self.w.create_polygon(x+w, y-h/2, x, y, x+w, y+h/2, x+w/5, y, fill=color, outline=color)
    
    def drawRightArrow(self, x, y, w, h, color="white"):
        self.w.create_polygon(x-w, y-h/2, x, y, x-w, y+h/2, x-w/5, y, fill=color, outline=color)
    
    def drawTotalDistance(self):
        color="white"
        self.w.create_rectangle(25, 25, 25+150, 25+50, fill=color, outline=color)
    
    def drawNextDistance(self):
        color="white"
        self.w.create_rectangle(325, 325, 375, 375, fill=color, outline=color)
    
    def clearScreen(self):
        color = "black"
        self.w.create_rectangle(0, 0, 700, 700, fill=color, outline=color)

screen = Screen( Tk() )
mainloop()



