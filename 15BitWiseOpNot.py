# (3.Bitwise(~)Not or One's complement)(eg:1s complement ka convert lote 1 ကို 0,0 ကို 1 change >>a=~10>>same>>a=-(10+1))
# (eg:2s complement ko sign change chin yin use>>အကုန်လုံးကို ko invert a kone change pi yin 1 plus tr)
# sign change twar naing အပေါင်းကိန်းကနေ အနုတ်ပြောင်းသို့မဟုတ် အနုတ်ကနေ အပေါင်းပြောင်းချင်ရင်သုံး
#Bitwise (~) Not or One's Complement
#a = 10 
#  =-(a+1)

#Decimal value of 10 = 1 0 1 0
# 1 0 1 0
#       1
#_________________
#  1 0 1 1  =====>    11
a = ~10
print("bitwise not or one's complement",a)


#2's complement
#Decimal value of 10 = 1010
#ပထမအဆင့်အနေနဲ့ အပေါ်က value အကုန်လုံးကို convert လုပ်ရမယ်
#ပြီးရင် 1 ပေါင်းရမယ်
#eg:
#1 0 1 0
#0 1 0 1 ဖြစ်တယ် (inverse result)
#Inverse result ကို 1 ပေါင်းရမယ်
# 0 1 0 1
#       1
#________________
#  0 1  1 0
#ဒါပေမဲ့ရလာသော result သည် sign ချိန်းသွားမည်ဖြစ်သည်။ 

