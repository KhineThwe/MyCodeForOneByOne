#pure endofpositional arg ko သူ့နောက်မှာ positional argument တွေထပ်မသုံးစေချင်တဲ့ အခြေအနေမျိုးမှာဆိုရင် သုံးတယ်
#keyword only arg ---> d=7
# keyword arg သူ့နောက်မှာလိုက်လို့ရသေးတယ် ----->**
#**

def myFun(a,b,*,c):
    print(a,b,c)

myFun(1,2,c=10)#c ka keyword only arg
