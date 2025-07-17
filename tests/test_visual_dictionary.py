import os
import unittest

from learning_ta import VisualDictionary


class TestCase(unittest.TestCase):
    def test_ta_to_image(self):
        for ta_word, expected_hash in [
            ["அரிசித்", "2922aa25"],
            ["ஜனாதிபதி", "2460fa3d"],
            ["வர்த்தகர்கள்", "5037bda0"],
        ]:
            expected_image_path = os.path.join(
                VisualDictionary.DIR_DATA_VISUAL_DICTIONARY,
                f"{expected_hash}.png",
            )
            actual_image_path = VisualDictionary.ta_to_image(ta_word)
            self.assertEqual(actual_image_path, expected_image_path)
