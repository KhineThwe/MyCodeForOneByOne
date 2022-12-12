#polymorphism
#poly ----> အများကြီး
#morphism ---> ပုံစံ
#class တိုင်းမှာ method တစ်ခုစီရှိမယ် class တိုင်းမှာ ရှိတဲ့ method တိုင်းကတူ ပြီး class ကွဲပြား name တူသော်လည်း behavior ကမတူဘူး
class AgAg:
    def human(self):
        print("AgAg is a programmer")
        print("AgAg is always coding")

class MgMg:
    def human(self):
        print("MgMg is a hacker")
        print("MgMg is always learning")

class KoKo:
    def human(self):
        print("MgMg is a scientist")
        print("MgMg is always testing")

class People:
    def fun(self,obj):
        obj.human()
agag = AgAg()
mgmg=MgMg()
koko = KoKo()
people = People()
people.fun(agag)
myList = [agag,mgmg,koko]
for obj in myList:
    people.fun(obj)
