password = '1234'
i=0
while i<3:
    if input('비밀번호 숫자4자리를 입력하시요') == password:
        print('로그인 성공')
        break
    else:
        i += 1
        print('다시 입력하세요')
