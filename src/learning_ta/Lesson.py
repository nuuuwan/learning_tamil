import os
import re
from dataclasses import dataclass
from functools import cache

from utils import File, Log

from learning_ta.Translator import Translator
from learning_ta.Transliterate import Transliterate
from news import NewsArticle
from utils_future import Markdown

log = Log("Lesson")


@dataclass
class Lesson:
    news_article: NewsArticle

    @classmethod
    def from_news_article(Class, news_article: NewsArticle) -> "Lesson":
        return Class(
            news_article,
        )

    @property
    def md_path(self) -> str:
        return os.path.join("data", "lessons", f"{self.news_article.hash}.md")

    @property
    def lines_footer(self) -> list[str]:
        return [
            "",
            f"* Hash: {self.news_article.hash}",
            f"* Time: {self.news_article.time_str}",
            f"* URL: [{self.news_article.url}]({self.news_article.url})",
            "",
        ]

    @staticmethod
    @cache
    def clean(s):
        # replace common punctuation with space
        s = re.sub(r"[.,;:!?]", " ", s)

        # replace multiples spaces with single
        s = re.sub(r"\s+", " ", s)

        return s.strip()

    @property
    def lines(self) -> list[str]:
        lines = [
            f"# {self.news_article.original_title}",
        ]

        translator = Translator("ta", "en")
        for ta_line, en_line in zip(
            [
                self.news_article.original_title,
                *self.news_article.original_body_lines,
            ],
            [self.news_article.en_title, *self.news_article.en_body_lines],
        ):
            iso_line = Transliterate.ta_to_iso(ta_line)
            lines.extend(
                [
                    "## " + ta_line,
                    "",
                    iso_line,
                    "",
                    Markdown.italic(en_line),
                    "",
                ]
            )

            ta_words = ta_line.split(" ")
            ta_words = list(set(ta_words))
            ta_words.sort()

            cell_list_list = []
            for ta_word in ta_words:
                cleaned_ta_word = Lesson.clean(ta_word)
                if not cleaned_ta_word:
                    continue

                en_word = translator[cleaned_ta_word]
                if not en_word:
                    continue

                iso_word = Transliterate.ta_to_iso(ta_word)
                cell_list_list.append(
                    [
                        Markdown.bold(cleaned_ta_word),
                        iso_word,
                        Markdown.italic(en_word),
                    ]
                )

            lines.append(
                Markdown.table(
                    [Markdown.bold("Tamil"), "ISO", Markdown.italic("English")],
                    cell_list_list,
                )
            )

            lines.extend(["", "---", ""])

        return lines + self.lines_footer

    def write(self):
        File(self.md_path).write_lines(self.lines)
        log.info(f"Wrote {self.md_path}")
