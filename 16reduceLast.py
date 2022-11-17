import functools
li = {1,2,3,4,5,6}#reduce fun mhar tok set so ll a lote lote tal
print("The sum of all elements from list: ",end="")
print((functools.reduce(lambda a,b:a*b,li)))
