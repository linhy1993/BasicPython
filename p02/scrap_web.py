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

    df = pd.DataFrame(res, columns=['person_name', 'create_time', 'content'])
    df.to_csv('test.csv', index=None, header=True, encoding='utf-8', mode='a')

def clean_conten(content):
    """remove html tag

    :param content:
    :return:
    """
    reg = re.compile('^[^>]*>')
    content = reg.sub('',content).replace('\n','').replace(' ','')
    res = re.sub(r"\s+", " ", content)
    # titile decode
    return res

def get_person_post(person_post):
    """Get information from json

    :param json_obj:
    :return:
    """
    resp_data = person_post['resp_data']
    content, create_time, person_name = [], [], []
    topics = resp_data['topics']
    for i in range(len(topics)):
        content.append(clean_conten(topics[i]['topic']['talk']['text']))
        # TODO: clean content
        create_time.append(topics[i]['topic']['create_time'])
        person_name.append(topics[i]['topic']['talk']['owner']['name'])

    total_res = {'person_name': person_name, 'create_time': create_time, 'content': content}
    save_into_csv(total_res)


def decode_url(url):
    r = requests.get(url, headers=HEADERS)
    data = r.json()
    if len(data['resp_data']['topics']) > 0:
        get_person_post(data)
    else:
        raise AttributeError


def main():
    index = 0
    while True:
        url = f'https://api.zsxq.com/v1.10/search/topics?count=30&scope=joined&index={index}&keyword=2019%E5%AE%9E%E6%88%98%E7%AC%AC%E4%BA%8C%E6%9C%9F'
        index += 30
        try:
            decode_url(url)
        except AttributeError:
            break


if __name__ == '__main__':
    main()
