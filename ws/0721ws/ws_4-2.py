students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

my_set = set(students)
#print(my_set)
#{'조민지', '김철수', '이영희', '박해피', '강디티', '김해킹', '한케이'}
# a = students.count('조민지')
# print(a)
result = {}

for i in students:
    if i not in result:
        result[i] = 1
    else:
        result[i] +=1

print(result)