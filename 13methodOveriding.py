#parent class ထဲကအတိုင်း child class မှာလိုက်ရေးထားတဲ့ method က ခေါ်ရင် child ကဟာပဲထွက်လာမယ်
#overide lote ခံရလို့
#method overriding
class Price():
    def payment(self):
        print("From Parent Class")
class Child(Price):
    def payment(self):
        print("From Child Class")
class GrandChild(Child):
    def payment(self):
        print("From GrandChild Class")
obj = GrandChild()
obj1 = Child()
obj1.payment()
obj.payment()
