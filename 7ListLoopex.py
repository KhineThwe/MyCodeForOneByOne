numberList = [1,2,3,4,5,88,99]

for e in numberList[:3]:
    numberList.remove(e)
    print('removing element',e)
print(numberList)

numList = []
for element in range(1,10):
    data = element**2
    numList.append(data)
    print('appending = ',data)
print(numList)
