import os
from dataclasses import dataclass

from utils import File, Log

from learning_tamil.T11e import T11e
from news import NewsArticle

log = Log("Lesson")


@dataclass
class Lesson:
    hash: str
    time_str: str
    url: str
    tamil_lines: list[str]

    @classmethod
    def from_news_article(Class, news_article: NewsArticle) -> "Lesson":
        tamil_lines = [news_article.original_title]
        return Lesson(
            news_article.hash,
            news_article.time_str,
            news_article.url,
            tamil_lines=tamil_lines,
        )

    @property
    def txt_path(self) -> str:
        return os.path.join("data", "lessons", f"{self.hash}.txt")

    @property
    def lines(self) -> list[str]:
        return [
            f"Hash: {self.hash}",
            f"Time: {self.time_str}",
            f"URL: {self.url}",
            "",
            *self.tamil_lines,
        ] + [T11e.tamil_to_english(line) for line in self.tamil_lines]

    def write(self):
        File(self.txt_path).write_lines(self.lines)
        log.info(f"Wrote {self.txt_path}")
