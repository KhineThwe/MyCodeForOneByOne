# issubclass(child,parent)#child classသည် parent class ၏ sub class ဖြစ်လား
# isinstance(obj,class)#ဒီ obj သည် ဒီ class ၏ instance obj ဖြစ်သလား
#class တွေများလာတဲ့အချိန်မျိူးဆို ဒီနည်းနဲ့စစ်လို့ရ

class Parent:
    pass
class Child(Parent):
    pass

print(issubclass(Child,Parent))
obj = Child()
print(isinstance(obj,Parent))
print(isinstance(obj,Child))
