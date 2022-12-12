#opeartor overloading
class People:#id age
    def __init__(self,id,age):
        self.id = id
        self.age = age

    def __add__(self,self1):
        data_id = self.id + self1.id
        data_age = self.age + self1.age
        return data_age,data_id

p1 = People(123,20)
p2 = People(124,20)
p3 = People(125,20)

total = p1+p2
# finalTotal = total+p3
did,dage = total
p4 = People(did,dage)
finalTotal = p4+p3
did,dage = finalTotal
result = did + dage
print(result)
