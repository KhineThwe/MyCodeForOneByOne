ls = [1,2,3,4,5]#list
#     0 1 2 3 4
data = 99
found = False
index = 0
     # 4    < 5 
while index < len(ls):
    if ls[index] == data:
        found = True
        break
    index+=1
if not found:
    ls.append(data)
print(ls)
