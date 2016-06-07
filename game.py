from tkinter import *
import random 
import time 

tk = Tk()
#The title is placed at the top of the sqare with the below line. 
tk.title("Bounce Game")
#Making the window a fixed size. 
tk.resizable(0,0)
#Places the game board at the topmost layer. 
tk.wm_attributes("-topmost", 1)
#Defining the canvas object. 
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
#Tells the canvas to size itself according to the precedding line. 
canvas.pack()
#This line tells tkinter to init itself for the animation in the game. 
tk.update()

#Creating the ball class. 
class Ball:
  def __init__(self,canvas,color):
    self.canvas = canvas
    self.id = canvas.create_oval(10,10,25,25, fill=color)
    self.canvas.move(self.id, 245, 100)
    starts = [-3, -2, -1, 1, 2, 3]
    random.shuffle(starts)
    self.x = starts[0]
    self.y = -3
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width = self.canvas.winfo_width()

  #making te ball move
  def draw(self):
    #The zero says do not move horizontal and the -1 says move UP the screen 
    self.canvas.move(self.id, self.x, self.y)
    pos = self.canvas.coords(self.id)
    if pos[1] <= 0:
      self.y = 3
    if pos[3] >= self.canvas_height:
      self.y = -3
    if pos[0] <= 0:
      self.x = 3
    if pos[2] >= self.canvas_width:
      self.x = -3

ball = Ball(canvas, 'blue')

#The below code will allow the board to be displayed longer than a split second.
while 1:
  ball.draw()
  tk.update_idletasks()
  tk.update()
  time.sleep(0.01)