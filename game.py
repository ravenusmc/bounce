from tkinter import *
import random 
import time 

from ball import Ball
from paddle import Paddle 

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

#These two lines create a ball and paddle object based on the ball and paddle classes.
paddle = Paddle(canvas, "red")
ball = Ball(canvas, paddle, 'blue')

#The below code will allow the board to be displayed longer than a split second.
while 1:
  if ball.hit_bottom == False:
    paddle.draw()
    ball.draw()
  tk.update_idletasks()
  tk.update()
  time.sleep(0.01)