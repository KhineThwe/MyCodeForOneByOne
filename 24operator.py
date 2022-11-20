import operator
from functools import reduce

print(operator.add(3,5))
print(operator.mul(3,5))
print(operator.truediv(3,2))
print(operator.floordiv(13,2))

#reduce and lambda
list = [1,2,3,4,5,6]
output1 = reduce(lambda x,y:x*y,list)
print("output form the reduce and lambda: ",output1)

#reduce and operator
output2 = reduce(operator.mul,list)
print("output from the reduce and operator: ",output2)

