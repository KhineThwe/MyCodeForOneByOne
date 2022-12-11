#inheritance
#OOP ---> 4 ku shi
#1.Inheritance---> multiple inheritance , multi-level inheritance
#multiple inheritance --> class အများကြီးကနေ inheritance လုပ်တာ
#class A class B class C ------> class D
#multi-level inheritance
#တစ်ဆင့် တစ်ဆင့် ချင်းဆက်ပြီး inheritance lote htr tae pone san
#2.Data Abstraction
#3.Encapsulation
#4.Polymorphism
class Animal:
    def eat(self):
        print('Animal is eating')

class Dog(Animal):
    def bark(self):
        print('Dog is barking')

dobj = Dog()
dobj.bark()
dobj.eat()
