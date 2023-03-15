from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    news = find_news()
    category_list = Counter(
        sorted([new["category"] for new in news])).most_common(5)
    return [category[0] for category in category_list]
