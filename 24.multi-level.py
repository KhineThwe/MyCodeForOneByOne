#multi-level inheritance
class Parent:#based class
    def parent(self):
        print("This is from parent")
class Aunty(Parent):#base class
    def aunty(self):
        print("This is from Aunty")
class Child(Aunty):#derived class
    def child(self):
        print("This is from child")

obj = Child()
obj.aunty()
