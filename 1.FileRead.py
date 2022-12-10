#Readline and ReadLines
#Readline ---> return string
#Readlines ----> return list \n ပါလာတယ် \n ka new line
file = open('data.txt','r')
file1 = open('data.txt','r')
if file:
    print('Success of opening file')
    data = file.readlines(-1)
    print(data)
    print("Reading with readlines")
    data = file1.readline()
    print(data)
else:
    print("Error")

file.close()
