from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass
class ConcreteClass(MyAbstractClass):
    def my_abstract_method(self):
        print("MY IMPLEMENTATION DETAILS")
obj = ConcreteClass()
obj.my_abstract_method()   