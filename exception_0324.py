"""
题目：
编写一个迷你的计算器，支持两个数加，减，乘，除
要求提示用户输入2个数字和一个运算符号，比如1,2,+

提示：
这个题目里面需要有几个地方检查
第一:是输入的参数，用户可能会乱输入，这个地方要有判断
第二:输入的参数要合法运算的适合，要考虑异常，比如9/0这样的肯定不对
第三:输入的参数，尤其是数字，可能是浮点，比如1.1,-10,-0.09
"""
import re


def validate_number(num):
    pattern = re.compile(r"^(-?\d)(\.\d+)?$")
    return True if re.match(pattern, num) else False


def validate_operation(operation):
    return operation in ["+", "-", "*", "/"]


def mini_calculator():
    input_number = input("Input two numbers and operator, like 1,2,+:\n")
    try:
        args = input_number.split(',')
        if len(args) == 3:
            a, b, operator = args
            if validate_number(a) and validate_number(b) and validate_operation(operator):
                res = eval(f'{a}{operator}{b}')
                print(f"{a}{operator}{b} = {res}")
            else:
                print("Input Error")
        else:
            print("Input Length Not Correct!")
    except ValueError:
        print("Value Error")
    except Exception as e:
        print(f'{e}')


if __name__ == '__main__':
    mini_calculator()
