#arbitary argument or end of positional argument or variable-length argument
#* pr tae argument nout mhar argument tway htet htae ma ya tok loe 
#thu ko end of positional argument loe call tal 
def myFun(*args):
    print(type(args))
    for d in args:
        print(d)

myFun(1,2,3,3,4,6,4,55,8,0)#tuple pone san return pyan tal

def myFun2 (a,b,c,*args):
    print(a)
    print(b)
    print(c)
    print(args)
    #a,b,c ka positional argument tway
    

myFun2(1,2,3,3,4,6,4,55,8,0)#tuple pone san return pyan tal
myFun2(1,2,3)
