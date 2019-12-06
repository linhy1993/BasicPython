def binary_search(array, item):
    """二分查找 递归"""
    n = len(array)
    if n > 0:
        mid = n // 2
        if item == array[mid]:
            return True
        elif item < array[mid]:
            return binary_search(array[:mid], item)
        else:
            return binary_search(array[mid + 1:], item)
    return False


def binary_search_2(array, item):
    n = len(array)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if item == array[mid]:
            return True
        elif item < array[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    print(binary_search([1, 2, 5, 8, 12, 20], 2))
    print(binary_search([1, 2, 5, 8, 12, 20], 3))
    print(binary_search_2([1, 2, 5, 8, 12, 20], 2))
    print(binary_search_2([1, 2, 5, 8, 12, 20], 3))
