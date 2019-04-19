"""
时间和日期的综合小练习
1.计算你的生日比如近30年来(1990-2019)，每年的生日是星期几,统计一下星期几出现的次数比较多
2,生日提醒,距离生日还有几天
"""
import datetime
week_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def find_day(birthday):
    print(datetime.date.weekday(birthday))

    gap_year = datetime.date.today().year - birthday.year
    day_lst = []

    for i in range(gap_year):
        birthday_temp = datetime.date(birthday.year + i, 11, 10)
        day = datetime.date.weekday(birthday_temp)
        day_lst.append(day)
        print(f'{week_name[day]} is the day of {birthday_temp.year} year')

    print(f'\n{week_name[max(day_lst)]} is the most day')

def remind_birthday(birthday):
    present_year = datetime.date.today().year\

    distance_day = datetime.date(present_year, birthday.month, birthday.day) -  datetime.date.today()

    if distance_day.days < 0:
        distance_day = datetime.date(present_year + 1, birthday.month, birthday.day) -  datetime.date.today()

    print(f'\nAfter {distance_day.days} is the next birthday')


def main():
    date_of_birth = input("Input your birthday, ex. 1993-11-10:\n")
    try:
        y, m, d = date_of_birth.split('-')
        birthday = datetime.date(int(y), int(m), int(d))
    except Exception:
        print('Format Error, please input as year-month-day!')
    else:
        find_day(birthday)
        remind_birthday(birthday)

if __name__ == '__main__':
    main()