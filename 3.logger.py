#logger application
#ကိုယ်ရေးတဲ့ fun or decorator ထဲမှာ ပဲ Module တွေရေးရင်ပိုရှင်းတယ်
def logger(fn):
    from functools import wraps
    from datetime import datetime,timezone

    @wraps(fn)
    def inner(*args,**kwargs):
        dt = datetime.now(timezone.utc)
        result = fn(*args,**kwargs)
        print('{0} : called {1}: recent data : {2}'.format(dt,fn.__name__,result))
        return result
    return inner
#above decorator function

@logger
def myFun1(x,y):
    """From fun 1"""
    return x+y

@logger
def myFun2():
    """from function 2"""
    return 10
myFun1(10,20)
myFun2()

