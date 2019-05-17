def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        left_array = [i for i in array[1:] if i <= pivot]
        right_array = [i for i in array[1:] if i > pivot]

        return quick_sort(left_array) + [pivot] + quick_sort(right_array)
