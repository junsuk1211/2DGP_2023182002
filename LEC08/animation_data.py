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
