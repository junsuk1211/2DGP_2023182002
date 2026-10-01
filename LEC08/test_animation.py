"""Run with: python -m unittest discover -s LEC08 -v"""
from pathlib import Path
import json
import unittest
from animation_data import load_clips
from playback import Playback

BASE = Path(__file__).resolve().parent

class AnimationTests(unittest.TestCase):
    def setUp(self):
        self.clips = load_clips(BASE / 'assets/animations.json')
        self.player = Playback(self.clips)

    def test_sheet_frame_counts_and_dimensions(self):
        self.assertEqual([len(c.frames) for c in self.clips], [6, 6, 5, 12])
        data = json.loads((BASE / 'assets/animations.json').read_text())
        for clip in self.clips:
            for frame, raw in zip(clip.frames, data[clip.name]['frames']):
                self.assertEqual((frame.width, frame.height), tuple(raw['source'][2:]))
                self.assertGreater(frame.width, 0)
                self.assertGreater(frame.height, 0)

    def test_every_frame_in_five_repetitions_then_pause(self):
        for clip_index, clip in enumerate(self.clips):
            p = Playback(self.clips)
            p.clip_index = clip_index
            for index in range(len(clip.frames) * 5):
                p.elapsed = (index + 0.5) / clip.fps
                self.assertEqual(p.frame_index, index % len(clip.frames))
                self.assertFalse(p.is_paused)
            p.elapsed = p.active_duration
            self.assertTrue(p.is_paused)
            self.assertEqual(p.frame_index, len(clip.frames) - 1)
            p.update(0.999)
            self.assertEqual(p.clip_index, clip_index)
            p.update(0.001)
            self.assertEqual(p.clip_index, (clip_index + 1) % 4)
            self.assertEqual(p.frame_index, 0)

    def test_large_time_step_and_full_cycle(self):
        duration = sum(len(c.frames) / c.fps * 5 + 1 for c in self.clips)
        self.player.update(duration * 3 + 0.2)
        self.assertEqual(self.player.clip_index, 0)
        self.assertAlmostEqual(self.player.elapsed, 0.2)
        self.assertEqual(self.player.frame_index, 2)

    def test_negative_time_does_not_reverse(self):
        self.player.update(-1)
        self.assertEqual(self.player.elapsed, 0)

if __name__ == '__main__':
    unittest.main()
