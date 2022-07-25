# 0725 hw 5-2

def leap_year(n):
    if n % 4 == 0 and n % 100 != 0:
        print(f'{n}년은 윤년입니다.')
    elif n % 400 == 0:
        print(f'{n}년은 윤년입니다.')
    else:
        print(f'{n}년은 윤년이 아닙니다.')

leap_year(2021)


