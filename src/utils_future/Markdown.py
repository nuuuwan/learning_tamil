class Markdown:
    @staticmethod
    def table(header_list: list[str], cell_list_list: list[list[str]]) -> str:
        table = []
        table.append("|".join(header_list))
        table.append("|".join(["---"] * len(header_list)))
        for cell_list in cell_list_list:
            table.append("|".join(cell_list))
        return "\n".join(table)

    @staticmethod
    def italic(s: str) -> str:
        s = s.strip()
        return f"*{s}*"
