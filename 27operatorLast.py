import operator

list = [1,2,3,4,5,6]
output1 = operator.lt(10,20)
output2 = operator.gt(10,20)
output3 = operator.is_('win','htut')
output4 = operator.is_not('win','htut')
output5 = operator.truth(list)#if data exist in list
print(dir(operator))#to list attribute
print(output1)
print(output2)
print(output3)
print(output4)
print(output5)
