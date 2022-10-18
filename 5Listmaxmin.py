#max min function
from audioop import reverse


numList =  [1,2,3,45,44,88,99]
print(max(numList))
print(min(numList))


#reverse method 
#index method
# numList.reverse()
print('After reversing',numList)
myIndex = numList.index(99)
print('my index',myIndex)

#sum function

sumAllvalues = sum(numList)
print(sumAllvalues)

#sort
#ငယ်စဉ်ကြီးလိုက်စီပေးတာ
numList.sort()
print(numList)
fruitList = ['apple','banana','orange','watermelon']
# fruitList.sort(reverse=True)
# print(fruitList)

#sort by length
#element ရဲ့ length ပေါ်မူတည်၍ စီစေရန်
fruitList.sort(key=len,reverse=True) #default ငယ်စဉ်ကြီးလိုက်
print(fruitList)

#ကြီးစဉ်ငယ်လိုက်စီပေးတာ
numList.sort(reverse=True)
print(numList)

