# my_list = [1,1,3,3,0,1,1,4] 
# re_list = list()
# i=0
# while True:
#     if i == len(my_list)-1:
#         break
#     if my_list[i] == my_list[i+1]:
#         re_list.append(my_list[i])
#         i = i+2
#     else:
#         re_list.append(my_list[i])
#         i = i+1
# print(re_list)


my_list = []
def f(s) :
    a = True  
    while a:     
        for i in s: 
            if len(my_list) == 0 :
                my_list.append(i)
            elif my_list[-1] != i : 
                my_list.append(i)
        a = False
    return my_list

print(f([1,1,3,3,0,1,1]))