import os
import logging


class BasicConfig(object):
    MONGO_URL = 'localhost'
    MONGO_DB = 'toutiao'
    MONGO_TABLE = 'toutiao'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    IMG_ROOT = os.path.join(PROJECT_ROOT, 'images')

    GROUP_START = 0
    GROUP_END = 3

    KEY_WORD = '街拍'


logging.basicConfig(
    filename='toutiao.log',
    filemode='w',
    format='%(levelname)-8s %(filename)-18s %(lineno)-4s %(message)s',
    level=logging.INFO
)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logging.getLogger().addHandler(console)
