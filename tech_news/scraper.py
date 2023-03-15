from parsel import Selector
import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
        time.sleep(1)

        return response.text
    except (requests.HTTPError, requests.Timeout):
        None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    urls = selector.css("h2.entry-title a::attr(href)").getall()

    return urls if urls else []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    url = selector.css("div.nav-links a.next::attr(href)").get()

    return url if url else None


# Requisito 4
def scrape_news(html_content: Selector):
    selector = Selector(text=html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("ul.post-meta li.meta-date::text").get()
    writer = selector.css("span.author a.url::text").get()
    reading_time = int((selector.css(
        "li.meta-reading-time::text").get()).split(" ")[0])
    summary = "".join(selector.css(
        "div.entry-content > p:first-of-type *::text").getall()).strip()
    category = selector.css("span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
