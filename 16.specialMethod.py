#adding attributes
class Myclass:
    def __init__(self,xAxis,yAxis):#special method
        self.xAxis = xAxis
        self.yAxis = yAxis
obj1 = Myclass(10,20)#class ကိုခေါ်တာနဲ့ init ka အလုပ်စလုပ်တယ် special method moe loe
print(obj1.xAxis,obj1.yAxis)
