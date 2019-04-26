from urllib.parse import unquote

import pandas as pd
import requests
import re

HEADERS = {
    'Host': 'api.zsxq.com',
    'Referer': 'https://wx.zsxq.com/dweb/',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': '_uab_collina=155239836559829643197203; upload_channel=qiniu; ws_address=wss%3A//ws.zsxq.com/ws%3Fversion%3Dv1.10%26access_token%3D0FECE3E2-7296-C8BB-CE84-8194A4D34638; user_id=844445115515512; name=%u6797%u4F18%u79C0%uD83C%uDF3B; avatar_url=https%3A//images.zsxq.com/FpdzBy2BnjsP8XTIJ0jw1o-0Lq6C%3Fe%3D1906272000%26token%3DkIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD%3AxJI9AowWRXBI87cHF_Y8RAFh-uw%3D; UM_distinctid=16972270ebb1aa-0336120a50eb108-72206752-1fa400-16972270ebc61; zsxq_access_token=0FECE3E2-7296-C8BB-CE84-8194A4D34638'
}


def save_into_csv(res):
    """Use pandas to save in csv file

    :param res:
    :return:
    """

    df = pd.DataFrame(res, columns=['person_name', 'topic', 'create_time', 'content'])
    df.drop_duplicates(inplace=True)
    df.to_csv('test.csv', index=None, header=True, encoding='utf-8', mode='a')


def clean_conten(content):
    """remove html tag

    :param content:
    :return:
    """
    reg = re.compile('^[^>]*>')
    content = reg.sub('', content).replace('\n', '').replace(' ', '')
    res = re.sub(r"\s+", " ", content)
    # titile decode
    return res


def find_title(text):
    try:
        title_raw = re.findall('title=\"(.*)\"\s', text)[0]
        title = unquote(title_raw, 'utf-8')
        return title
    except IndexError:
        return text


def get_person_post(person_post):
    """Get information from json

    :param json_obj:
    :return:
    """
    resp_data = person_post['resp_data']
    topic, content, create_time, person_name = [], [], [], []
    topics = resp_data['topics']
    for i in range(len(topics)):
        topic.append(find_title(topics[i]['topic']['talk']['text']))
        content.append(clean_conten(topics[i]['topic']['talk']['text']))
        create_time.append(topics[i]['topic']['create_time'])
        person_name.append(topics[i]['topic']['talk']['owner']['name'])

    total_res = {'person_name': person_name, 'topic': topic, 'create_time': create_time, 'content': content}
    # save_into_csv(total_res)
    return person_name, topic, create_time, content


def decode_url(url):
    r = requests.get(url, headers=HEADERS)
    data = r.json()
    if len(data['resp_data']['topics']) > 0:
        person_name, topic, create_time, content = get_person_post(data)
        return person_name, topic, create_time, content
    else:
        raise AttributeError


def main():
    person_name_lst, topic_lst, create_time_lst, content_lst = [], [], [], []
    index = 0
    while True:
        url = f'https://api.zsxq.com/v1.10/search/topics?count=30&scope=joined&index={index}&keyword=2019%E5%AE%9E%E6%88%98%E7%AC%AC%E4%BA%8C%E6%9C%9F'
        index += 30
        try:
            person_name, topic, create_time, content = decode_url(url)
            person_name_lst.extend(person_name)
            topic_lst.extend(topic)
            create_time_lst.extend(create_time)
            content_lst.extend(content)
        except AttributeError:
            break
    total_res = {'person_name': person_name_lst, 'topic': topic_lst, 'create_time': create_time_lst,
                 'content': content_lst}
    save_into_csv(total_res)


if __name__ == '__main__':
    main()
