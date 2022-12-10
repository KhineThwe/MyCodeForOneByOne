#function တွေက decorator ထဲကိုဖြတ်တဲ့အခါကျရင် function တစ်ခုရဲ့ doc string က ပျောက်သွားတယ် doc string သာ
# မရှိတော့ရင် အဲ့ function က ဘာတွေအလုပ်လုပ်လဲဆိုတာမသိနိုင်တော့ဘူး အဲ့လိုပြသနာကို ဖြေရှင်းနိုင်ဖို့အတွက် wrapper ကို အသုံးပြုတယ်
#to solve
from functools import wraps
def log(fn):
    @wraps(fn)#higher order function pl arg anay nae takes one function
    def with_log(*args,**kwargs):
        print(fn.__name__+"was called")
        return fn(*args,**kwargs)
    return with_log

@log
def myFun(x):
    """Some operation just like arithmetic"""
    return x+x+x

@log
def myFun2(x):
    """From myFun2 """
    return x+x+x

myFun(5)
print(myFun.__name__)
print(myFun.__doc__)#None

myFun2(20)
print(myFun2.__name__)
print(myFun2.__doc__)#None
