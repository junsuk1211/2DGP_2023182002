"""Deterministic playback clock without graphics dependencies."""
class Playback:
    def __init__(self, clips):
        self.clips = clips
        self.clip_index = 0
        self.elapsed = 0.0

    @property
    def clip(self):
        return self.clips[self.clip_index]

    @property
    def frame_index(self):
        return int(self.elapsed * self.clip.fps + 1e-9) % len(self.clip.frames)

    def update(self, dt):
        self.elapsed += max(0.0, dt)
