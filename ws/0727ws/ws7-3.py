#0727 ws7-3
class Calculator:
    def __init__(self, a, b):
        self.a =a
        self.b =b

    def add(self):
        result = self.a + self.b
        return result
    
    def substract(self):
        result = self.a - self.b
        return result
    
    def multiply(self):
        result = self.a * self.b
        return result
    
    def divide(self):
        if self.b == 0:
            print("0으로는 나눌수 없어용")
        else:
            result = self.a/self.b
            return result

print(Calculator(1,2).add())
print(Calculator(2,1).substract())
print(Calculator(3,4).multiply())
print(Calculator(4,0).divide())