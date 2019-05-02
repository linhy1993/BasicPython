import json
import re
import requests
from multiprocessing import Pool
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return None


def parse_one_page(html):
    pattern = re.compile('<li class="item pb-3 pt-3 border-bottom">.*?<a href="/items.*?>(.*?)</a>.*?authors.*?>(.*?)' +
                         '</a>' + '.*?img.*?src="(.*?)"' + '.*?<p>(.*?)</p>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'title': item[0],
            'author': item[1],
            'img_src': item[2],
            'summary': item[3].strip()
        }


def write_in_file(content):
    with open('res.txt', 'a') as f:
        f.write(json.dumps(content) + '\n')
        f.close()


def main(year):
    url = f'https://thegreatestbooks.org/the-greatest-fiction-from/{year}/to/{year + 1}'
    html = get_one_page(url=url)
    for item in parse_one_page(html):
        write_in_file(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(2000, 2015)])
