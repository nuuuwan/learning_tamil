# Transliterate (T11e)
# write or print (a letter or word) using
# the closest corresponding letters of a different alphabet or script.
# "names from one language are often transliterated into another"

from learning_tamil.TA_TO_EN import TA_TO_EN


class T11e:
    @staticmethod
    def tamil_to_english(tamil: str) -> str:
        english = []
        i = 0
        while i < len(tamil):
            match = None
            for j in range(len(tamil), i, -1):
                substring = tamil[i:j]
                if substring in TA_TO_EN:
                    match = TA_TO_EN[substring].title()
                    i = j - 1
                    break
            if match:
                english.append(match)
            else:
                english.append(tamil[i])
            i += 1
        return "".join(english)
