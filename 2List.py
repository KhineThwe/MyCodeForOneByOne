#List methods
#List ထဲမှ data ထုတ်ချင်လျှင် သုံး
#1.clear တန်ဖိုးတွေတစ်ပြိုင်တည်းဖြတ်ချင်ရင်သုံး
#2.pop Index no နဲ့ဖြတ် index မပါရင် default က last ကဟာပျက်မယ် remove လုပ်လိုက်တဲ့တန်ဖိုးကိုလည်း returnပြန်ပေးတယ် 
#အာ့တာကို var နဲ့ store pi pyan ထုတ်လို့ရတယ် 
#3.remove obj ကိုတိုက်ရိုက်ဖြတ်တယ်ဆိုတဲ့ ပုံစံမျိုး remove ka return pyan ma pay tok buu
from ast import Num


numbers = [22,32,45,66]
# numbers.clear()
print(numbers)
x = numbers.pop()
print(numbers)
print(f'Remove element is:{x}')

colors = ["Red","Green","Blue","Yellow"]
y = colors.remove("Blue")
print(f'Remove element is:{y}')
print(colors)
