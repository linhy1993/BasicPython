# -*- coding: utf-8 -*-
# 最好的时间复杂度为O(nlogn)
# 最坏的时间复杂度为O(n2)
# 不稳定
def quick_sort(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] > mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value

    quick_sort(alist, first, low - 1)
    quick_sort(alist, low + 1, high)


if __name__ == '__main__':
    li = [1, 7, 4, 2, 5, 15, 12]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
