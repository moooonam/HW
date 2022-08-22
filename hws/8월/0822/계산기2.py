for tc in range(1, 11):
    n = int(input()) 
    my_str = input() 
    stack = []
    result = ""
    icp = {"+": 1, "*" : 2}
    for i in my_str:
        if "0" <= i <= "9":
            result += i
            continue
        if len(stack) == 0:
            stack.append(i)
            continue
        while len(stack) and icp[stack[-1]] >= icp[i]:
            result += stack.pop()
        stack.append(i)

    while len(stack):
        result += stack.pop()

    n = len(result)
    stack2 = []
    for i in range(n):
        if "0" <= result[i] <= "9":
            stack2.append(result[i])
        else:
            if result[i] == '*':
                stack2.append(int(stack2.pop()) * int(stack2.pop()))
            elif result[i] == '+':
                stack2.append(int(stack2.pop()) + int(stack2.pop()))
            else:
                stack2.pop()
    print(f"#{tc} {stack2[0]}")