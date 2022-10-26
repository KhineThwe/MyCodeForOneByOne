#find largest number

def find_largest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

largestNo = find_largest(1,5,8)
print(largestNo)
