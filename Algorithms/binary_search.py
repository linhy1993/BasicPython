"""
对于包含n个元素的列表,用二分查找最多需要log2(n)步,而简单查找最多需要n步
仅当列表是有序的时候,二分查找才管用
函数 binary_search 接受一个有序数组和一个元素。如果指定的元素包含在数组中,这个
函数将返回其位置
"""


def binary_search(order_list, item):
    """
    :param order_list: 一个有序数组
    :param item: 一个元素
    :return: 如果指定的元素包含在数组中,这个函数将返回其位置
    """
    low_index = 0
    high_index = len(order_list) - 1

    while low_index <= high_index:
        mid_index = int((low_index + high_index) / 2)
        if order_list[mid_index] == item:
            return mid_index
        elif item < order_list[mid_index]:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return None


def main():
    order_lst = [1, 2, 3, 4, 5, 6, 7]
    item = 8
    result = binary_search(order_lst, item)
    if result:
        print(f'Find item {item} in {result}th position')
    else:
        print('Not found anything in list')


if __name__ == '__main__':
    main()
