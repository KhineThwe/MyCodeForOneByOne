#class built-in function ---> 4 ku shi
#1.getattr(obj's name,attr's name)
#2.setattr(obj,name,value) ဘယ် obj ထဲက ဘယ် attr ကိုဘယ် value set up lote ma ll
#3.delattr(obj,name)
#4.hasattr(obj,name)#obj name ,obj's attr shi yin true ma shi yin false
class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
sobj = Student("NCCstu",101,24)#parameterized constructor
print(getattr(sobj,'name'))
setattr(sobj,'age',23)
print(getattr(sobj,'age'))
delattr(sobj,'age')
print(hasattr(sobj,'age'))
