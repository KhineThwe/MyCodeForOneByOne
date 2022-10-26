#arbitary argument or end of positional argument or variable length non keyword argument
#exercise

def avg(*args):
    length = len(args)
    total = sum(args)
    if length == 0:
        return 0
    else:
        return total/length

result = avg(1,2,3,4,5)
print(result)
