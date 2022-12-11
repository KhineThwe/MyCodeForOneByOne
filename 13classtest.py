#ပထမဆုံး oop ကိုနားလည်ဖို့ဆိုရင် class ကိုနားလည်ရမယ်
# ပြီးရင်သူ့ကိုကိုယ်စားပြုထားတဲ့ obj ကိုနားလည်ရမယ်
#class name ရှေ့ဆုံးစကားလုံး အကြီး -----> naming conversion အရ -----> PEP 8 မှာသွားရှာဖတ်လို့ရတယ်
#attribute ---> သူ့ထဲမှာရှိတဲ့ variable ---> in c++ property
#behavior  ----> သူ့ထဲမှာပါတဲ့ method ---> class ရဲ့အောက်မှာရေးထားတဲ့ ဟာ function

class Myclass:
    def myFun(self):
        pass
obj1 = Myclass()#constructor#class ကိုလှမ်းခေါ်တာနဲ့တစ်ပြိုင်နက်တည်းအလုပ်လုပ်ပေးတယ်
#class ကိုကိုယ်စားပြုထားတဲ့ကောင်ကို object လို့ခေါ်တယ်
#obj တွေများကြီးဆောက်လို့ရတယ်
obj2 = Myclass()
print(obj1)
print(obj2)
if id(obj1) == id(obj2):
    print("Addresses are equal")
else:
    print("They are not same ")
#class တူသော်လည်းပဲ class တစ်ခုကိုကိုယ်စားပြု၍ ဆောက်ထားသော objတွေက လုံးဝမတူဘူး memory address လည်းမတူဘူး
#obj မဆောက်ထားရင် Myclass.myFun() ဆိုပြီးတစ်ခါပဲသုံးလို့ရတော့တယ်
