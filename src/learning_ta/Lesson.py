import os
from dataclasses import dataclass

from utils import File, Log

from learning_ta.T11e import T11e
from news import NewsArticle

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
    def lines(self) -> list[str]:
        lines = [
            f"# {self.news_article.original_title}",
            "",
            f"* Hash: {self.news_article.hash}",
            f"* Time: {self.news_article.time_str}",
            f"* URL: [{self.news_article.url}]({self.news_article.url})",
            "",
        ]
        for ta_line, en_line in zip(
            [
                self.news_article.original_title,
                *self.news_article.original_body_lines,
            ],
            [self.news_article.en_title, *self.news_article.en_body_lines],
        ):
            iso_line = T11e.ta_to_iso(ta_line)
            lines.extend([ta_line, "", iso_line, "", en_line, "...", ""])

        return lines

    def write(self):
        File(self.md_path).write_lines(self.lines)
        log.info(f"Wrote {self.md_path}")
