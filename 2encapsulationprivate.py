#encapsulation private
class Parent:
    def __init__(self,age):
        self.__age = age

class Child(Parent):
    def modify(self,input):
        self.__age = input#modify လုပ်တာ
        return self.__age
    def get_data(self):
        # self.__age = 30
        print(self.__age)

# p = Parent(30)
# print(p.__age)#Attribute error tat mal

obj = Child(30)
print(obj.__dict__)
print(obj.modify(50))
print(obj.__dict__)
obj.get_data()
