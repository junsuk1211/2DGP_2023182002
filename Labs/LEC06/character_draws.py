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
   print("오른쪽 이동")
def movebottom():
   print("아래 이동")
def moveleft():
   print("왼쪽 이동")

def movetriangle():
    print("삼각형 이동")
    pass

while True:
    movecircle()
    moverectangle()
    movetriangle()
    pass

close_canvas()