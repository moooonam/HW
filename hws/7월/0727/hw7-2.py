# 0727 hw7-2
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs +=1
        Doggy.birth_of_dogs +=1

    def bark(self):
        print("멍멍멍멍멍!!!!!")

    def get_status():
        print(f"태어난강아지수 :{Doggy.birth_of_dogs}, 강아지수:{Doggy.num_of_dogs}")
    
    def death(self):
        Doggy.num_of_dogs -=1

dog1 = Doggy('코코', '비숑')
dog2 = Doggy('흰둥이', '비숑')
dog3 = Doggy('탱이', '푸들')
dog4 = Doggy('ㅠㅠ', 'ㅠㅠ')
dog1.bark()
Doggy.get_status()
dog4.death()
Doggy.get_status()

