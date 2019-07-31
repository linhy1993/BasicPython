import re

import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine


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


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    movies_info = soup.find_all(name='div', attrs={"class": "movie-item-info"})
    for movie in movies_info:
        title = movie.find(attrs={'name'}).get_text()
        star = movie.find(attrs={'star'}).get_text()
        time = movie.find(attrs={'releasetime'}).get_text()

        yield {
            'title': clean_string(title),
            'star': clean_string(star),
            'time': clean_string(time)
        }


def main():
    for i in range(0, 100, 10):
        # get page index
        html = get_page_index(offset=i)
        for movie_info in parse_html(html):
            print(movie_info)
            # save in db

if __name__ == '__main__':
    main()
