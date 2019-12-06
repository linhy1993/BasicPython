def bubble_sort(array_list: list):
    for i in range(len(array_list)):
        count = 0  # 优化的话要考虑到如果一开始就是顺序排序的话就不需要再遍历
        for j in range(len(array_list) - i - 1):
            if array_list[j] > array_list[j + 1]:
                array_list[j], array_list[j + 1] = array_list[j + 1], array_list[j]
                count += 1
        if 0 == count:
            break
    print(array_list)


if __name__ == '__main__':
    bubble_sort([2, 4, 6, 5, 3, 1])
    bubble_sort([1, 2, 3, 4, 5, 6])
