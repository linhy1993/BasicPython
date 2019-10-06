# -*- coding: utf-8 -*-
# 最优时间复杂度是O(n), 升序排序
# 最坏时间复杂度是O(n2)
# 稳定性是稳定的
def insert_sort(array):
    n = len(array)
    for j in range(1, n):
        i = j
        while i > 0:
            if array[i] < array[i - 1]:
                array[i - 1], array[i] = array[i], array[i - 1]
                i -= 1
            else:
                break
    print(array)


def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if array[i] < array[i - gap]:
                    array[i], array[i - gap] = array[i - gap], array[i]
                    i -= 1
                else:
                    break
        gap = gap // 2
    print(array)


if __name__ == '__main__':
    insert_sort([2, 1, 31, 10, 8, 9])
    shell_sort([2, 1, 31, 10, 8, 9])
