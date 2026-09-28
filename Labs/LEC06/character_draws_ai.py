import math
import os

from pico2d import *


open_canvas(800, 600)
character = load_image(os.path.join(os.path.dirname(__file__), "character.png"))


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def circle_positions():
    for degree in range(360):
        angle = math.radians(degree)
        yield 400 + 200 * math.cos(angle), 300 + 200 * math.sin(angle)


def polygon_positions(vertices):
    closed_vertices = vertices[1:] + vertices[:1]

    for start, end in zip(vertices, closed_vertices):
        x0, y0 = start
        x1, y1 = end
        steps = max(1, round(math.hypot(x1 - x0, y1 - y0) / 5))

        for step in range(steps + 1):
            ratio = step / steps
            x = x0 + (x1 - x0) * ratio
            y = y0 + (y1 - y0) * ratio
            yield x, y


rectangle = [(50, 550), (750, 550), (750, 50), (50, 50)]
triangle = [(100, 100), (700, 100), (400, 500)]

while True:
    for position in circle_positions():
        draw_character(*position)

    for position in polygon_positions(rectangle):
        draw_character(*position)

    for position in polygon_positions(triangle):
        draw_character(*position)
