#higher order
#function တစ်ခုကနေ တခြားသော function ကိုကိုယ့်ရဲ့ argument အနေနဲ့ ပြန်သုံးချင်တယ် သုံးတဲ့
#function ကို higher order function လို့ခေါ်တယ်။
#myFun is higher order function
def myFun(x,fn):
    return fn(x)
value = myFun(5,lambda y:y**2)
print(value)

#higher order function ထဲမှာ arg and kwargs pass
#higher order function ထဲမှာကိုက တခြားfunction ရှိနေတယ်
def myFun1(fn,*args,**kwargs):
    return fn(*args,**kwargs)
value1 = myFun1(lambda x,y:x**y,2,3)
value2 = myFun1(lambda x,y:x+y,2,y=20)
print(value1)
print(value2)

