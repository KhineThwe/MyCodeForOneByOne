#zip function
#takes two parameter
#first parameter ka iterable 2 ku
#tuple ponesone return pyan
#map function က တစ်ခုပဲ return pyan
itr1 = [1,2,3,4,5]
itr2 = [10,20,30,40,50]

# results = zip(itr1,itr2)#1 ku pl return
# print(results)
# for i in results:
#     print(i)
# for x in results:
#     print(x)

results = list(zip(itr1,itr2))
for y in results:
    print(y)
for z in results:
    print(z)
