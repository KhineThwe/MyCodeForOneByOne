#doc string က function ရဲ့ body အတွက် ဆိုရင် function annotation က function
#ထဲသို့ဖြတ်သွားမည့် argument,parameter တွေအ တွက်ဖြစ်တယ်
#funAnnotation.py
#PEP 3107
#https://peps.python.org/pep-3107/
# def myFun(a:<expression>,b:<expression>)-><expression>:
# def myFun(a:'annotation of a',b:'annotation of b')->'return of function':
#     return a*b
# print(myFun.__annotations__)
def myFun(a:'annotation of a',b:'annotation of b')->'return of function':
    """this is body expression for myFun"""
    return a*b
print(myFun.__annotations__)
print(myFun.__doc__)

# x = 3
# y = 5
# def myFun1(a:'some value from funCall')->'multiply'+str(max(x,y))+'times':
#     """Doc ....will return multiply by of max"""
#     return a*max(x,y)
# data = myFun1(2)
# print(data)
# print(myFun1.__annotations__)
# print(myFun1.__doc__)


x = 3
y = 5
def myFun1(a:'some value from funCall',b:'some value from function call')->'multiply'+str(max(x,y))+'times':
    """Doc ....will return multiply by of max"""
    return b+a*max(x,y)
data = myFun1(2,4)
print(data)
print(myFun1.__annotations__)
print(myFun1.__doc__)


