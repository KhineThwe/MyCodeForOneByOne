#memorization
#cache decorator
#funtools module ထဲကပဲခေါ်သုံးရမှာ
#လုပ်ပြီးသားအလုပ်တွေကို ထပ်ခါထပ်ခါ မရေးတော့ဘဲ မှတ်ထားပြီး ပြန်သုံးမယ်
#fibonnacci or factorial တွေဆိုတာက ထပ်ခါထပ်ခါအလုပ်လုပ်မယ့်ကောင်တွေ
#0 1 1 2 3 5 8
#programming နည်းအရဆိုformula အရ fn = (fn - 1) + (fn - 2)
def fibo(n):
    print('Calculating fibo{0}'.format(n))
    return 1 if n<3 else fibo(n-1) + fibo(n-2)

print(fibo(6))
#နောက်ကွယ်မှာလုပ်ပြီးသား step တွေပြန် ပြန်အလုပ်လုပ်နေတဲ့ကိစ္စမျိုးမဖြစ်ရအောင်လို့ memo လုပ်မယ်
