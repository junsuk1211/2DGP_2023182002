"""Deterministic playback clock without graphics dependencies."""
class Playback:
    def __init__(self, clips):
        self.clips = clips
        self.clip_index = 0
        self.elapsed = 0.0

    @property
    def clip(self):
        return self.clips[self.clip_index]

    REPEATS = 5

    @property
    def active_duration(self):
        return len(self.clip.frames) / self.clip.fps * self.REPEATS

    @property
    def repetition(self):
        return min(self.REPEATS, int(self.elapsed / (len(self.clip.frames) / self.clip.fps)) + 1)

    @property
    def frame_index(self):
        if self.elapsed >= self.active_duration:
            return len(self.clip.frames) - 1
        return int(self.elapsed * self.clip.fps + 1e-9) % len(self.clip.frames)

    def update(self, dt):
        self.elapsed += max(0.0, dt)
