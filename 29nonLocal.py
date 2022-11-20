# #non local
# def outerFun():
#     d = 'green'
#     def innerFun():
#         d = 'python'#reassign ပေးပေးမဲ့ မပြောင်းလဲဘူး
#         print('Inner Function Value',d)
#     innerFun()
#     print('Outer Fun',d)
# outerFun()
# #အကုန်လုံးက local ထဲမှာ ရှိရင်တောင် inner ထဲပြုပြုင်ပြောင်းလိုက်ပေမဲ့ outer value ကို affect မဖြစ်စေဘူး

#scoper မတူတဲ့နှစ်ခုကိုပြောင်းလဲစေချင်ရင်
#non local
def outerFun():
    d = 'green'
    def innerFun():
        nonlocal d#use this function တွေထဲမှဆိုပေမဲ့ scope မတူရင်ဒီဟာသုံးတယ်
        d = 'python'
        print('Inner Function Value',d)
    innerFun()
    print('Outer Fun',d)
outerFun()
#အကုန်လုံးက local ထဲမှာ ရှိရင်တောင် inner ထဲပြုပြုင်ပြောင်းလိုက်ပေမဲ့ outer value ကို affect မဖြစ်စေဘူး
