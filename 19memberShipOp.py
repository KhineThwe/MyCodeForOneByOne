# Membership Operator အများနဲ့ပတ်သတ်တဲ့ဟာတွေထဲမှာရှိတဲ့ data တွေကိုစစ်ဆေးချင်တဲ့အခါမျိုးမှာသုံး
# <list,tuple,dict,set twal htl ka data twal check chin yin>
#    # in 
#    # not in
# (Memory location စစ်ချင်ရင်သုံးတယ်။)
list1 = [1,2,3,4,5,'w']
list2 = [1,2,3,4,5]
print(1 in list1)
if 'w' in list1:
    print('w is in list1: ')
print(2 not in list2)

#program2
x = 24
y = 20
myList = [10,20,30,40,50,60,70]
if x not in myList:
    print('#x not in given myList')
else:
    print('x is present in given myList')


if y in myList:
   print('#y is in myList')
else:
    print('y is noy in myList')


#overlap program another
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]


def overlap(list1,list2):
    c = 0
    d = 0
    for i in list1:
        c+=1
    for i in list2:
        d+=1
    for i in range(0,c):
        for j in range(0,d):
            if list1[i] == list2[j]:
                return 1     
    return  0

if(overlap(list1,list2)):
    print('They are overlap')
else:
    print('not overlap')
#Debug lote ၍ ပြရန်
#1 ဆိုလည်း 6,7,8,9 nae tu lr

