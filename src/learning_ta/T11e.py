# Transliterate (T11e)


from learning_ta.TA_TO_ISO import TA_TO_ISO


class T11e:
    @staticmethod
    def ta_to_iso(ta: str) -> str:
        iso = []
        i = 0
        while i < len(ta):
            match = None
            for j in range(len(ta), i, -1):
                substring = ta[i:j]
                if substring in TA_TO_ISO:
                    match = TA_TO_ISO[substring].title()
                    i = j - 1
                    break
            if match:
                iso.append(match)
            else:
                iso.append(ta[i])
            i += 1
        return "".join(iso)
