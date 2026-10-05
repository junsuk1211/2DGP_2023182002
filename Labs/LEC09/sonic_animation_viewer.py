"""소닉 스프라이트 시트의 동작을 제자리에서 재생한다."""

from pathlib import Path
from time import perf_counter

import pico2d


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
SCALE = 10
FRAME_SECONDS = 0.1
IMAGE_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")

# 프레임 영역은 원본 이미지의 좌측 상단 기준 (x, y, 너비, 높이)다.
ANIMATIONS = [
    ("대기", [
        (1, 39, 29, 39), (31, 40, 26, 38), (58, 39, 29, 39),
        (87, 40, 29, 38), (118, 40, 30, 38), (150, 40, 30, 38),
        (182, 40, 30, 38),
    ]),
]


class Player:
    def __init__(self):
        self.animation_index = 0
        self.frame_index = 0
        self.elapsed = 0.0

    @property
    def frames(self):
        return ANIMATIONS[self.animation_index][1]

    @property
    def frame(self):
        return self.frames[self.frame_index]

    def update(self, dt):
        self.elapsed += dt
        while self.elapsed >= FRAME_SECONDS:
            self.elapsed -= FRAME_SECONDS
            self.frame_index = (self.frame_index + 1) % len(self.frames)


def draw_frame(sheet, frame):
    """좌측 상단 좌표를 변환하고 모든 프레임을 고정 중심에 그린다."""
    left, top, width, height = frame
    sheet.clip_draw(left, sheet.h - top - height, width, height,
                    WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
                    width * SCALE, height * SCALE)


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
        sheet = pico2d.load_image(str(IMAGE_PATH))
        player = Player()
        previous = perf_counter()
        while handle_events():
            now = perf_counter()
            player.update(now - previous)
            previous = now
            pico2d.clear_canvas()
            draw_frame(sheet, player.frame)
            pico2d.update_canvas()
            pico2d.delay(0.01)
    finally:
        pico2d.close_canvas()


if __name__ == "__main__":
    main()
