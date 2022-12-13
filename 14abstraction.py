#abstraction
#မသိစေချင်တဲ့အပိုင်းတွေကို ဖုံးအုပ်ထားတာကို abstraction လို့ခေါ်တယ်
#ကားအကြောင်းမသိဘဲကားမောင်းလို့ရသလိုမျိူးပဲ သို့မဟုတ် တီဗီမှာရှိတဲ့ ခလုတ်နှိပ်ရင် လိုင်းပြောင်းတယ် ခလုတ်နှိပ်ရုံပဲ
#အထဲက Hidden layer ကိုသိစရာမလိုတာမျိုး
#application တစ်ခုမှာရှိတဲ့တချို့ဟာတွေကို hide လုပ်ထား program ရဲ့ efficiency ပိုကောင်းလာမယ်
#abstract class နဲ့ abstract method နှစ်ခုရှိ
#class တစ်ခုရှိမယ် inheritance လုပ်ထားတဲ့ subclass တစ်ခုရှိမယ် သူ့ထဲမှာ abstract method 1 or more ပါဝင်ရမယ်အာ့တာကို abstract class လို့ခေါ်
#abc module ----> abstract base class
#abstract class ဖြစ်ဖို့ abstract method ရှိရမယ်
#abstract class ထဲရှိ abstract method က declare ပဲလုပ်ထားတာ သူ့ကိုလှမ်းခေါ်မှ implement လုပ်ပေးတယ်
from abc import ABC,abstractmethod
#ABC for class
class Price(ABC):#abstract class
    def print_slip(self,amount):
        print('Payment amount $',amount)
    @abstractmethod#to become abstract method
    def payment(self):
        # pass
        print("This is important from abstract method")
# p = Price()
# p.print_slip()
# Can't instantiate abstract class Price with abstract method payment
#abstract class ကိုအပေါ်ကပုံစံသုံးလို့မရ
class CreditCardPayment(Price):
    def payment(self,amount):
        super().payment()
        print("Payment with Credit Card $",amount)
class MobileBanking(Price):
    def payment(self,amount):
        super().payment()
        print("Payment with Mobile Banking ",amount)

obj = CreditCardPayment()
obj.print_slip(10000)
obj.payment(1000)

obj1 = MobileBanking()
obj1.print_slip(10000)
obj.payment(100)
