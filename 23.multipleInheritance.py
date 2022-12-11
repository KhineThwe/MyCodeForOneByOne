#multiple inheritance
class Parent:
    def parent(self):
        print("This is from parent")
class Aunty:
    def aunty(self):
        print("This is from Aunty")
class Uncle:
    def uncle(self):
        print("This is from Uncle")

class Child(Parent,Aunty,Uncle):
    def child(self):
        print("This is from child")

obj = Child()
obj.aunty()
