import os
from functools import cache, cached_property

from googletrans import Translator as GoogleTranslator
from utils import JSONFile, Log

log = Log("Translator")


class Translator:
    GOOGLE_TRANSLATOR = GoogleTranslator()

    def __init__(self, lang_src, lang_dest):
        self.lang_src = lang_src
        self.lang_dest = lang_dest

    @cached_property
    def __idx_path__(self) -> str:
        return os.path.join(
            "data", "translator", f"{self.lang_src}_{self.lang_dest}.idx"
        )

    @property
    def __idx__(self) -> dict[str, str]:
        if not os.path.exists(self.__idx_path__):
            return {}

        return JSONFile(self.__idx_path__).read()

    def __set_idx__(self, s: str, translated_s: str):
        new_idx = self.__idx__
        new_idx[s] = translated_s
        new_idx = dict(sorted(new_idx.items()))
        JSONFile(self.__idx_path__).write(new_idx)

    @cache
    def __translate_nocache__(self, s: str) -> str:
        s = s.strip()
        if not s:
            return ""
        result = self.GOOGLE_TRANSLATOR.translate(
            s, src=self.lang_src, dest=self.lang_dest
        )
        if result:
            translated_s = result.text
            log.debug(f'"{s}" -> "{translated_s}"')
            return translated_s
        raise Exception(
            f'Failed to translate "{s}" ({self.src}) to {self.dest}'
        )

    def __getitem__(self, s: str) -> str:
        if s in self.__idx__:
            return self.__idx__[s]

        translated_s = self.__translate_nocache__(s)
        self.__set_idx__(s, translated_s)
        return translated_s
