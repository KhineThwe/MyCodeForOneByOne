numberList = [1,2,3,4,5,6]
#[:3] 0 1 2
for e in numberList[:3]:
	numberList.remove(e)
	print('removing element',e)
print(numberList)

numList = []
for element in range(1,10):# 1 2 3 4 ---- 9
	data = element**2#1 4
	numList.append(data)
	print('appending = ',data)
print(numList)



