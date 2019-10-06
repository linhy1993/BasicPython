# -*- coding: utf-8 -*-
# 时间复杂度O(n2), 空间复杂度O(n2)
# 不稳定

def select_sort(array):
    n = len(array)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i, n):
            if array[min_index] > array[j]:
                array[min_index], array[j] = array[j], array[min_index]
    print(array)


if __name__ == '__main__':
    select_sort([2, 3, 1, 10, 8, 9])
    select_sort([12, 23, 11, 110, 8, 9])
