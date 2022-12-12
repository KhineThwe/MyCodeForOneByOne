#Encapsulation
#ဆိုတာ class တစ်ခုအတွင်းမှာရှိတဲ့ method တွေ အကုန်လုံးကို encapsulate လုပ်ထားတာ
#တခြားသော programming language တွေမှာဆိုရင် private public protected access specifierတွေရှိပေမဲ့ python မှာတော့
#private ----> __varname or __methodName
#protected ---> _varname လို့ရေးတယ် or _methodName
class Parent:#base class
    def __init__(self,age):
        self._age = age#don't touch from the outside#protected
        #c++ မှာတော့ သူ့ကို derived လုပ်ထားတဲ့ class ကနေပြီးတော့ မှ access လုပ်ခွင့်ရှိတယ် ဒါပေမဲ့ python မှာကျ protected ဆိုသော်လည်း class ရဲ့ အပြင်ကနေလှမ်းခေါ်သုံးလို့ရတယ်
        #modify လုပ်လို့တော့ရတယ် ဒါပေမဲ့ official doc တွေမှာတော့ method ထဲကနေပဲ access လုပ်ပါပေါ့

class Sub(Parent):
    def getData(self):
        print(self._age)

obj = Sub(100)
obj.getData()
# obj._age = 20
# print(obj._age)
