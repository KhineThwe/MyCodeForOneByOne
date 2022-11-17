def myGen():
    data = 1
    while data<=10:
        square=data*data
        yield square
        data+=1
results = myGen()
for i in results:
    print(i)
