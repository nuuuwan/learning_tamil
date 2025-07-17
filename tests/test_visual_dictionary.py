import unittest

from learning_ta import VisualDictionary


class TestCase(unittest.TestCase):
    def test_ta_to_image(self):
        for ta_word, expected_image_path in [
            ["கடல்", None],
        ]:
            actual_image_path = VisualDictionary.ta_to_image(ta_word)
            self.assertEqual(actual_image_path, expected_image_path)
