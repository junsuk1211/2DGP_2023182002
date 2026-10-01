"""Drill #8: Naruto animation viewer (run, walk, jump, Y combo)."""
from pathlib import Path
import json

WIDTH, HEIGHT = 1000, 800
BASE = Path(__file__).resolve().parent

def main():
    import pico2d as p
    p.open_canvas(WIDTH, HEIGHT)
    p.close_canvas()

if __name__ == '__main__':
    main()
