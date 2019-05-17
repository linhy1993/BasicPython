# # factorial
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)
#
# res = factorial(5)
#
# print(res)

# sum_iter
def sum_func(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_func(array[1:])

print(sum_func([2,4,6]))

