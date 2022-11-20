#non local
def outerFun():
    d = 'green'
    def innerFun1():
        def innerFun2():
            print("The most inner2",d)#non local nae ma change htr loe d lo pl output ထွက်တယ်
        innerFun2()
        nonlocal d#beacuse of this
        d = 'python'
        print('inner fun 1',d)
    innerFun1()
    print('Outer ',d)

outerFun()
#The most inner2 green
# inner fun 1 python
# Outer  python
