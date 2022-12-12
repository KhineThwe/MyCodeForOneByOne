# Python contains a special type of method called Magic Methods or Special Methods or Dunder Methods. These methods have two underscores before and after their name.
#https://pythongeeks.org/python-operator-overloading/
class Number:
   def __init__(self, num):
       self.num = num
   def __neg__(self):
       print("Negative Operator")
       return self.num
n1 = Number(5)
print(-n1)
