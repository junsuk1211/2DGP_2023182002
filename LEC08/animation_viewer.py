"""Drill #8: Naruto animation viewer (run, walk, jump, Y combo)."""
from pathlib import Path
from animation_data import load_clips
from playback import Playback

WIDTH, HEIGHT = 1000, 800
SCALE = 8
BASE = Path(__file__).resolve().parent

def main():
    import pico2d.pico2d as p
    p.open_canvas(WIDTH, HEIGHT)
    p.SDL_SetHint(p.SDL_HINT_RENDER_SCALE_QUALITY, b'0')
    p.SDL_SetWindowTitle(p.window, b'Naruto | Run / Walk / Jump / Y Combo')
    try:
        clips = load_clips(BASE / 'assets/animations.json')
        player = Playback(clips)
        atlas = p.load_image(str(BASE / 'assets/naruto_atlas.png'))
        font_path = Path('C:/Windows/Fonts/consola.ttf')
        if not font_path.exists():
            font_path = Path(p.__file__).parent / 'data/ConsolaMalgun.TTF'
        font = p.load_font(str(font_path), 24)
        last = p.get_time()
        running = True
        while running:
            for event in p.get_events():
                if event.type == p.SDL_QUIT or (event.type == p.SDL_KEYDOWN and event.key == p.SDLK_ESCAPE):
                    running = False
            if not running:
                break
            now = p.get_time()
            player.update(now - last)
            last = now
            p.clear_canvas()
            frame = player.clip.frames[player.frame_index]
            # Keep the union of each clip centered; feet share a stable baseline.
            max_height = max(item.height for item in player.clip.frames) * SCALE
            baseline = HEIGHT / 2 - max_height / 2
            center_y = baseline + frame.height * SCALE / 2
            atlas.clip_draw(frame.x, atlas.h - frame.y - frame.height,
                            frame.width, frame.height, WIDTH // 2, center_y,
                            frame.width * SCALE, frame.height * SCALE)
            name = player.clip.name.replace('_', ' ').upper()
            status = 'PAUSE 1s' if player.is_paused else f'REPEAT {player.repetition}/5'
            font.draw(28, HEIGHT - 35, f'{name}   |   {status}', (30, 40, 60))
            font.draw(28, 28, 'RUN > WALK > JUMP > Y COMBO    |    ESC: QUIT', (60, 70, 90))
            p.update_canvas()
            p.delay(0.01)
    finally:
        p.close_canvas()

if __name__ == '__main__':
    main()
