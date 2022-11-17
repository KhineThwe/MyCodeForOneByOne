#Reduce Function
#takes two parameter function yal iterable yal
#ကျွန်တော်တို့ရေးလိုက်တဲ့ function တစ်ခုမှာ fun,no of code line အရေအတွက် နည်းအောင် လုပ်ပေးတယ်
#python 2 mhar ka pr tal
#python 3 mhar
import functools
list = [1,2,3,4,5,6]
print("The sum of all elements from list: ",end="")
print(functools.reduce(lambda a,b:a+b,list))
print(functools.reduce(lambda a,b:a if a<b else b,list))
print(functools.reduce(lambda a,b:a if a>b else b,list))
#reduce function ma use yin code line 5,6 lines kone naing tal

