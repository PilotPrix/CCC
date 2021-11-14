from tkinter import *
from time import *
myInterface = Tk()
screen = Canvas(myInterface, width=1280, height=720, background="CadetBlue2")
screen.pack()

screen.create_rectangle(100, 200, 300, 300, fill = "turquoise3", outline = "cadetBlue2")
screen.create_oval(100, 100, 300, 300, fill = "turquoise2", outline = "CadetBlue2")

ballLeft = 100
for frame in range(500):
    ball = screen.create_oval(ballLeft, 100, ballLeft + 200, 300, fill = "blue", outline= "")
    ballLeft = (ballLeft + 1)%500
    screen.update()
    sleep(0.02)
    screen.delete(ball)
