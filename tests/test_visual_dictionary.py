import os
import unittest

from learning_ta import VisualDictionary


class TestCase(unittest.TestCase):
    def test_ta_to_image(self):
        for en_sentence, expected_hash in [
            ["Demonstration asking for rice to Pongal", "729619a6"],
            ["The country is coming", "0bcb829e"],
            [
                "Therefore, the protesters have suggested that the"
                " government take appropriate action to eliminate the"
                " control price and address the shortage of rice.",
                "87e80b21",
            ],
        ]:
            expected_image_path = os.path.join(
                VisualDictionary.DIR_DATA_VISUAL_DICTIONARY,
                f"{expected_hash}.png",
            )
            actual_image_path = VisualDictionary.en_sentence_to_image(
                en_sentence
            )
            self.assertEqual(actual_image_path, expected_image_path)
