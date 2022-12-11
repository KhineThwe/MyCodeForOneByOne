class Animal:
    color = 'yellow'#yoe yoe so public
    age = 2
    #behavior
    def eat(self):
        print('Animal is eating')

class Dog(Animal):
    def bark(self):
        print('Dog is barking')

dobj = Dog()
dobj.age =5
dobj.color = 'black'
print(dobj.color)
print(dobj.age)
