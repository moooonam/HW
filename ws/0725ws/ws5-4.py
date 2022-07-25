def sum_of_repeat_number(list):
    my_list = []
    for i in list:
        if list.count(i) == 1:
            my_list.append(i)
    return sum(my_list)

print(sum_of_repeat_number([4,4,7,8,10,4]))
        