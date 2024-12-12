class List:
    def __init__(self, raw: list):
        self.raw = raw

    def unique(self):
        new_raw = []
        for raw_item in self.raw:
            if raw_item not in new_raw:
                new_raw.append(raw_item)
        return List(new_raw)
