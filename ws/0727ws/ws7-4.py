# 0727 hw7-4

def fee(a, b):
    c = 1200*(a/10) # 대여 요금
    if a % 30 > 20:  # 보험료 
        c += (a/30+1)*525
    else:
        c += (a/30)*525
    
    if b > 100:
        c += 100*170 + (b-100)*85
    else:
        c += b*170

    return c

print(fee(600, 50)) 
print(fee(600, 110)) 
     