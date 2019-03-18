# 1.让用户输入1-20，猜数字，可以猜5次。
# 2.每次有提示，大了，或者小了！
# 3.如果超过5次，提示game over.
import random

answer = random.randint(1, 20)
print("Welcome guess number!")
for i in range(0, 5):
    input_number = input("Input a number please:\n")
    if input_number.isnumeric():
        if int(input_number) > answer:
            print(f"Bigger than answer, left {4 - i} chance")
            continue
        elif int(input_number) < answer:
            print(f"Smaller than answer, left {4 - i} chance")
            continue
        else:
            print(f"Congratulations! The answer is {answer}")
            break
    else:
        print("Please input an integer number!")

    if i + 1 == 5:
        print("GG")
