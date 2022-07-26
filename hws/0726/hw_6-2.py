# hw_6-4
def mass_percent():
    salt = 0 # 소금 양
    water = 0 # 소금물의 양
    count = 1 
    while count < 6:
        a = input(f"{count}.소금물의 농도(%)와 소금물의 양(g)을 입력하시오: ex) 5%%100g")
        if a == "Done" :     #Done을 입력하면 멈춤
            break 
        b = a.split('%')
        salt += int(b[0])   # '%'를 기준으로 단어를 나누어  % 앞에있는 농도를 가져와 누적합한다
        water += int(b[1].split('g')[0])   # 'g' 앞에있는 수를 가져와 누적합한다.
       
        count +=1
    return print(f"{100*salt/water:.2f}%{water}g")    
mass_percent()