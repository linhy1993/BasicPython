import json
import os
import re
import logging
from hashlib import md5
from multiprocessing.pool import Pool
from urllib.parse import urlencode
from json import JSONDecodeError
import pymongo
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from toutiao.config import BasicConfig

logger = logging.getLogger(__name__)

client = pymongo.MongoClient(BasicConfig.MONGO_URL, connect=False)
db = client[f'{BasicConfig.MONGO_DB}']

HEADERS = {
    'accept': 'application / json, text / javascript',
    'accept - encoding': 'gzip, deflate, br',
    'accept - language': 'zh - CN, zh; q = 0.9, en; q = 0.8, fr; q = 0.7',
    'content - type': 'application / x - www - form - urlencoded',
    'cookie': 'tt_webid=6684047013610440196; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16a57c9646d448-02fe5e946a799e-36697e04-384000-16a57c9646ea52; tt_webid=6684047013610440196; csrftoken=c95a047ca5c73ca0d71ad0ad03e0f9e0; uuid="w:7c98dc6a41934eeab36115a06838ecd7"; __tasessionId=738vudnc31556374308099; CNZZDATA1259612802=278262223-1556248060-https%253A%252F%252Fwww.google.com%252F%7C1556371728; s_v_web_id=3e9f73082247f6d6e0ffc8eb3bbae3cb',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}


def get_page_index(offset, keyword):
    data = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': 1556374347326
    }

    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        logger.debug('请求索引页面出错')
        return None


def parse_one_page(html):
    try:
        data = json.loads(html)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        pass


def get_page_detail(url):
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        logger.debug('请求详情页面出错')
        return None


def parse_get_page(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    pattern = re.compile('img src&#x3D;&quot;(.*?)&quot;', re.S)
    image = re.findall(pattern, html)
    if image:
        for i in image:
            download_img(i)
        return {
            'title': title,
            'url': url,
            'image': image
        }
    else:
        change_pattern = re.compile(r'gallery: JSON.parse.*?\(\"(.*?)\"\)', re.S)
        image = re.search(change_pattern, html)
        if image:
            json_data = image.group(1).replace('\\', '')
            data = json.loads(json_data)
            if data and 'sub_images' in data.keys():
                sub_images = data.get('sub_images')
                images = [item.get('url') for item in sub_images]
                for i in images:
                    download_img(i)
                return {
                    'title': title,
                    'url': url,
                    'image': images
                }


def save_to_mongo(result):
    if db[BasicConfig.MONGO_TABLE].insert_one(result):
        logger.debug('Save in DB', result)
        return True
    return False


def download_img(url):
    logger.info(f"Download {url} image")
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException:
        logger.debug('请求Image出错')
        return None


def save_image(content):
    file_path = f'{BasicConfig.IMG_ROOT}/{md5(content).hexdigest()}.jpg'
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def main(offset):
    html = get_page_index(offset, BasicConfig.KEY_WORD)
    for url in parse_one_page(html):
        html_detail = get_page_detail(url)
        if html_detail:
            result = parse_get_page(html_detail, url)
            if isinstance(result, dict):
                save_to_mongo(result)


if __name__ == '__main__':
    groups = [x * 2 for x in (BasicConfig.GROUP_START, BasicConfig.GROUP_END)]
    pool = Pool()
    pool.map(main, groups)
