#adding attributes
class Myclass:
    def myMethod(self):#normal method call mha work mhar
        self.x = 10
        self.y = 20

obj1 = Myclass()
obj1.myMethod()#switch button
#obj1 ka self nay yar ko win thwar tr
print(obj1.x,obj1.y)

obj2 = Myclass()
obj2.myMethod()
print(obj2.x,obj2.y)
