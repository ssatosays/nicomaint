import json
import os
import requests
from bs4 import BeautifulSoup

JSON_PATH = './utils/articles.json'


def _read_json() -> list:
    with open(JSON_PATH, 'r') as f:
        return json.load(f)


def _update_json(target: list):
    with open(JSON_PATH, 'w') as f:
        json.dump(target, f, indent=4, ensure_ascii=False)


def _del_sent_articles(latest_articles: list):
    if not os.path.exists(JSON_PATH):
        _update_json(latest_articles)
        return
    la_titles = [l['title'] for l in latest_articles]
    rj_titles = [r['title'] for r in _read_json()]
    latest = list(set(la_titles) - set(rj_titles))
    if len(latest) > 0:
        _update_json(latest_articles)
        diff = []
        for title in latest:
            for la in latest_articles:
                if title == la['title']:
                    diff.append(la)
        latest_articles.clear()
        latest_articles.extend(diff)
    else:
        latest_articles.clear()


def get_latest_articles():
    BASE_URL = 'https://blog.nicovideo.jp'
    URL = f'{BASE_URL}/niconews/category/ge_maintenance/'
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='utf-8')
    result = soup.find_all('ul', class_='l-main l-main-list2')
    first_pagination = result[0]

    latest_articles = []
    links = first_pagination.find_all('a')
    for i, link in enumerate(links, start=1):
        latest_articles.append({
            'index': i,
            'url': f"{BASE_URL}{link.get('href')}",
            'title': link.find('p', class_='l-main l-main-list2-title').text,
            'date': link.find('p', class_='l-main l-main-list2-date').text
        })
    _del_sent_articles(latest_articles)
    return latest_articles


if __name__ == '__main__':
    print(get_latest_articles())
