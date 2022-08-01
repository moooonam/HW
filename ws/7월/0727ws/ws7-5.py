#0727 ws7-5
class Matching:
    def __init__(self, name):
        
        self.name = name
    def pick(self, n):
        
        import random
        list_s = random.sample(self.name, n)
        return list_s
    def match_pair(self):
        import random
        my_list = []
        count = 0
        while count == len(self.name)/2:
            sample1 = random.sample(self.name, 2)
            my_list.append(sample1)
            count += 1
        return my_list

list_n = ['a','b','c','d','e','f']

a = Matching(list_n)
print(a.pick(4))
print(a.match_pair())


