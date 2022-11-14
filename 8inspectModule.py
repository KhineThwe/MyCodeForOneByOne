#function getsource and inspect module
import inspect#second
from inspect import isfunction,ismethod
import math
def myFun(x,y,z=10,*,kw1,kw2=2):
    return x*y
print(myFun.__name__)#name
print(myFun.__defaults__)#positional arguments tuple return
print(myFun.__kwdefaults__)#keyword only arguments dictionary return
print(myFun.__code__.co_varnames)#return function's var names into tuple type
print(myFun.__code__.co_argcount)#return positional arg's count
print(inspect.getsource(myFun))#function တစ်ခု name ကိုသိရုံနဲ့ ဆွဲထုတ်လို့ရတယ်
print(inspect.getcomments(myFun))
print(inspect.getmodule(print))#print ---> built-in
print(inspect.getmodule(ismethod))
print('checking is function',isfunction(myFun))
#function stands separately
print('checking is method',ismethod(myFun))
print(inspect.getmodule(math.sin))
#method သည် class တစ်ခု ထိန်းချုပ်မှုအောက်မှာရှိ

# class hello:
#     myFun() #method
#
# def myFun():#function
#     pass
