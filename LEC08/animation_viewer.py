"""Drill #8: Naruto animation viewer (run, walk, jump, Y combo)."""
from pathlib import Path
from animation_data import load_clips
from playback import Playback

WIDTH, HEIGHT = 1000, 800
BASE = Path(__file__).resolve().parent

def main():
    import pico2d as p
    p.open_canvas(WIDTH, HEIGHT)
    clips = load_clips(BASE / 'assets/animations.json')
    player = Playback(clips)
    atlas = p.load_image(str(BASE / 'assets/naruto_atlas.png'))
    p.close_canvas()

if __name__ == '__main__':
    main()
