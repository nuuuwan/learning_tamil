import os
import re
from dataclasses import dataclass
from functools import cache

from utils import File, Log

from learning_ta.Translator import Translator
from learning_ta.Transliterate import Transliterate
from learning_ta.VisualDictionary import VisualDictionary
from news import NewsArticle
from utils_future import List, Markdown

log = Log("Lesson")


@dataclass
class Lesson:
    news_article: NewsArticle

    DIR_DATA_LESSONS = os.path.join("data", "lessons")

    @classmethod
    def from_news_article(Class, news_article: NewsArticle) -> "Lesson":
        return Class(
            news_article,
        )

    @property
    def date(self) -> str:
        return self.news_article.time_str[:10]

    @property
    def title(self) -> str:
        return Lesson.clean(self.news_article.en_title[:48]).replace(" ", "-")

    @property
    def md_path(self) -> str:
        return os.path.join(
            Lesson.DIR_DATA_LESSONS, f"[{self.date}] {self.title}.md"
        )

    @property
    def lines_article_data(self) -> list[str]:
        return [
            "",
            f"[{self.news_article.url}]({self.news_article.url})",
            "",
            f"`{self.news_article.time_str}`",
            "",
        ]

    @staticmethod
    @cache
    def clean(s):
        # replace common punctuation with space
        s = re.sub(r"[.,;:!?”“\"]", " ", s)

        # replace multiples spaces with single
        s = re.sub(r"\s+", " ", s)

        return s.strip()

    @staticmethod
    def get_dictionary_table_lines(
        translator: Translator, ta_line: str
    ) -> list[str]:
        ta_words = ta_line.split(" ")
        ta_words = List(ta_words).unique().raw

        cell_list_list = []
        i_row = 0
        for ta_word in ta_words:
            cleaned_ta_word = Lesson.clean(ta_word)
            if not cleaned_ta_word:
                continue
            en_word = translator[cleaned_ta_word]
            if not en_word:
                continue
            i_row += 1
            image_src = VisualDictionary.ta_to_image(ta_word)
            image_md = f"![{cleaned_ta_word}](../../{image_src})"
            cell_list_list.append(
                [
                    str(i_row),
                    Markdown.bold(cleaned_ta_word),
                    Transliterate.ta_to_iso(ta_word),
                    image_md,
                    Markdown.italic(en_word),
                ]
            )
        return [
            Markdown.table(
                [
                    "எண்",
                    Markdown.bold("தமிழ்"),
                    "ISO",
                    "Image",
                    Markdown.italic("English"),
                ],
                cell_list_list,
            )
        ]

    @property
    def tamil_lines(self) -> list[str]:
        return [
            self.news_article.original_title,
            *self.news_article.original_body_lines,
        ]

    @property
    def lines(self) -> list[str]:
        lines = [
            f"# {self.news_article.original_title}",
        ] + self.lines_article_data

        translator = Translator("ta", "en")
        for ta_line in self.tamil_lines:
            for ta_sentence in ta_line.split("."):
                cleaned_ta_sentence = Lesson.clean(ta_sentence)
                if not cleaned_ta_sentence:
                    continue
                en_sentence = translator[cleaned_ta_sentence]
                if not en_sentence:
                    continue
                lines.extend(
                    [
                        "## " + ta_sentence,
                        "",
                        Transliterate.ta_to_iso(cleaned_ta_sentence),
                        "",
                        Markdown.italic(en_sentence),
                        "",
                    ]
                )

                lines += self.get_dictionary_table_lines(
                    translator, ta_sentence
                )

            lines.extend(["", "---", ""])

        return lines

    def write(self):
        os.makedirs(Lesson.DIR_DATA_LESSONS, exist_ok=True)
        File(self.md_path).write_lines(self.lines)
        log.info(f"Wrote {self.md_path}")
