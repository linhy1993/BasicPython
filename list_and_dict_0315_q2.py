"""
2.寻找班级里面名字最长的人
我有一串字符串人名:
names=(' Kunpen Ji, Li XIAO, Caron Li,' ' Dongjian SHI, Ji ZHAO, Fia YUAN Y,' ' Wenxue DING, Xiu XU, Haiying WANG, Hai LIN,' ' Jey JIANG, Joson WANG E,' ' Aiyang ZHANG, Haiying MENG,' ' Jack ZHANG E, Chang Zhang, Coron ZHANG')

我希望能做到下面3点：
问题1：排序,按照姓名A-Z排序
问题2：找出里面姓”ZHANG”有几个
问题3：找出名字里面最长的人

"""


def sort_name_string(name):
    # 排序,按照姓名A-Z排序
    names_lst = names.split(',')
    names_lst_remove_space = [name.strip() for name in names_lst]
    print("sorted name:")
    print(sorted(names_lst_remove_space))


def find_name_include(name):
    # 找出里面姓”ZHANG”
    names_lst = names.split(',')
    names_lst_remove_space = [name.strip() for name in names_lst]
    names_with_word = [n for n in names_lst_remove_space if '{}'.format(name) in n]
    print("Find Named ZHANG Count:")
    print(len(names_with_word))


def find_longest_name(names):
    # 找出名字里面最长的人
    names_lst = names.split(',')
    names_lst_remove_space = [name.replace(' ', '') for name in names_lst]
    name_length_dict = {name: len(name) for name in names_lst_remove_space}
    max_length = max(name_length_dict.values())
    name_with_max_length = [k for k in name_length_dict if name_length_dict[k] == max_length]
    print("Find Longest Name:")
    print(name_with_max_length)


if __name__ == '__main__':
    names = ('Kunpen Ji, Li XIAO, Caron Li,'
             'Dongjian SHI, Ji ZHAO, Fia YUAN Y,'
             'Wenxue DING, Xiu XU, Haiying WANG, Hai LIN,'
             'Jey JIANG, Joson WANG E,'
             'Aiyang ZHANG, Haiying MENG,'
             'Jack ZHANG E, Chang Zhang, Coron ZHANG')

    sort_name_string(names)
    find_name_include('ZHANG')
    find_longest_name(names)
