class StudentClass:
    #constructors
    def __init__(self,name,age):
        self.name = name#instance variable
        self.age = age
    def myfunc(self,marks):
        print(f"The Name is {self.name} and age is {self.age} and the marks is: {marks}")
        
s1 = StudentClass("bob", 27)
s1.myfunc(98)  

