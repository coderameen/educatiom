#overriding
class Parent:
    def display(self):
        print("This is parent property")
        
class Child(Parent):
    def display(self):
        print("This is child property")    
        super().display() 
c = Child()
c.display()