#my own reduce function
def mySum(x1,y1):
    return x1+y1

def myReduce(mySum,seq):#seq = list , tuple
    first = seq[0]
    for i in seq[1:]:
        first = mySum(first,i)
    return first
list = [1,2,3,4,5,6]#tuple so ll ya dal # but set tok ma ya set ka unsequence type moe loe#this is drawback
print(myReduce(mySum,list))
