"""소닉 스프라이트 시트의 동작을 제자리에서 재생한다."""

from pathlib import Path
from time import perf_counter

import pico2d


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
SCALE = 10
FRAME_SECONDS = 0.1
REPEAT_COUNT = 5
PAUSE_SECONDS = 1.0
IMAGE_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")

# 프레임 영역은 원본 이미지의 좌측 상단 기준 (x, y, 너비, 높이)다.
ANIMATIONS = [
    ("대기", [
        (1, 39, 29, 39), (31, 40, 26, 38), (58, 39, 29, 39),
        (87, 40, 29, 38), (118, 40, 30, 38), (150, 40, 30, 38),
        (182, 40, 30, 38),
    ]),
    ("위 보기", [
        (212, 39, 28, 38), (240, 39, 29, 38),
    ]),
    ("웅크리기", [
        (270, 45, 24, 32), (302, 51, 29, 26),
    ]),
    ("걷기", [
        (8, 80, 26, 37), (37, 80, 27, 37), (65, 80, 31, 38),
        (97, 80, 37, 37), (135, 80, 32, 35), (170, 79, 32, 38),
        (206, 79, 26, 38), (238, 80, 24, 37), (263, 80, 30, 37),
        (295, 80, 36, 37), (334, 80, 32, 36), (370, 79, 29, 38),
    ]),
    ("달리기", [
        (1, 124, 33, 40), (39, 124, 35, 39), (89, 125, 35, 38),
        (130, 121, 34, 42), (181, 122, 34, 41), (228, 122, 33, 40),
    ]),
    ("몸 말기", [
        (1, 169, 29, 30), (35, 167, 29, 31), (67, 169, 30, 29),
        (98, 169, 31, 29), (131, 168, 29, 30), (162, 168, 29, 31),
        (193, 170, 30, 29), (230, 170, 31, 29), (268, 170, 30, 30),
    ]),
    ("회전", [
        (1, 206, 30, 27), (36, 206, 29, 27), (70, 206, 29, 27),
        (105, 206, 29, 27), (139, 206, 29, 27), (174, 206, 29, 27),
    ]),
    ("회전 준비", [
        (1, 239, 29, 35), (36, 239, 30, 35), (74, 239, 31, 35),
        (111, 238, 31, 36), (149, 239, 30, 35), (186, 238, 31, 36),
    ]),
    ("고속 회전", [
        (1, 283, 29, 35), (36, 283, 30, 35), (72, 286, 39, 31),
        (123, 285, 39, 32), (172, 286, 39, 31), (218, 285, 38, 32),
    ]),
    ("방향 전환", [
        (1, 326, 24, 45), (31, 327, 29, 44), (65, 327, 20, 44),
        (90, 327, 25, 43), (119, 327, 25, 43), (149, 327, 20, 44),
    ]),
    ("피격", [
        (184, 341, 40, 28), (232, 341, 39, 27),
    ]),
    ("제동", [
        (1, 379, 27, 38), (31, 379, 31, 36), (64, 379, 31, 36),
        (99, 377, 33, 38), (136, 379, 32, 36), (176, 379, 33, 36),
        (217, 379, 33, 36), (254, 378, 33, 36),
    ]),
    ("넘어짐", [
        (6, 429, 34, 40), (49, 426, 34, 43),
    ]),
    ("균형 잡기", [
        (96, 427, 23, 39), (125, 427, 23, 39),
    ]),
]


class Player:
    def __init__(self):
        self.animation_index = 0
        self.frame_index = 0
        self.completed = 0
        self.waiting = False
        self.elapsed = 0.0

    @property
    def frames(self):
        return ANIMATIONS[self.animation_index][1]

    @property
    def frame(self):
        return self.frames[self.frame_index]

    def update(self, dt):
        self.elapsed += dt
        while True:
            duration = PAUSE_SECONDS if self.waiting else FRAME_SECONDS
            if self.elapsed < duration:
                break
            self.elapsed -= duration
            if self.waiting:
                self.animation_index = (self.animation_index + 1) % len(ANIMATIONS)
                self.frame_index = 0
                self.completed = 0
                self.waiting = False
                continue
            self.frame_index += 1
            if self.frame_index == len(self.frames):
                self.completed += 1
                if self.completed == REPEAT_COUNT:
                    self.frame_index = len(self.frames) - 1
                    self.waiting = True
                else:
                    self.frame_index = 0


def validate_frames(sheet):
    for name, frames in ANIMATIONS:
        if not frames:
            raise ValueError(f"프레임이 없는 동작: {name}")
        for left, top, width, height in frames:
            if (left < 0 or top < 0 or width <= 0 or height <= 0
                    or left + width > sheet.w or top + height > sheet.h):
                raise ValueError(f"이미지 범위를 벗어난 프레임: {name}")
            if width * SCALE > WINDOW_WIDTH or height * SCALE > WINDOW_HEIGHT:
                raise ValueError(f"화면 크기를 벗어난 프레임: {name}")


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
        validate_frames(sheet)
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
