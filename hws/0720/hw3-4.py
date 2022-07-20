s_triangle = input("3변의 길이를 연속하여 입력하세요 예) 3 4 5 ").split()

# print(type(s_triangle)) # 타입 확인하니 리스트다
a = float(s_triangle[0])
b = float(s_triangle[1])
c = float(s_triangle[2])
if (a + b < c) or (a + c < b) or (c + b < a):
    print('삼각형이 아닙니다')
elif a==b==c:
    print('정삼각형')
elif a==b!=c or a!=b==c or a==c!=b:
    print('이등변 삼각형')
elif (a**2 + b**2 ==c**2) or (a**2 + c**2 ==b**2) or (c**2 + b**2 ==a**2):
    print('직각삼각형')
else:
    print('삼각형')