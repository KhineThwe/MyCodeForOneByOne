#Generator Function
def myFun(x):
    return x
#normal fun terminate
#1 ခုပဲ return pyan pay loe ya dal
def myGen():
    data = 10
    yield data
    yield data+1
    yield data+2
    yield data+3
#not terminate suspend
results = myGen()
print(results)
# print(results.__next__())
# print(results.__next__())
# print(results.__next__())
# print(results.__next__())
#for loop ထဲမှာ next ka shi nay p thar moe loe akone output ya nay mhar
for i in results:
    print(i)
