#for loop
#for(int i=0;i<n;i++){
    
#}
# i =0 
# while i<5:
#     print(i)
#     i+=1

i = 0
# for i in range(5):
#     print(i)
z = range(5)#5 ဆိုရင် 0 ကနေ 5 ထိဆိုပေမဲ့ 4 မှာဆုံးတယ်  0 1 2 3 4
for i in z:
    print(i)
    
#for loop with list
# l = [1,2,3,4,5]
# #    0 1 2 3 4
# for i in l:
#     print(i)

#for loop with string
s = 'khine'
for i in s:
    print(i)
    
#for loop with tuple
k = ('a','b','c',3,4,5)
for i in k:
    print(i)

#for loop with list tuple
lt = [(1,2),(3,4),(5,6),(7,8)]#list တစ်ခုထဲမှာ tuple 4 ခုထည့်ထား
    #  0      1    2      3
for i,j in lt:
    print(i,j)
# for i in lt:
#     print(i)
#လက်သည်းကွင်းပါတာကို packing လုပ်ထားတယ်လို့ခေါ်တယ်
#လက်သည်းကွင်းမပါတာကို un-packing လုပ်ထားတယ်လို့ခေါ်တယ်

