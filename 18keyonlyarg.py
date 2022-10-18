#keyword only argument
#list pass to fun

def myFun(a,b,c):
    print(a)
    print(b)
    print(c)

myList =[1,2,4]
# myFun(myList)#d lo ထည့်ပေးလိုက်ရင်သူက Mylist ကို arg တစ်ခုအနေနဲ့ပဲကြည့်တယ်
myFun(*myList)#ae lo ma phyit ag * nae ဖြတ်ရတယ် but 3 ခု 3 ခု မို့အဆင်ပြေတာ
