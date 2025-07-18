import os
from functools import cache

import openai
import requests
from utils import Hash, Log

log = Log("VisualDictionary")

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


class VisualDictionary:

    DIR_DATA_VISUAL_DICTIONARY = os.path.join("data", "visual_dictionary")
    T_TIMEOUT = 120
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        + " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110"
        + " Safari/537.3"
    }
    MODEL = "dall-e-3"
    DIM = 1024
    IMAGE_SIZE = f"{DIM}x{DIM}"

    @staticmethod
    @cache
    def __get_image_file_path__(en_sentence: str) -> str:
        h = Hash.md5(en_sentence)[:8]
        os.makedirs(
            VisualDictionary.DIR_DATA_VISUAL_DICTIONARY, exist_ok=True
        )
        return os.path.join(
            VisualDictionary.DIR_DATA_VISUAL_DICTIONARY, f"{h}.png"
        )

    @staticmethod
    def __generate_image__(en_sentence: str) -> str:
        log.debug(f'Generating image for "{en_sentence}"')
        image_file_path = VisualDictionary.__get_image_file_path__(
            en_sentence
        )
        assert not os.path.exists(image_file_path)

        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        prompt = "".join(
            [
                " Create a vivid image that unambiguously represents",
                f' the meaning of the sentence "{en_sentence}".',
                " Do not include any text in the image"
                " — no letters, words, or symbols.",
            ]
        )
        log.debug(f"{prompt=}")
        response = client.images.generate(
            model=VisualDictionary.MODEL,
            prompt=prompt,
            n=1,
            size=VisualDictionary.IMAGE_SIZE,
        )
        image_url = response.data[0].url
        log.debug(f"{image_url=}")

        response = requests.get(
            image_url,
            timeout=VisualDictionary.T_TIMEOUT,
            headers=VisualDictionary.HEADERS,
        )
        if response.status_code == 200:
            with open(image_file_path, "wb") as f:
                f.write(response.content)
        log.info(f"✅ Wrote {image_file_path}")

        return image_file_path

    @staticmethod
    def en_sentence_to_image(en_sentence: str) -> str:
        image_file_path = VisualDictionary.__get_image_file_path__(
            en_sentence
        )
        if not os.path.exists(image_file_path):
            VisualDictionary.__generate_image__(en_sentence)

        return image_file_path
