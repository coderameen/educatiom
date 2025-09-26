#Heirarchical In
class Parent:
    def pdisplay(self):
        print("This is parent property")
        
class Child1(Parent):
    def c1display(self):
        print("This is child 1 property")
class Child2(Parent):
    def c2display(self):
        print("This is child 2 property")
class Child3(Parent):
    def c3display(self):
        print("This is child 3 property")
        
c1 = Child1()
c1.c1display()
c1.pdisplay()

c2 = Child2()
c2.c2display()
c2.pdisplay()
