#docstring
#document string
#built in ပါတဲ့ function တွေ သို့ ကျွန်တော်တို့ကိုယ်တိုင်ရေးထားတဲ့ function တွေ မှာ ပါတဲ့ string
#doc string တွေကို ကျွန်တော်တို့ interpreter ကနေ သိတယ် comment နဲ့မတူဘူး
#doc string သည် သူ့အပေါ်မှာ comment ကလွဲပြီးတော့ ပထမဆုံးစာကြောင်းဖြစ်ရမယ်
#အကယ်၍ သူ့အပေါ်မှာ comment မဟုတ် ရင် python interpreter က မသိဘဲ သူ့အပေါ်ကကောင်ကိုပဲ doc string
#လို့ ယူဆသွားတယ်
#advantage of docstring
#program ကို ရှင်းရှင်းလင်းလင်းနဲ့‌နောက်လူတွေ ပြန်ကြည့်ရင်နားလည်အောင် လုပ်လို့ရတယ်
#ကိုယ်ပိုင် function တွေရေးတဲ့ အခါကျရင် ကောင်းတယ်
def myFun(x,y):
    #this is comment
    """ This function return x*y """
    return x*y
print(myFun(1,2))
help(myFun)
print(myFun.__doc__)

