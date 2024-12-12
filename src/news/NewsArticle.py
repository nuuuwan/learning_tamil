import os
from dataclasses import dataclass
from functools import cached_property

from utils import WWW, JSONFile, Log, TSVFile

log = Log("NewsArticle")

# https://raw.githubusercontent.com/nuuuwan/news_lk3_data/refs/heads/main/ext_articles/0000808a.ext.json

# https://raw.githubusercontent.com/nuuuwan/news_lk3_data/refs/heads/main/articles/0000808a.json


@dataclass
class NewsArticle:
    # metadata
    newspaper_id: str
    time_str: str
    original_title: str
    n_original_body_lines: int
    hash: str
    time_ut: int
    original_lang: str
    url: str

    SUMMARY_TSV_PATH = os.path.join("data", "news", "summary.tsv")

    @classmethod
    def from_dict(Class, d: dict) -> "NewsArticle":
        return Class(**d)

    @classmethod
    def list_all(Class) -> list["NewsArticle"]:
        if not os.path.exists(Class.SUMMARY_TSV_PATH):
            raw_url = (
                "https://raw.githubusercontent.com"
                + "/nuuuwan/news_lk3_data/refs/heads/main/summary.tsv"
            )
            temp_path = WWW(raw_url).download()
            os.rename(temp_path, Class.SUMMARY_TSV_PATH)
            log.info(f"Wrote {Class.SUMMARY_TSV_PATH}")

        d_list = TSVFile(Class.SUMMARY_TSV_PATH).read()
        log.debug(
            f"Read {len(d_list):,} news articles from {Class.SUMMARY_TSV_PATH}"
        )
        news_article_list = [Class.from_dict(d) for d in d_list]
        news_article_list.sort(key=lambda x: x.time_ut, reverse=True)
        return news_article_list

    # details
    @cached_property
    def details_path(self) -> str:
        return os.path.join(
            "data", "news", "articles", "details", f"{self.hash}.json"
        )

    @cached_property
    def d_details(self) -> dict:
        if not os.path.exists(self.details_path):
            url_details = (
                "https://raw.githubusercontent.com"
                + "/nuuuwan/news_lk3_data/refs/heads/main"
                + f"/articles/{self.hash}.json"
            )
            os.rename(WWW(url_details).download(), self.details_path)
            log.info(f"Wrote {self.details_path}")
        return JSONFile(self.details_path).read()

    @cached_property
    def original_body_lines(self) -> list[str]:
        return self.d_details["original_body_lines"]

    # extended
    @cached_property
    def extended_path(self) -> str:
        return os.path.join(
            "data", "news", "articles", "extended", f"{self.hash}.json"
        )

    @cached_property
    def d_extended(self) -> dict:
        if not os.path.exists(self.extended_path):
            url_ext = (
                "https://raw.githubusercontent.com"
                + "/nuuuwan/news_lk3_data/refs/heads/main"
                + f"/ext_articles/{self.hash}.ext.json"
            )
            os.rename(WWW(url_ext).download(), self.extended_path)
            log.info(f"Wrote {self.extended_path}")
        return JSONFile(self.extended_path).read()

    @cached_property
    def en_title(self) -> str:
        return self.d_extended["translated_text"]["en"]["title"]

    @cached_property
    def en_body_lines(self) -> list[str]:
        return self.d_extended["translated_text"]["en"]["body_lines"]
