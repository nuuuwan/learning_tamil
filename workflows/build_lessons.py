from utils import Log

from learning_ta import Lesson
from news import NewsArticle

log = Log("build_lessons")


def main():
    news_article_list = NewsArticle.list_all()
    ta_news_article_list = [
        news_article
        for news_article in news_article_list
        if news_article.original_lang == "ta"
    ]
    log.debug(f"Found {len(ta_news_article_list):,} Tamil news articles")
    LIMIT = 1
    latest_ta_news_article_list = ta_news_article_list[:LIMIT]
    log.debug(
        f"Building lessons for {len(latest_ta_news_article_list):,} articles"
    )
    lesson_list = [
        Lesson.from_news_article(news_article)
        for news_article in latest_ta_news_article_list
    ]
    for lesson in lesson_list:
        lesson.write()


if __name__ == "__main__":
    main()
