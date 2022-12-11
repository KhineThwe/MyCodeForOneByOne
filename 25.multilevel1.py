class Base1:
    def multi(self,a,b):
        return a*b
class Base2(Base1):
    def Adding(self,a,b):
        return a+b
class Derived(Base2):
    def sub(self,a,b):
        return a-b

obj = Derived()
print(obj.multi(10,20))
