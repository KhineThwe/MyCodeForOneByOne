##Memory allocation
# data တွေ program memo ပေါ် ဘယ်လိုနေရာယူသလဲ။
# stack memory        heap memory 
#       !                    !
#    Functions          10,20,30>Objects
#    Methods
#    သိမ်း
# #Variables are memory reference.
# memory reference ကသာ data value တွေကိုလှမ်းထောက်ထားတယ်။
# eg: var a----->0*1008-------->10
# eg:a=10
#a = 10 ဆိုတာ var a ထဲမှာ ၁၀ ကို သိမ်းထားတာမဟုတ်ဘူး 
#a = 0*1008(reference)----> 10 object
#a ဆိုသောကောင်သည် memory reference ကိုကိုင်ထားတယ် ထို memory reference ကမှ objectဖြစ်တဲ့ real value  ကို လှမ်းထောက်ထားခြင်းဖြစ်သည်။
#Variables are memory reference.
#လူတွေရဲ့နေတဲ့အိမ်တွေမှာလည်း တစ်ခန်းနဲ့တစ်ခန်း address လေးတွေရှိသလိုပဲ memory 1 ကန့် 1 ကန့်မှာလည်း address တွေရှိတယ်

a = 10
print(id(a))#a ရဲ့ adress ကိုသိချင်ရင် id ဆိုတဲ့ fun နဲ့သုံး built-in fun
print(hex(id(a)))
# in python,value tu yin memory 1 ku hlt mhar store tl.eg:a=10 and b=10
#a နှင့် b သည် 10 ဆိုလျှင် name မတူသော်လည်း value တူညီသောကြောင့် memory ၏ တစ်နေရာထဲတွင် သွား၍ သိမ်းသည်။
b = 10
print(id(b))#a ရဲ့ adress ကိုသိချင်ရင် id ဆိုတဲ့ fun နဲ့သုံး built-in fun
print(hex(id(b)))


#C programming language မှာဆိုရင်တော့ name မတူ value တူညီနေရင်တောင် သွား store တဲ့ memory အကန့် နေရာမတူပါဘူး


c = 5
d = 5
print(hex(id(a)))
print(hex(id(b)))
if id(a) == id(b):
    print("They are same memory address!")
else:
    print("They are not same memory address!")


