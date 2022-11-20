#Scope of variable
# Local,Global
#python ရဲ့ထူးခြားချက်တစ်ခုသည် var ko call use တဲ့ချိန်ကျရင် assign လုပ်ပေးရတယ် မလုပ်ပေးရင် unbound Local error တက်တယ်
# g = 10
# def myFun(n):
#     #how to change global var use---> global keyword
#     # global g
#     v= g**n
#     g = 20
#     return v
# print(myFun(2))
# print('global var g:',g)
#unbound local error condition

g = 10
def myFun(n):
    #how to change global var use---> global keyword
    global g
    g = 20
    v= g**n
    return v
print(myFun(2))
print('global var g:',g)#true

#nonlocal global var == global
#diff ---> global သည် အပြင်ဘက်ဆုံးမှာရှိတာဖြစ်ပြီးတော့
#nonlocal ka inside of function or nested function အတွင်းမှာရှိတတ်တယ်
