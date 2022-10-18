#positional arg  ---> p
#arbitary arg   -----> p
#keyword only arg 
#end of pos arg

# def myFun(a,b,c):
#     print(a)
#     print(b)
#     print(c)

# myList =[1,2,4,8,9,9]
# # myFun(myList)#d lo ထည့်ပေးလိုက်ရင်သူက Mylist ကို arg တစ်ခုအနေနဲ့ပဲကြည့်တယ်
# myFun(*myList)

#error up program



def myFun(a,b,*c):#here *c
    print(a)
    print(b)
    print(c)

myList =[1,2,4,8,9,9]
# myFun(myList)#d lo ထည့်ပေးလိုက်ရင်သူက Mylist ကို arg တစ်ခုအနေနဲ့ပဲကြည့်တယ်
myFun(*myList)



#error down program
# def myFun(a,b,*c,d):#here d
#     print(a)
#     print(b)
#     print(c)

# myList =[1,2,4,8,9,9]
# # myFun(myList)#d lo ထည့်ပေးလိုက်ရင်သူက Mylist ကို arg တစ်ခုအနေနဲ့ပဲကြည့်တယ်
# myFun(*myList)


def myFun(a,b,*c,d):#here d how to solve end of positional arg problem
    print(a)
    print(b)
    print(c)
    print(d)

myList =[1,2,4,8,9,9]
# myFun(myList)#d lo ထည့်ပေးလိုက်ရင်သူက Mylist ကို arg တစ်ခုအနေနဲ့ပဲကြည့်တယ်
myFun(*myList,d=7)
#arbit keyword 
#d ka keyword only argument

def myFun2(*c,x,d):
    print(c)
    print(d)
    print(x)

myFun2(1,2,3,x=4,d='hello')
