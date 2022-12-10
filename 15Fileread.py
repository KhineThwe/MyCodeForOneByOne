file = open("data.txt","r")
# file2 = open("data1.txt","r")
if file:
    print("Success of opening file")
    data = file.read(4)
    print(data)
else:
    print("Fail of opening file")
file.close()
#data read ---> read fun--> takes one int arg --> no para so yin akone read mal
