class animal:
    def __init__(self,name,color,age,behavior):
        self.__name = name
        self.__color = color
        self.__age = age
        self.__behavior = behavior

class dog(animal):
    def dmodify(self,name,color,age,behavior):
        self.__name = name
        self.__color = color
        self.__age = age
        self.__behavior = behavior
    def dget_data(self):
        print(self.__name,self.__color,self.__age,self.__behavior)

dobj = dog("micky","yellow",5,"eat")
print(dobj.__dict__)
dobj.dmodify("micky","yellow",5,"eat")
dobj.dget_data()
