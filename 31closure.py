#closure
def myFun(n):
    def adding(data):
        return data+n
    return adding
add10=myFun(10)
print(add10.__closure__)

def test():
    print('Hello')
print(test.__closure__)
print(add10.__closure__[0].cell_contents)#to evaluate parameter value
add20=myFun(20)
print(add20.__closure__[0].cell_contents)
#function or function obj တစ်ခုသည် closure ဖြစ်လားစစ်ရင် cell obj တစ်ခု tuple ပုံစံပြန်ပေးတယ်
