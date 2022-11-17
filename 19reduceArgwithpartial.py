#reduce arg with partial fun
from functools import partial
def myFun(x,y,*args,x1,y1,**kwargs):
    print(x,y,args,x1,y1,kwargs)
# newFun = partial(myFun,10,x1='test')
# newFun(20,30,40,y1='test1',aa=100,bb=200)#with many parameters

newFun = partial(myFun,10,20,x1='test')
newFun(30,y1='testing',kw='keyword only')#with many parameters
