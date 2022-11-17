from functools import partial
#partial fun --> higher order fun ဖြစ်တဲ့အတွက်သူ့ထဲမှာ fun ဖြတ်လို့ရတယ်
#partial fun ----> return new function
#takes two parameter ---> fun and preset value
def myFun(x,y,z):
    x=x+11
    y=y+11
    z=z+11
    print(x,y,z)
newFun = partial(myFun,10)#10 preset value gointo first arg x
#line 7 partial fun return -->
# def myFun(y,z):
    #print(x,y,z)
newFun(100,200)
