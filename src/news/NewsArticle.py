import os
from dataclasses import dataclass

from utils import WWW, Log, TSVFile

log = Log("NewsArticle")


@dataclass
class NewsArticle:
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
