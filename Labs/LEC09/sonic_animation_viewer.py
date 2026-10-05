"""소닉 스프라이트 시트의 동작을 제자리에서 재생한다."""

import pico2d


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800


def main():
    pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    pico2d.delay(0.2)
    pico2d.close_canvas()


if __name__ == "__main__":
    main()
