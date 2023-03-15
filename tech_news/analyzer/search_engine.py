from tech_news.database import search_news
import datetime


# Requisito 7
def search_by_title(title):
    return [
        (news["title"], news["url"])
        for news in search_news({"title": {"$regex": title, "$options": "i"}})
    ]


# Requisito 8
def search_by_date(date):
    try:
        date_format = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        return [
            (news["title"], news["url"])
            for news in search_news({"timestamp": date_format})
        ]

    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
