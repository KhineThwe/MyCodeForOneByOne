# '''
# Control Structure in Python
# *******************************
# python မှာ switch case statement မရှိဘူး အဲ့အစား if else statement ကိုသာ အသုံးပြုလေ့ရှိသည်။
# program ရဲ့ flow ကို control လုပ်ထားလို့ control structure လို့ခေါ်တယ် 
# Relational Operators
# --------------------
# i.Equals:a==b  a နှင့် b သည် အတူတူပင်ဖြစ်သည်။
# ii.Not Equals:a!=b a နှင့် b သည် မတူပါ။
# iii.Less than: a<b a သည် b ထက်ငယ်သည်။
# iv.Less than or equal to: a<=b a သည် b ထက်ငယ်သည် သို့မဟုတ် ညီသည်။
# v.Greater than: a>b a သည် b ထက်ကြီးသည်။
# vi.Greater than or eqaul to: a>=b a သည် b ထက်ကြီးသည် သို့မဟုတ် ညီသည်။
# -------------------------------------------------------
# 1.if
# 2.if else
# 3.elif

# Logical op ----> and
# '''
# a = 30
# b = 20
# if a < b:
#     print('a<b')
# else:
#     print('a>b')
#largest number



a = 10
b = 20
c = 30
d = 140

if (a>b) and (a>c) and (a>d):
    largestNumber = a 
elif (b>a) and (b>c) and (b>d):
     largestNumber = b
elif (c>a) and (c>b) and (c>d):
     largestNumber = c
else:
    largestNumber = d
print('Largest Number is ',largestNumber)
