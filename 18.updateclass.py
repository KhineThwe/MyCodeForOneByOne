#updating attributes
#manually   -----> class ထဲမှာ method ရေးပြီး update လုပ်တာနဲ့ class outside ကနေ obj ကိုကိုင် ပြီး ပြင်တာ နှစ်မျိုးရှိ
#built in
class Myclass:
    def __init__(self):
        self.name = "NCC"
        self.subject = "Python"
    def update(self):
        self.name = "ncc"
        self.subject = "c++"

o1 = Myclass()
o2 = Myclass()
print('Before update ')#manually update
print(o1.name,o1.subject)
print(o2.name,o2.subject)
# o1.name = "kkk"
# o1.subject = "DSA"
#
# o2.name = "khine"
# o2.subject = "django"
o1.update()
o2.update()
# print('After update manually ')#manually update
print('After update manually from method ')
print(o1.name,o1.subject)
print(o2.name,o2.subject)
