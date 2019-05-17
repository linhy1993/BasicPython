"""
假设你的计算机存储了很多乐曲。对于每个乐队,你都记录了其作
品被播放的次数。你要将这个列表按播放次数从多到少的顺序排列,从而将你喜欢的乐队排序
[156, 141, 35, 94, 88, 61, 111]
"""


def select_sorting(array):
    """
    遍历每个列表找出最小的数放在最前面
    :param array: list
    :return:
    """
    def find_smallest_one(rest_array):
        smallest_item = rest_array[0]
        smallest_item_index = 0
        for i in range(len(rest_array)):
            if rest_array[i] < smallest_item:
                smallest_item = rest_array[i]
                smallest_item_index = i
        return smallest_item_index

    result = []
    for i in range(len(array)):
        smallest_item_index = find_smallest_one(array)
        result.append(array.pop(smallest_item_index))
    return result


def main():
    array = [156, 141, 35, 94, 88, 61, 111]
    res = select_sorting(array)
    print(res)


if __name__ == '__main__':
    main()
