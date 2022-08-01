

words =["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(words):
    my_dict = {}
    for word in words:
        sorted_word = "".join(sorted(word)) #sorted() => 결과가 리스트, 물자열로 변환해야한다.==> join()
        if my_dict.get(sorted_word): #딕셔너리에 애너그램 그룹이 존재한다
            my_dict[sorted_word].append(word) #존재하면 딕셔너리에 추가해준다
        else:
            my_dict[sorted_word] = [word]
    result = my_dict.values()
    
    return result

print(group_anagrams(words))
