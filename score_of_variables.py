n = 10000#Global Variable

class MyClass:
    def __init__(self):
        self.n = 10#instance variable
        
    def myfunc(self):
        n = 100#local variable
        print(n)
        print(self.n)

print(n)
obj = MyClass()
print(obj.n)
obj.myfunc()