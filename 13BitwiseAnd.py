# 4.Bitwise Operators 6 ခုရှိ
# (1.Bitwise(&)And--->0 & 0 = 0,0 & 1 = 0,1 & 0 = 0,1 & 1 = 1//bit by bit operation)
#                    (2.Bitwise(|)or----->0 | 0 = 0,0 | 1 = 1,1 | 0 = 1,1 | 1 = 1)
#                    (3.Bitwise(~)Not or One's complement)(eg:1s complement ka convert lote 1 ကို 0,0 ကို 1 change >>a=~10>>same>>a=-(10+1))
# (eg:2s complement ko sign change chin yin use>>အကုန်လုံးကို ko invert a kone change pi yin 1 plus tr)
# sign change twar naing အပေါင်းကိန်းကနေ အနုတ်ပြောင်းသို့မဟုတ် အနုတ်ကနေ အပေါင်းပြောင်းချင်ရင်သုံး
#                    (4.Bitwise(^)Xor)(tu yin 0//ma tu yin 1)
#                    (5.Bitwise(>>)right shift)(value ka less thwar ml)
#                     eg: x>>2 (အနောက်ဆုံးနှစ်လုံးကို ညာဘက်ကိုတွန်းထုတ်မယ်။0တွေက ဘယ်ဘက်ကနေဝင်)
#                    (6.Bitwise(<<)left shift))(value ka greater thwar ml)
#                     eg: x>>2 (အနောက်ဆုံးနှစ်လုံးကို ဘယ်ဘက်ကိုတွန်းထုတ်မယ်။0တွေက ညာဘက်ကနေဝင်)

#Bitwise (&) And
#Bitwise (|) Or
#Bitwise (~) Not or One's Complement
#Bitwise (^) Xor
#Bitwise (>>) right shift
#Bitwise (<<) Left shift



#Bitwise (&) And 
#Logical Op နဲ့အနည်းငယ်ဆင်တယ် 
#1 ka True 0 ka False
#x y | xy(output)
#0 0 | 0
#0 1 | 0
#1 0 | 0
#1 1 | 1
#Bit operator သည် bit by bit operation ပြုလုပ်သည်။ Bit တစ်ခုချင်းစီလုပ်ပေး
#decimal ka နေ Binary value change pi တော့ operation ပြုလုပ်ပေးမည်။ 
# အဲ့လိုပြောင်းဖို့ဆိုရင် 2 နှင့် ထို ပြောင်းမည့် value ကိုစားပေးရန် လိုအပ်သည်။ 
#2 | 60   0
#2 | 30   0
#2 | 15   1
#2 | 7    1
#2 | 3    1
#    1
#Decimal 60 = 111100 အောက်ကနေအပေါ်ကိုစ ရေတွက် 
#Decimal 13 = 1101
# 1 1 1 1 0 0
#     1 1 0 1
#_____________________
#0 0  1 1 0 0
#https://www.rapidtables.com/convert/number/decimal-to-binary.html
#1 byte = 8 bits(00000000)
a = 60
b = 13
c = 0
c = a & b
print('bitwise and operation: ',c)
