import unittest

from learning_ta import Translator


class TestCase(unittest.TestCase):
    def test_translate(self):
        translator = Translator("ta", "en")
        for ta_word, expected_translation in [
            ["கடல்", "Sea"],
            ["மழை", "Shower"],
            ["சூரியன்", "Sun"],
        ]:
            actual_translation = translator[ta_word]
            self.assertEqual(actual_translation, expected_translation)
