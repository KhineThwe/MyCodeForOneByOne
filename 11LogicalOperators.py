# ##Operator in Python Programming
# 1.Arithmetic operator သင်ပြီး 
# 2.Relational Operator သင်ပြီး
# 3.Logical Operators(and,or,not)
#logical Operator in another language & | !
#3.Logical Operators(and,or,not)

a = 10
b = 9
c = 13
# if a>b and c>a:#logical op 
#     print('Both conditions are True')
# else:
#     print('One condition or both are false')
    
if a>b and c>a:#logical op 
    print('Both or one conditions are True')
else:
    print('Both are false')
    
    
#for not logical operator eg
x = True
print('not x is ',not x)
y = False
print('not y is ',not y)


# Python program to demonstrate
# logical not operator 
a = 10
if not a:
    print("Boolean value of a is True")
if not (a%3 == 0 or a%5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")
