#class built in attribute
#class တစ်ခုကို စcreate လုပ်လိုက်တာနဲ့ built in attribute တွေကပါတယ်
#class တစ်ခုမှာ built-in attr 5 ku shi
#1.__dict__ အချက်အလက်အားလုံးကိုဖော်ပြ
#2.__doc__  class တစ်ခုရဲ့ မှတ်ချက်တွေကိုဖော်ပြ
#3.__name__ class ရဲ့ name ကိုရလိုသောအခါသုံး
#4.__module__
#5.bases ဒီ class မှာဘယ် base class တွေရှိလဲဆိုတာမျိုး class တစ်ခုကနေခွဲသွားတဲ့ကောင် inheritance ----> nae twal use လေ့ရှိတယ်
class MyClass:
    variable = "programming"
    def active(self):
        print(f'hello from {MyClass.variable}')
print(MyClass.__dict__)#return dictionary format
