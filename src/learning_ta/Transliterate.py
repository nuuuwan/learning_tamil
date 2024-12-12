# Transliterate (T11e)


from learning_ta.TA_TO_ISO import TA_TO_ISO


class Transliterate:
    @staticmethod
    def ta_to_iso(ta: str) -> str:
        iso_list = []
        i = 0
        while i < len(ta):
            match = None
            for j in range(len(ta), i, -1):
                substring = ta[i:j]
                if substring in TA_TO_ISO:
                    iso = TA_TO_ISO[substring].title()
                    match = f"{substring}({iso})"
                    i = j - 1
                    break
            if match:
                iso_list.append(match)
            else:
                iso_list.append(ta[i])
            i += 1
        return "".join(iso_list)
