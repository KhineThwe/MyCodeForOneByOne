#operator overloading ဆိုတာက arithmetic လုပ်လို့မရတဲ့ကောင်တွေကို arithmetic လုပ်လို့ရအောင်လုပ်ခဲ့ကြတယ်
#method overloading ---> method က တစ်ခုပဲရှိတယ် method ကိုလှမ်းခေါ်ကြတဲ့ချိန်မှာ parameter ကြိုက်သလောက် ထည့်ခေါ်လို့ရ
#function declare လုပ်ထားချိန်မှာတော့ ကြိုက်သလို declare လုပ်ထားမယ် လှမ်းခေါ်ရင်လဲမိမိကြိုက်နှစ်သက်သလိုလှမ်းခေါ်လို့ရရမယ်
#python မှာတော့ မပါမဖြစ်အနေနဲ့ self ပါရမယ် method မှာ
class Price:
    def payment(self,x=None,y=None):#parameter 1 or 2 br pyit pyit alote lote mal
        if x!=None and y!=None:
            return x*y
        elif x!=None:
            return x*x
        else:
            return None
obj = Price()
print(obj.payment(7,6))
#parameter များကြီးပိုထည့်မိရင်ဒီ နည်းက အဆင်မပြေပါ။

