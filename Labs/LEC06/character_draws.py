# 실습 과제 진행
import math
from pico2d import*

open_canvas(800,600)
character = load_image('character.png')
point_a = (100, 100)
point_b = (700, 100)
point_c = (400, 500)

def movecircle():
   for degree in range(0,360):
      theta = math.radians(degree)
      x = 400 + 200 * math.cos(theta)
      y = 300 + 200 * math.sin(theta)
      draw_character(x,y)
   pass

def move_top():
   for x in range(50,751,5):
      draw_character(x,550)
   pass

def draw_character(x,y):
      clear_canvas()
      character.draw(x,y)
      update_canvas()
      delay(0.05)

def move_right():
   for y in range(550,49,-5):
      draw_character(750,y)
   pass
def move_bottom():
   for x in range(750,49,-5):
      draw_character(x,50)
   pass
def move_left():
   for y in range(50,551,5):
      draw_character(50,y)
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
   move_ab()
   move_bc()
   move_ca()
   pass

def move_ab():
   pass

def move_bc():
   pass

def move_ca():
   pass

while True:
   movecircle()
   moverectangle()
   movetriangle()
   pass

close_canvas()
