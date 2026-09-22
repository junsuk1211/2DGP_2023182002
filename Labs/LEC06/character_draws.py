# 실습 과제 진행
import math
from pico2d import*

open_canvas(800,600)
character = load_image('character.png')

def drawcharacter(x,y):
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
    print("삼각형 이동")
    pass

movebottom()
close_canvas()