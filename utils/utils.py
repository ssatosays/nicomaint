import requests
from bs4 import BeautifulSoup


def get_latest_articles():
    BASE_URL = "https://blog.nicovideo.jp"
    URL = f"{BASE_URL}/niconews/category/ge_maintenance/"
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.content, "html.parser", from_encoding="utf-8")
    result = soup.find_all("ul", class_="l-main l-main-list2")
    first_pagination = result[0]

    latest_articles = []
    links = first_pagination.find_all("a")
    for i, link in enumerate(links):
        article = {
            "index": i,
            "url": f"{BASE_URL}{link.get('href')}",
            "title": link.find("p", class_="l-main l-main-list2-title").text,
            "date": link.find("p", class_="l-main l-main-list2-date").text
        }
        latest_articles.append(article)
    return latest_articles


if __name__ == "__main__":
    print(get_latest_articles())
