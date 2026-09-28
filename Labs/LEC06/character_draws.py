# 실습 과제 진행
import math
from pico2d import*

open_canvas(800,600)
character = load_image('character.png')

def movecircle():
   for degree in range(360):
      theta = math.radians(degree)
      x = 400 + 200 * math.cos(theta)
      y = 300 + 200 * math.sin(theta)
      clear_canvas()
      character.draw(x,y)
      update_canvas()
      delay(0.05)
      pass

def move_top():
   print('top')
   pass
def move_right():
   print('right')
   pass
def move_bottom():
   print('bottom')
   pass
def move_left():
   print('left')
   pass

def moverectangle():
   print("사각형 이동")
   move_top()
   move_right()
   move_bottom()
   move_left()
   pass

def movetriangle():
   print("삼각형 이동")
   pass

while True:
   movecircle()
   moverectangle()
   movetriangle()
   pass

close_canvas()