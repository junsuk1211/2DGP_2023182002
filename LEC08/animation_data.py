"""Frame metadata uses top-left image coordinates, independent of Pico2D."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Frame:
    x: int
    y: int
    width: int
    height: int

@dataclass(frozen=True)
class Clip:
    name: str
    fps: float
    frames: tuple[Frame, ...]

def load_clips(path):
    import json
    data = json.loads(path.read_text(encoding='utf-8'))
    return tuple(Clip(name, data[name]['fps'],
                      tuple(Frame(*frame['rect']) for frame in data[name]['frames']))
                 for name in ('run', 'walk', 'jump', 'y_combo'))
