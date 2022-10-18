#arbitrary argument or endofpositional argument
#* ပါတဲ့ argument ရဲ့နောက်မှာ argument တွေထပ်ထည့်လို့မရတော့လို့ သူ့ကို end of positional
#argument လို့လည်းခေါ်ကြတယ်
# def myFun(*args):
    # print(args) #tuple ponesan output ya mal
    # for d in args:
    #     print(d)

def myFun(a,b,c,*args):
    print(a)
    print(b)
    print(c)
    print(args)
    #a,b,c ka positional arguments tway 

myFun(1,2,3,4,5,5,6,6)
#myFun(1,2,3,4,5) #error
