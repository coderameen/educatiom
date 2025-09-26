class Encap:
    n = 10#public
    _n = 100#protected
    __n = 1000#private
    
    def myfunc(self):
        print("This is class function")
        print("This is private variable: ",self.__n)
    

obj = Encap()
print("The public variable: ", obj.n)
print("This is protected variable: ",obj._n)
obj.myfunc()
 

    