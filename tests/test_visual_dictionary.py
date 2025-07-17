import os
import unittest

from learning_ta import VisualDictionary


class TestCase(unittest.TestCase):
    def test_ta_to_image(self):
        for ta_word, expected_image_path in [
            [
                "கடல்",
                os.path.join(
                    VisualDictionary.DIR_DATA_VISUAL_DICTIONARY,
                    "0dca56b3.png",
                ),
            ],
        ]:
            actual_image_path = VisualDictionary.ta_to_image(ta_word)
            self.assertEqual(actual_image_path, expected_image_path)
