#CSPRNG
#Cryptographically strong Pseudo-Random Number Generator
#random
#secrets module က python 3.6 မှပါဝင်လာတာ
#security နဲ့ပတ်သတ်တဲ့ sensitive ဖြစ်ရမည့် အခြေအနေမျိုးမှာ အသုံးပြုတယ် 
#token တွေ OTP message တွေ gmail ကို reset ချမယ်ဆိုရင် ကျွန်တော်တို့ gmail ကို လွယ်လွယ် ကူကူ
#နဲ့ ဝင်လို့မရအောင် tokenတွေနဲ့ခံထားတဲ့နေရာတွေမှာသုံးတယ်
import secrets
print('Printing integer number using secrets module')
secureNumber=secrets.SystemRandom()
number_list = [1,2,3,4,5,6,88]
# randomNumber = secureNumber.randint(0,10)
# randomNumber = secureNumber.randrange(0,10,4)
# randomNumber = secureNumber.choice(number_list)
randomNumber = secureNumber.sample(number_list,3)
print('Secure Random Number is',randomNumber)
