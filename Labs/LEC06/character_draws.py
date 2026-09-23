# 실습 과제 진행
import math
from pico2d import*

open_canvas(800,600)
character = load_image('character.png')
pointa = (100,100)
pointb = (700,100)
pointc = (400,500)
def drawcharacter(x,y):
   get_events()
   clear_canvas()
   character.draw(x,y)
   update_canvas()
   delay(0.01)

def movecircle():
 for degree in range(360):
    theta = math.radians(degree)
    x = 400 + 200 * math.cos(theta)
    y = 300 + 200 * math.sin(theta)
    drawcharacter(x,y)
    pass

def moverectangle():
    movetop()
    moveright()
    movebottom()
    moveleft()
    pass
def movetop():
   for x in range(50,751,5):
      drawcharacter(x,550)
def moveright():
   for y in range(550,49,-5):
      drawcharacter(750,y)
def movebottom():
   for x in range(750,49,-5):
      drawcharacter(x,50)
def moveleft():
   for y in range(50,551,5):
      drawcharacter(50,y)

def movetriangle():
    moveab()
    movebc()
    moveca()
    pass

def moveab():
   x0,y0 = pointa
   x1,y1 = pointb

   n= 100

   for step in range(n+1):
      t = step /n
      x = x0 + (x1 - x0) * t
      y = y0 + (y1 - y0) * t
      drawcharacter(x,y)
   pass
def movebc():
     x0,y0 = pointb
     x1,y1 = pointc
   
     n= 100
   
     for step in range(n+1):
         t = step /n
         x = x0 + (x1 - x0) * t
         y = y0 + (y1 - y0) * t
         drawcharacter(x,y)
     pass
def moveca():
     x0,y0 = pointc
     x1,y1 = pointa
   
     n= 100
   
     for step in range(n+1):
         t = step /n
         x = x0 + (x1 - x0) * t
         y = y0 + (y1 - y0) * t
         drawcharacter(x,y)
     pass

moveab()
close_canvas()
