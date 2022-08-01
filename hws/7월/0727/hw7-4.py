#0727 hw_7-4

def collatz(n):
    count = 0
    while count <501:
        count +=1
        if n==1:
            count -=1
            break
        elif n % 2 ==0:
            n = n/2
            continue
        else:
            n = n*3 +1
    return count

print(collatz(6))
