"""소닉 스프라이트 시트의 동작을 제자리에서 재생한다."""

import pico2d


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800


def handle_events():
    for event in pico2d.get_events():
        if event.type == pico2d.SDL_QUIT:
            return False
        if event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            return False
    return True


def main():
    pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    try:
        while handle_events():
            pico2d.clear_canvas()
            pico2d.update_canvas()
            pico2d.delay(0.01)
    finally:
        pico2d.close_canvas()


if __name__ == "__main__":
    main()
