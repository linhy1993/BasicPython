'''
假如我们有一个目录里面包含若干个文件和子目录
问题1:我们要统计该目录下有多少个文件并显示出来(包含子目录)
问题2:该目录总共的大小可以按M,也可以按K显示
问题3:该目录下最大的文件和最小的文件，以及对应的大小
目录为你的python，环境目录
'''
import os
from os.path import getsize
BASEDIR = os.path.abspath(os.path.dirname(__file__))

def get_all_files(path):
    res = []
    size = 0
    size_order = {}
    for root, dirs, files in os.walk(path):
        for filespath in files:
            size_order[os.path.join(root, filespath)] = getsize(os.path.join(root, filespath))
            res.append(os.path.join(root, filespath))
            size += getsize(os.path.join(root, filespath))

    return res, size, size_order


if __name__ == '__main__':
    res, size, size_order = get_all_files(BASEDIR)
    print(f"Total files are: {len(res)}")
    print(f"Size is {size / 1024 /1024}, Mbytes")
    smallest_file = sorted(size_order.items(), key = lambda k:k[1])[0]
    largest_file = sorted(size_order.items(), key = lambda k:k[1])[-1]
    print(f"Largest File Name is {largest_file[0]}, size is {largest_file[1] / 1024 / 1024} Mbytes")
    print(f"Smallest File Name is {smallest_file[0]}, size is {smallest_file[1] / 1024 / 1024} Mbytes")
