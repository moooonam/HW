# 0725 hw 5-4
# 문제 1
def fn_d(n):
    a = 0
    for i in str(n):
        a += int(i)
    a += n    
    return(a)
# 문제 2
# 100 이하의 숫자 판단
my_list = list()

def is_selfnumber(n):
    for i in range(0,101):
        my_list.append(fn_d(i))
    if n in my_list:
        print(f'{n}은 self number가 아닙니다.')
    else:
        print(f'{n}은 self number 입니다')
    
is_selfnumber(3)
is_selfnumber(4)






