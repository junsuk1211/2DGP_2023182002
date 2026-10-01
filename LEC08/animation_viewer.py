"""Drill #8: Naruto animation viewer (run, walk, jump, Y combo)."""
from pathlib import Path
from animation_data import load_clips
from playback import Playback

WIDTH, HEIGHT = 1000, 800
SCALE = 8
BASE = Path(__file__).resolve().parent

def main():
    import pico2d as p
    p.open_canvas(WIDTH, HEIGHT)
    clips = load_clips(BASE / 'assets/animations.json')
    player = Playback(clips)
    atlas = p.load_image(str(BASE / 'assets/naruto_atlas.png'))
    last = p.get_time()
    running = True
    while running:
        now = p.get_time()
        player.update(now - last)
        last = now
        p.clear_canvas()
        frame = player.clip.frames[player.frame_index]
        atlas.clip_draw(frame.x, atlas.h - frame.y - frame.height,
                        frame.width, frame.height, WIDTH // 2, HEIGHT // 2,
                        frame.width * SCALE, frame.height * SCALE)
        p.update_canvas()
        p.delay(0.01)
    p.close_canvas()

if __name__ == '__main__':
    main()
