"""
1-1题目:替换1-20内的数字，3的倍数和5的倍数用不同的数字代替
列出1到20的数字，若是3的倍数就用apple代替，若是5的倍数就用orange代替，若既是3的倍数又是5的倍数就用appleorange代替。
"""
number=[]
for i in range(1, 21):
    if i % 3 == 0 and i % 5 ==0:
        number.append('appleorange')
    elif i % 3 == 0:
        number.append('orange')
    elif i % 5 == 0:
        number.append('apple')
    else:
        number.append(str(i))
    print('apple'[i % 3 * len('apple')::] + 'orange'[i % 5 * len('orange')::] or i)
print(' '.join(number))

"""
1-2题目：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码，使用 Python 如何生成 200 个激活码 
类似这样：总长12 ：字母和数字的混合 
no1. 6L3A3O8C8KAR no.2 QJP38MR4RSPY
"""
import random, string

activate_code = [''.join(random.sample(string.ascii_uppercase + string.digits, 12)) for i in range(200)]
print(activate_code)