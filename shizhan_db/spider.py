import re

import requests
from bs4 import BeautifulSoup
from shizhan_db.db import Database
from dateutil import parser


def get_page_index(offset):
    if offset == 100:
        offset -= 1
    url = f'https://maoyan.com/board/4?offset={offset}'
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.text
    except Exception:
        return None


def clean_string(input_str):
    string = re.sub('\s+', ' ', input_str)
    output_str = string.strip()
    return output_str


def parse_ymd(input_str):
    return parser.isoparse(input_str)


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    movies_info = soup.find_all(name='div', attrs={"class": "board-item-content"})
    for movie in movies_info:
        name = movie.find(name='p', attrs={'name'}).get_text()
        stars = movie.find(name='p', attrs={'star'}).get_text()[3:]
        time = movie.find(name='p', attrs={'releasetime'}).get_text()[5:]
        release_time = re.sub(u"\\(.*?\\)", "", time)
        score = movie.find(name='p', attrs={'score'}).get_text()

        yield {
            'name': clean_string(name),
            'stars': clean_string(stars),
            'release_time': parse_ymd(release_time),
            'score': score
        }


def main():
    db = Database(truncate=True)
    for i in range(0, 100, 10):
        # get page index
        html = get_page_index(offset=i)
        for movie_info in parse_html(html):
            print(movie_info)
            db.insert_movie(name=movie_info['name'],
                            stars=movie_info['stars'],
                            release_time=movie_info['release_time'],
                            score=movie_info['score'])
    db.close_db()


if __name__ == '__main__':
    main()
