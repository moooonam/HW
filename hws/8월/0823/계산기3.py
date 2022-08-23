def hoo(a):
    icp = {'*':2, '+':1, '(':3}
    isp = {'*':2, '+':1, '(':0}
    stack = []
    num_list = []
    for i in range(len(a)):
        if a[i].isdigit():
            num_list.append(a[i])
            continue
        else:
            if not stack:
                stack.append(a[i])
                continue

            elif stack:
                if a[i] == ')':
                   while stack[-1] != '(':
                       num_list.append(stack.pop())
                   stack.pop()

                elif icp[a[i]] > isp[stack[-1]]:
                    stack.append(a[i])

                else:
                    while icp[a[i]] <= isp[stack[-1]]:
                        num_list.append(stack.pop())
                    stack.append(a[i])
    return num_list
def calcul(b):
    stack = []      
    for i in range(len(b)):
        if b[i].isdigit():
            stack.append(b[i])
        else:
            r = int(stack.pop())
            l = int(stack.pop())
            if b[i] == "+":
                stack.append(r+l)
            elif b[i] == "*":
                stack.append(r*l)
    return stack

for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    result = calcul(hoo(arr))
    print(f"#{tc} {result[0]}")