#decorator with counter application

def counter(fn):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count+=1
        print('function{0} was called {1}'.format(fn.__name__,count) )
        return fn(*args,**kwargs)
    return inner
def add(a,b=0):
    """adding two value using decorator"""
    print(a+b)
def sub(a,b=0):
    """sub two values using decorator"""
    print(a-b)
result = counter(add)
result(10,20)
result(30,40)

resultSub = counter(sub)
resultSub(10,5)
