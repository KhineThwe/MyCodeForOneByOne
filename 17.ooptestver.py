#adding attributes
class Myclass:
    def __init__(self,cat1,cat2):
        self.cat1 = cat1
        self.cat2 = cat2
    def mInfo(self):
        print('From mInfo',self.cat1,':',self.cat2)
obj1 = Myclass('apple','orange')
print(obj1.cat1,obj1.cat2)
obj1.mInfo()
#self ka data binding lote htr tr
