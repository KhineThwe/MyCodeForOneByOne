# Special Operator
# Identity Operator(is,is not(memory locationတွေကိုစစ်ချင်တဲ့အခါမျိုးမှာသုံးလို့ရတယ်))
# (eg:a=10,b=20,c=a is b(memory location ko compare tr)##true or false return)


a = 10
b = 10
# print(id(a))
# print(id(b))
# c = a is b #memory locationကိုပဲ နှိုင်းယှဉ်တာ 
# print(c)

if a is b:
    print('They are same location')
else:
    print('They are not same location')
    
    

a = 20
if a is b:
    print('2.They are same location')
else:
    print('2.They are not same location')


#is not 
x= 10
y=20
if x is not y:
    print('2.They are same location')
else:
    print('2.They are not same location')


#type စစ်ခြင်းရင်လည်းရတယ်
#x=5
#type(x) is int 
#True
#type(x) is not float
# True


#string compare
string1 = 'hello'
string2 = 'hello'
print(id(string1),id(string2))
string3 = string1 is string2
print('The output is',string3)

if string1 == string2:
    print('string 1 and 2 are same: ')
else:
    print('They are not same: ')
