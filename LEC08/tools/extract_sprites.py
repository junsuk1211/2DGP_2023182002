"""Extract variable-size frames; Pillow is needed only when rebuilding assets."""
from pathlib import Path
import json
from PIL import Image

BASE = Path(__file__).resolve().parents[1]

def extract():
    source = Image.open(BASE / 'assets/naruto_source.png').convert('RGBA')
    # Exact sheet background: preserve dark outlines and anti-aliased artwork.
    pixels = source.load()
    for y in range(source.height):
        for x in range(source.width):
            if pixels[x, y][:3] == (0, 128, 0):
                pixels[x, y] = (0, 0, 0, 0)
    specs = json.loads((BASE / 'assets/source_regions.json').read_text())
    clips = {}
    frames = []
    for name, spec in specs.items():
        left, top, right, bottom = spec['region']
        spans, start = [], None
        for x in range(left, right + 1):
            occupied = x < right and source.crop((x, top, x + 1, bottom)).getbbox() is not None
            if occupied and start is None:
                start = x
            if not occupied and start is not None:
                spans.append((start, x))
                start = None
        clip_frames = []
        for index, (x1, x2) in enumerate(spans):
            crop = source.crop((x1, top, x2, bottom))
            bounds = crop.getbbox()
            sprite = crop.crop(bounds)
            frame = {'source': [x1 + bounds[0], top + bounds[1], sprite.width, sprite.height],
                     'width': sprite.width, 'height': sprite.height}
            clip_frames.append(frame)
            frames.append((sprite, frame))
        clips[name] = {'fps': spec['fps'], 'frames': clip_frames}
    cell_width = max(sprite.width for sprite, _ in frames) + 4
    cell_height = max(sprite.height for sprite, _ in frames) + 4
    atlas = Image.new('RGBA', (cell_width * len(frames), cell_height))
    for index, (sprite, frame) in enumerate(frames):
        x, y = index * cell_width + 2, 2
        atlas.paste(sprite, (x, y))
        frame['rect'] = [x, y, sprite.width, sprite.height]
    atlas.save(BASE / 'assets/naruto_atlas.png')
    (BASE / 'assets/animations.json').write_text(json.dumps(clips, indent=2) + '\n')
    print({name: len(clip['frames']) for name, clip in clips.items()})

if __name__ == '__main__':
    extract()
