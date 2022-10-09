# (4.Bitwise(^)Xor)(tu yin 0//ma tu yin 1)
#  (5.Bitwise(>>)right shift)(value ka less thwar ml)
# #                     eg: x>>2 (အနောက်ဆုံးနှစ်လုံးကို ညာဘက်ကိုတွန်းထုတ်မယ်။0တွေက ဘယ်ဘက်ကနေဝင်)
# #                    (6.Bitwise(<<)left shift))(value ka greater thwar ml)
# #                     eg: x>>2 (အနောက်ဆုံးနှစ်လုံးကို ဘယ်ဘက်ကိုတွန်းထုတ်မယ်။0တွေက ညာဘက်ကနေဝင်)

#XOR result
a = 5
b = 3
c = a ^ b
print('Xor result: ',c)


#Right Shift
x = 10
#Decimal value of x = 000010    10
#After Right Shift => 000000    10
y = x >> 2
print('After Right Shift',y)


#Left Shift
x = 10
#Decimal value of x = 000010    10
#After Left Shift => 00001010  00
y = x << 2
print('After Left Shift',y)
