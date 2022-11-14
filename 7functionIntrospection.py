#function introspection
#function's built-in attribute -> annotation,docs
#မူရင်းပါလာသော attribute တွေနေရာမှာ own attribute ထည့်ခြင်းကို function introspection လို့ခေါ်တယ်
def myFun(x,y):
    return x+y
print(dir(myFun))#to show built - in attribute
myFun.__subject__ = 'bio'
myFun.__mark__ = 99
print(dir(myFun))
print(myFun.__subject__)#to show property
print(myFun.__mark__)
