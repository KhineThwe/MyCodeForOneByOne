#@property
def myDec_1(fn):
    def inner():
        print('Running decorator 1')
        return fn()
    return inner

def myDec_2(fn):
    def inner():
        print('running decorator 2')
        return fn()
    return inner

@myDec_1
@myDec_2
def myFun():
    print('Running my fun')

myFun()

# result = myDec_1(myFun)
# result()
#
# result = myDec_1(myDec_2(myFun))#line 14 15 16 16 ရေးပုံနဲ့တူတယ်
# result()


