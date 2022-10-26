#keyword argument ----> **
#keyword argument ko use mal so yin tok tuple anay nae ma hoke pl dictionary 
#anay nae pl return pyan pay tal

#key ရော value ရောလိုချင်ပြီးသူ့နောက်မှာ တခြားကောင်တွေထပ်မလိုက်စေချင်တဲ့ အခြေအနေမျိုးမှာသုံးတယ်
def myFun(**key):
    print(key)

myFun(a=10,b=20,c=30)


#end of positional arg vs keyword arg
# def myFun2(a,b,*,**kw):
#     print(a)
#     print(b)
#     print(kw)
# myFun2(a=10,b=20,c=30)
#named arguments must follow bare * ----> error shi tal

#to solve thu doe 2 ku kyar htl ko (keyword only argument ) shi loe ya dal
#end of positional arg (keyword only argument) keyword arg

def myFun2(a,b,*,koa,**kw):
    print(a)
    print(b)
    print(kw)
    print(koa)
myFun2(a=10,b=20,c=30,koa=101)
