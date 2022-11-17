#to make arg less
#partial fun
#to understand this we need to understand preset values
def myFun(x,y,z):
    print(x,y,z)

#own partial fun
def pFun(yy,zz):
    return myFun(10,yy,zz)#10 ka preset value=default value

pFun(100,200)
