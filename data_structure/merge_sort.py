# -*- coding: utf-8 -*-
# 最优复杂度O(nlogn)
# 最坏复杂度O(nlogn)
# 稳定
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist

    mid = n // 2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    # merge
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    li = [1, 7, 4, 2, 5, 15, 12]
    print(li)
    li_sorted = merge_sort(li)
    print(li_sorted)
