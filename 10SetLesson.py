#Removing element
#methods2
#1.discard() က မရှိတဲ့ element ကိုထည့်ပေးလိုက်ရင် error မတက်ဘူး
#2.remove()က မရှိတဲ့ element ကိုထည့်ပေးလိုက်ရင် error တက်တယ်

my_set = {1,2,3,4,5,6,7}
my_set.discard(2)
print(my_set)

my_set1 = {1,2,3,4,5,6,7}
my_set1.remove(4)
print(my_set1)

my_set2 = set("HelloPython")
my_set2.pop()
print(my_set2)

# my_set2.clear()
# print(my_set2)

A = {1,2,3,4,5,6,7}
B = {4,5,6,7,8}
print(A|B)#| <===== union operator
print(A.union(B))
print(A&B)# & <===== intersection
print(A.intersection(B))
