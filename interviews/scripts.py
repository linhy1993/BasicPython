def inverse_int(integer):
    # 反转一个整数，例如-123 --> -321
    if -10 < integer < 10:
        print(integer)
    else:
        str_int = str(integer)
        if str_int[0] == '-':
            inv_str = '-' + str_int[-1:0:-1]
        else:
            inv_str = str_int[-1::-1]
        print(inv_str)

def catch_file(dir, suffix):
    #设计实现遍历目录与子目录，抓取.pyc文件
    import os
    for root, dirs, files in os.walk(dir):
        for file in files:
            name, suf = os.path.splitext(file)
            if suf == suffix:
                print(file)
if __name__ == '__main__':
    inverse_int(-123)
    catch_file('/home/hng/PycharmProjects/BasicPython', '.pyc')