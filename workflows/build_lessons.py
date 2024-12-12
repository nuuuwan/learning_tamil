from learning_tamil import Lesson
from news import NewsArticle


def main():
    news_article_list = NewsArticle.list_all()
    tamil_news_article_list = [
        news_article
        for news_article in news_article_list
        if news_article.original_lang == "ta"
    ]
    latest_tamil_news_article_list = tamil_news_article_list[:10]
    lesson_list = [
        Lesson.from_news_article(news_article)
        for news_article in latest_tamil_news_article_list
    ]
    for lesson in lesson_list:
        lesson.write()


if __name__ == "__main__":
    main()
