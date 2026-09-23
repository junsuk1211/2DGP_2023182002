# DRILL #6: 원 → 사각형 → 삼각형 이동을 무한 반복한다.
import math
from pico2d import *


open_canvas(800, 600)
character = load_image('character.png')


def draw_character(x, y):
    get_events()
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)


def move_top():
    for x in range(50, 751, 5):
        draw_character(x, 550)


def move_right():
    for y in range(550, 49, -5):
        draw_character(750, y)


def move_bottom():
    for x in range(750, 49, -5):
        draw_character(x, 50)


def move_left():
    for y in range(50, 551, 5):
        draw_character(50, y)


def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()


def move_line(start, end, steps=100):
    x0, y0 = start
    x1, y1 = end

    for step in range(steps + 1):
        t = step / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        draw_character(x, y)


def move_triangle():
    point_a = (100, 100)
    point_b = (700, 100)
    point_c = (400, 500)

    move_line(point_a, point_b)
    move_line(point_b, point_c)
    move_line(point_c, point_a)


while True:
    move_circle()
    move_rectangle()
    move_triangle()


close_canvas()
